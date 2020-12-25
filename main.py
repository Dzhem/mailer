import lib
import json


with open("mail.json", "r") as file:
    data = json.load(file)

login = data["login"]
passwd = data["passwd"]
host = data["smtp_server"]
port = data["port"]

mail = lib.Mail(host, login, passwd, port)
mail.getHost()
mail.login_mail()
lib.mailer(mail, 'base.csv', delay=0)
mail.exit()


