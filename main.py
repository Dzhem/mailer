import lib
import json


with open("mail.json", "r") as file:
    data = json.load(file)

login = data["login"]
passwd = data["passwd"]
host = "smtp.mail.ru"

mail = lib.Mail(host, login, passwd)
mail.getHost()
mail.login_mail()
lib.mailer(mail, 'base.csv')
mail.exit()


