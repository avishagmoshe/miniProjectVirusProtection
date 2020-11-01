import file_generator
import sending_mail
def main():
    file_generator.random_files_generator()
    send_from = 'rmf.mini2020@gmail.com'
    send_to = ['rmf.mini2020@gmail.com']
    subject = 'We promise you this is not a virus'
    text = 'Hello , we send you the file you wanted.'
    user_name = 'rmf.mini2020@gmail.com'
    user_passport = 'rotem600'
    email_server = ('smtp.gmail.com', 465)
    files = ['firstFile.txt', 'secondFile.txt']

    sending_mail.send_mail(send_from,send_to,subject,text,user_name,user_passport,email_server,files)

if __name__ == '__main__':
    main()


