import smtplib
import time
import csv


class Mail():
    def __init__(self, host: str, login: str, passwd: str, port: int = 587):
        self.host = host
        self.login = login
        self.passwd = passwd
        self.port = port

    def getHost(self):
        try:
            self.sender = smtplib.SMTP(self.host, self.port)
            self.sender.starttls()
        except smtplib.SMTPConnectError:
            print("Ошибка соединения")

    def login_mail(self):
        self.sender.login(self.login, self.passwd)

    def send_message(self, email: str, message: str, limit: int = 1):
        for i in range(limit):
            self.sender.sendmail(self.login, email, message)
            print("Отправленно сообщение")

    def flood(self, email: str, message: str, time_: int = 2):
        while True:
            self.sender.sendmail(self.login, email, message)
            time.sleep(time_)

    def exit(self):
        self.sender.close()


def mailer(mail_obj, csv_file, message):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            message_ = f'{message} {row["name"]} {row["email"]}'
            mail_obj.send_message(row['email'], message_)
            time.sleep(61)
