import random
import string
import virus_scan
def random_files_generator():
    maliciousStr = 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*\n'

    firstFile = open("firstFile.txt", "w")
    secondFile = open("secondFile.txt", "w")
    randomRange = random.randint(100,200)
    randomLine = random.randint(0,randomRange)
    randomSpace = random.randint(10,20)
    for i in range(0, randomRange):
        if i == randomLine:
            if i % 2 == 0:
                firstFile.write("\n")
                firstFile.write(maliciousStr)
            else:
                secondFile.write("\n")
                secondFile.write(maliciousStr)
        if i % randomSpace == 0:
            firstFile.write("\n")
            secondFile.write("\n")
        firstFile.write(random.choice(string.ascii_letters))
        secondFile.write(random.choice(string.ascii_letters))
    firstFile.close()
    secondFile.close()
    if(virus_scan.virus_scan('firstFile.txt')):
        print('firstFile clean')
    else:
        print('virus in firstFile')
    if(virus_scan.virus_scan('secondFile.txt')):
        print('secondFile clean')
    else:
        print('virus in secondFile.txt')
