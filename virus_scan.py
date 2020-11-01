import binascii
import hashlib


def crc32_check(file, crc_str):

    for line in file:
        result = hex(binascii.crc32(line.encode('utf-8')))
        if result == crc_str:
            return 1
    return 0

def hashCheck(file,hashName,strValue):
    if hashName is "MD5":
        hash_function = hashlib.md5
    elif hashName is "SHA1":
        hash_function = hashlib.sha1
    elif hashName is "SHA224":
        hash_function = hashlib.sha224
    elif hashName is "SHA256":
        hash_function = hashlib.sha256
    elif hashName is "SHA384":
        hash_function = hashlib.sha384
    elif hashName is "SHA512":
        hash_function = hashlib.sha512


    for line in file:

        implamentor = hash_function()
        implamentor.update(line.encode('utf-8'))
        val = implamentor.hexdigest()
        if val == strValue:
            return 1

    return 0

def virus_scan(path):
    with open(path, "r") as fil:
        file = fil.readlines()

        flagFile = 0
        strCRC32 = "1dd02bdb"
        strMD5 = "69630e4574ec6798239b091cda43dca0"
        strSHA1 = "cf8bd9dfddff007f75adf4c2be48005cea317c62"
        strSHA224 = "a2e3aa5b0d6b05643f99e619c2d16deef927d171861477696be5b4c0"
        strSHA256 = "131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267"
        strSHA384 = "10cc0011d21012867900a17757c239025dac46589f8e08ef93916d773a1dcc6257b357e408112d0d09fc9d3401d25700"
        strSHA512 = "5581f85b25f0d80fa84c69e7ca24d98344f5fbaec45b7707dccf139a8c065961391d6e762516ee1db3137c4d82eca7fbc67c348c37ea0d615bb88161cf3b3008"

        flagFile += crc32_check(file,strCRC32)
        flagFile += hashCheck(file, "MD5", strMD5)
        flagFile += hashCheck(file, "SHA1", strSHA1)
        flagFile += hashCheck(file, "SHA224", strSHA224)
        flagFile += hashCheck(file, "SHA256", strSHA256)
        flagFile += hashCheck(file, "SHA384", strSHA384)
        flagFile += hashCheck(file, "SHA512", strSHA512)
    if flagFile < 4:
        return True
    return False