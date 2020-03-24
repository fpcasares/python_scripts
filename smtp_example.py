import smtplib
from email.mime.text import MIMEText
from getpass import getpass


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = ""
SMTP_PASSWORD = ""
EMAIL_FROM = "camerahous@gmail.com"
EMAIL_TO = "fpcasares@gmail.com"
EMAIL_SUBJECT = "Email Subject"
co_msg = "This is the body of the email"


def send_email():
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    SMTP_USERNAME=raw_input('Ingrese usuario de email de gmail\n')
    SMTP_PASSWORD=getpass('Ingrese password de email de gmail\n')
    send_email()

