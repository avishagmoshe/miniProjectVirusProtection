
import smtplib
import virus_scan
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
def send_mail(send_from, send_to, subject, text,user_name, user_password ,email_server,files=None ):
    assert isinstance(send_to, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        if virus_scan.virus_scan(f):
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
        else:
            print('virus found in file ',f,' file was\'nt attach')

    server = smtplib.SMTP_SSL(*email_server)
    server.ehlo()
    server.login(user_name, user_password)
    server.sendmail(send_from, send_to, msg.as_string())
    server.close()

