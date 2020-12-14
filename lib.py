import smtplib
import time
import csv
from email.message import EmailMessage


class Mail:
    def __init__(self, host: str, login: str, passwd: str, port: int = 587):
        self.host = host
        self.login = login
        self.passwd = passwd
        self.port = port

    def getHost(self):
        try:
            self.sender = smtplib.SMTP(self.host, self.port)
            self.sender.ehlo()
            self.sender.starttls()
            self.sender.ehlo()
        except smtplib.SMTPConnectError:
            print("Ошибка соединения")

    def login_mail(self):
        self.sender.login(self.login, self.passwd)

    def send_message(self, msg, limit: int = 1):
        for i in range(limit):
            self.sender.send_message(msg)
            print("Отправленно сообщение")

    def exit(self):
        self.sender.close()


def mailer(mail_obj: Mail, csv_file):
    msg = EmailMessage()
    msg['Subject'] = 'Тема тестового сообщения'
    msg['From'] = mail_obj.login
    msg.set_content('Это тестовое пистьмо.')

    mail_html = ''
    with open('index.html') as f:
        mail_html = f.read()

    msg.add_alternative(mail_html, subtype='html')

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                msg.replace_header('To', row['email'])
            except KeyError:
                msg['To'] = row['email']

            mail_obj.send_message(msg)
            time.sleep(61)
