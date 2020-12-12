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

    msg.add_alternative("""
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    <html>
    <head>
        <meta http-equiv="content-type" content="text/html" charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body{
                background-color: #ffffff;
                padding: 20px 0;
                margin: 0 auto;
            }
            table{
                max-width: 600px;
                width: 100%;
                border-collapse: collapse;
                border-spacing: 0;
                margin: 0 auto;
                padding: 0;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
            }
            td{
                margin: 0;
                padding: 0;
            }
            .wrap-tabli-email,
            .table-content,
            .table-footer{
                background-color: #eeeeee;
            }
            img{
                outline: none;
                -ms-interpolation-mode: bicubic;
                display: block;
                margin: 0 auto;
                padding: 0;
            }
            .tabel-heder{
                background-color: #8FD8F7;
            }
            .td-header{
                font-family: Arial, Helvetica, sans-serif;
                color: #333333;
                font-size: 16px;
                line-height: 22px;
                mso-line-height-rule: exactly;
                font-style: normal;
                font-weight: bold;
                letter-spacing: normal;
                text-align: center;
                padding: 15px 5px;
            }
            .content-img{
                width: 30%;
            }
            .td-content-text{
                font-family: Arial, Helvetica, sans-serif;
                color: #333333;
                font-size: 14px;
                line-height: 20px;
                mso-line-height-rule: exactly;
                font-style: normal;
                font-weight: normal;
                letter-spacing: normal;
                text-align: left;
                padding: 15px 10px;
            }
            .td-content-btn{
                text-align: center;
                padding: 20px 0 30px;
            }
            .content-btn{
                background-color: #0d89c7;
                font-family: Arial, Helvetica, sans-serif;
                color: #ffffff;
                font-size: 14px;
                line-height: 20px;
                mso-line-height-rule: exactly;
                font-style: normal;
                font-weight: normal;
                letter-spacing: normal;
                text-align: center;
                padding: 15px 25px;
            }
            .td-social-title{
                font-family: Arial, Helvetica, sans-serif;
                color: #333333;
                font-size: 14px;
                line-height: 20px;
                mso-line-height-rule: exactly;
                font-style: italic;
                font-weight: normal;
                letter-spacing: normal;
                text-align: center;
                padding: 20px 0 5px;
            }
            .content-btn,
            .social-btn{
                text-decoration: none;
            }
            .table-social-btns{
                width: 240px;
            }
            .td-social-btn{
                width: 40px;
                padding: 0 0 20px;
            }
            .social-img{
                max-width: 32px;
                max-height: 32px;
            }
            .td-freepik{
                font-family: Arial, Helvetica, sans-serif;
                color: #333333;
                font-size: 10px;
                line-height: 18px;
                mso-line-height-rule: exactly;
                font-style: italic;
                font-weight: normal;
                letter-spacing: normal;
                text-align: center;
                padding: 20px 0 0;
            }
        </style>
    </head>
    <body style="background-color:#ffffff;padding-top:20px;padding-bottom:20px;padding-right:0;padding-left:0;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;" >
        <table class="wrap-tabli-email" align="center" border="0" bgcolor="#eeeeee" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;width:100%;border-collapse:collapse;border-spacing:0;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;mso-table-lspace:0pt;mso-table-rspace:0pt;background-color:#eeeeee;" >
            <tbody>
                <tr>
                    <td class="wrap-td-header" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;" >
                        <table class="table-header" align="center" border="0" bgcolor="#8FD8F7" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;width:100%;border-collapse:collapse;border-spacing:0;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;mso-table-lspace:0pt;mso-table-rspace:0pt;" >
                            <tbody>
                                <tr>
                                    <td class="td-header" align="center" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;font-family:Arial, Helvetica, sans-serif;color:#333333;font-size:16px;line-height:22px;mso-line-height-rule:exactly;font-style:normal;font-weight:bold;letter-spacing:normal;text-align:center;padding-top:15px;padding-bottom:15px;padding-right:5px;padding-left:5px;" >
                                        Приглашаем принять участие
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td class="wrap-td-content" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;" >
                        <table class="table-content" align="center" border="0" bgcolor="#eeeeee" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;width:100%;border-collapse:collapse;border-spacing:0;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;mso-table-lspace:0pt;mso-table-rspace:0pt;background-color:#eeeeee;" >
                            <tbody>
                                <tr>
                                    <td class="td-content-img" align="center" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;" >
                                        <img class="content-img" alt="эмблема конкурса" width="30%" src="https://r1.nubex.ru/s13952-3ac/f488_62/grenaders_logo_2019.png" style="outline-style:none;-ms-interpolation-mode:bicubic;display:block;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;width:30%;" >
                                    </td>
                                </tr>
                                <tr>
                                    <td class="td-content-text" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;font-family:Arial, Helvetica, sans-serif;color:#333333;font-size:14px;line-height:20px;mso-line-height-rule:exactly;font-style:normal;font-weight:normal;letter-spacing:normal;text-align:left;padding-top:15px;padding-bottom:15px;padding-right:10px;padding-left:10px;" >
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Unde culpa nulla perspiciatis in vitae maxime laborum doloremque, aperiam sed harum molestias nihil facere facilis esse aspernatur eveniet quia tenetur magnam.
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center" class="td-content-btn" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;text-align:center;padding-top:20px;padding-bottom:30px;padding-right:0;padding-left:0;" >
                                        <a class="content-btn" target="_blank" href="#" style="background-color:#0d89c7;font-family:Arial, Helvetica, sans-serif;color:#ffffff;font-size:14px;line-height:20px;mso-line-height-rule:exactly;font-style:normal;font-weight:normal;letter-spacing:normal;text-align:center;padding-top:15px;padding-bottom:15px;padding-right:25px;padding-left:25px;text-decoration:none;" >Button</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
                <tr>
                    <td class="wrap-td-footer" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;" >
                        <table class="table-footer" align="center" border="0" bgcolor="#eeeeee" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;width:100%;border-collapse:collapse;border-spacing:0;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;mso-table-lspace:0pt;mso-table-rspace:0pt;background-color:#eeeeee;" >
                            <tbody>
                                <tr>
                                    <td style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;" >
                                        <table class="table-social-title" align="center" border="0" bgcolor="#eeeeee" cellpadding="0" cellspacing="0" width="100%" style="max-width:600px;width:100%;border-collapse:collapse;border-spacing:0;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;mso-table-lspace:0pt;mso-table-rspace:0pt;" >
                                            <tbody>
                                                <tr>
                                                    <td class="td-social-title" align="center" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;font-family:Arial, Helvetica, sans-serif;color:#333333;font-size:14px;line-height:20px;mso-line-height-rule:exactly;font-style:italic;font-weight:normal;letter-spacing:normal;text-align:center;padding-top:20px;padding-bottom:5px;padding-right:0;padding-left:0;" >
                                                        Мы в социальных сетях
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;" >
                                        <table class="table-social-btns" align="center" border="0" bgcolor="#eeeeee" cellpadding="0" cellspacing="0" width="240px" style="max-width:600px;border-collapse:collapse;border-spacing:0;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;mso-table-lspace:0pt;mso-table-rspace:0pt;width:240px;" >
                                            <tbody>
                                                <tr>
                                                    <td class="td-social-btn" width="40px" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;width:40px;padding-top:0;padding-bottom:20px;padding-right:0;padding-left:0;" >
                                                        <a class="social-btn" target="_blank" href="#" style="text-decoration:none;" >
                                                            <img class="social-img" alt="facebook icon" src="data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjUxMnB0IiB2aWV3Qm94PSIwIDAgNTEyIDUxMiIgd2lkdGg9IjUxMnB0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Im00ODMuNzM4MjgxIDBoLTQ1NS41Yy0xNS41OTc2NTYuMDA3ODEyNS0yOC4yNDIxODcyNSAxMi42NjAxNTYtMjguMjM4MjgxIDI4LjI2MTcxOXY0NTUuNWMuMDA3ODEyNSAxNS41OTc2NTYgMTIuNjYwMTU2IDI4LjI0MjE4NyAyOC4yNjE3MTkgMjguMjM4MjgxaDQ1NS40NzY1NjJjMTUuNjA1NDY5LjAwMzkwNiAyOC4yNTc4MTMtMTIuNjQ0NTMxIDI4LjI2MTcxOS0yOC4yNSAwLS4wMDM5MDYgMC0uMDA3ODEyIDAtLjAxMTcxOXYtNDU1LjVjLS4wMDc4MTItMTUuNTk3NjU2LTEyLjY2MDE1Ni0yOC4yNDIxODcyNS0yOC4yNjE3MTktMjguMjM4Mjgxem0wIDAiIGZpbGw9IiM0MjY3YjIiLz48cGF0aCBkPSJtMzUzLjUgNTEydi0xOThoNjYuNzVsMTAtNzcuNWgtNzYuNzV2LTQ5LjM1OTM3NWMwLTIyLjM4NjcxOSA2LjIxNDg0NC0zNy42NDA2MjUgMzguMzE2NDA2LTM3LjY0MDYyNWg0MC42ODM1OTR2LTY5LjEyODkwNmMtNy4wNzgxMjUtLjk0MTQwNi0zMS4zNjMyODEtMy4wNDY4NzUtNTkuNjIxMDk0LTMuMDQ2ODc1LTU5IDAtOTkuMzc4OTA2IDM2LTk5LjM3ODkwNiAxMDIuMTQwNjI1djU3LjAzNTE1NmgtNjYuNXY3Ny41aDY2LjV2MTk4em0wIDAiIGZpbGw9IiNmZmYiLz48L3N2Zz4=" style="outline-style:none;-ms-interpolation-mode:bicubic;display:block;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;max-width:32px;max-height:32px;" />
                                                        </a>
                                                    </td>
                                                    <td class="td-social-btn" width="40px" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;width:40px;padding-top:0;padding-bottom:20px;padding-right:0;padding-left:0;" >
                                                        <a class="social-btn" target="_blank" href="#" style="text-decoration:none;" >
                                                            <img class="social-img" alt="instagram icon" src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iaXNvLTg4NTktMSI/Pg0KPCEtLSBHZW5lcmF0b3I6IEFkb2JlIElsbHVzdHJhdG9yIDE2LjAuMCwgU1ZHIEV4cG9ydCBQbHVnLUluIC4gU1ZHIFZlcnNpb246IDYuMDAgQnVpbGQgMCkgIC0tPg0KPCFET0NUWVBFIHN2ZyBQVUJMSUMgIi0vL1czQy8vRFREIFNWRyAxLjEvL0VOIiAiaHR0cDovL3d3dy53My5vcmcvR3JhcGhpY3MvU1ZHLzEuMS9EVEQvc3ZnMTEuZHRkIj4NCjxzdmcgdmVyc2lvbj0iMS4xIiBpZD0iTGF5ZXJfMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB4bWxuczp4bGluaz0iaHR0cDovL3d3dy53My5vcmcvMTk5OS94bGluayIgeD0iMHB4IiB5PSIwcHgiDQoJIHdpZHRoPSIxNjkuMDYzcHgiIGhlaWdodD0iMTY5LjA2M3B4IiB2aWV3Qm94PSIwIDAgMTY5LjA2MyAxNjkuMDYzIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCAxNjkuMDYzIDE2OS4wNjM7Ig0KCSB4bWw6c3BhY2U9InByZXNlcnZlIj4NCjxnPg0KCTxwYXRoIGQ9Ik0xMjIuNDA2LDBINDYuNjU0QzIwLjkyOSwwLDAsMjAuOTMsMCw0Ni42NTV2NzUuNzUyYzAsMjUuNzI2LDIwLjkyOSw0Ni42NTUsNDYuNjU0LDQ2LjY1NWg3NS43NTINCgkJYzI1LjcyNywwLDQ2LjY1Ni0yMC45Myw0Ni42NTYtNDYuNjU1VjQ2LjY1NUMxNjkuMDYzLDIwLjkzLDE0OC4xMzMsMCwxMjIuNDA2LDB6IE0xNTQuMDYzLDEyMi40MDcNCgkJYzAsMTcuNDU1LTE0LjIwMSwzMS42NTUtMzEuNjU2LDMxLjY1NUg0Ni42NTRDMjkuMiwxNTQuMDYzLDE1LDEzOS44NjIsMTUsMTIyLjQwN1Y0Ni42NTVDMTUsMjkuMjAxLDI5LjIsMTUsNDYuNjU0LDE1aDc1Ljc1Mg0KCQljMTcuNDU1LDAsMzEuNjU2LDE0LjIwMSwzMS42NTYsMzEuNjU1VjEyMi40MDd6Ii8+DQoJPHBhdGggZD0iTTg0LjUzMSw0MC45N2MtMjQuMDIxLDAtNDMuNTYzLDE5LjU0Mi00My41NjMsNDMuNTYzYzAsMjQuMDIsMTkuNTQyLDQzLjU2MSw0My41NjMsNDMuNTYxczQzLjU2My0xOS41NDEsNDMuNTYzLTQzLjU2MQ0KCQlDMTI4LjA5NCw2MC41MTIsMTA4LjU1Miw0MC45Nyw4NC41MzEsNDAuOTd6IE04NC41MzEsMTEzLjA5M2MtMTUuNzQ5LDAtMjguNTYzLTEyLjgxMi0yOC41NjMtMjguNTYxDQoJCWMwLTE1Ljc1LDEyLjgxMy0yOC41NjMsMjguNTYzLTI4LjU2M3MyOC41NjMsMTIuODEzLDI4LjU2MywyOC41NjNDMTEzLjA5NCwxMDAuMjgxLDEwMC4yOCwxMTMuMDkzLDg0LjUzMSwxMTMuMDkzeiIvPg0KCTxwYXRoIGQ9Ik0xMjkuOTIxLDI4LjI1MWMtMi44OSwwLTUuNzI5LDEuMTctNy43NywzLjIyYy0yLjA1MSwyLjA0LTMuMjMsNC44OC0zLjIzLDcuNzhjMCwyLjg5MSwxLjE4LDUuNzMsMy4yMyw3Ljc4DQoJCWMyLjA0LDIuMDQsNC44OCwzLjIyLDcuNzcsMy4yMmMyLjksMCw1LjczLTEuMTgsNy43OC0zLjIyYzIuMDUtMi4wNSwzLjIyLTQuODksMy4yMi03Ljc4YzAtMi45LTEuMTctNS43NC0zLjIyLTcuNzgNCgkJQzEzNS42NjEsMjkuNDIxLDEzMi44MjEsMjguMjUxLDEyOS45MjEsMjguMjUxeiIvPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPGc+DQo8L2c+DQo8Zz4NCjwvZz4NCjxnPg0KPC9nPg0KPC9zdmc+DQo=" style="outline-style:none;-ms-interpolation-mode:bicubic;display:block;margin-top:0;margin-bottom:0;margin-right:auto;margin-left:auto;padding-top:0;padding-bottom:0;padding-right:0;padding-left:0;max-width:32px;max-height:32px;" />
                                                        </a>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="td-freepik" align="center" style="margin-top:0;margin-bottom:0;margin-right:0;margin-left:0;font-family:Arial, Helvetica, sans-serif;color:#333333;font-size:10px;line-height:18px;mso-line-height-rule:exactly;font-style:italic;font-weight:normal;letter-spacing:normal;text-align:center;padding-top:20px;padding-bottom:0;padding-right:0;padding-left:0;" >
                                        Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>
    """, subtype='html')

    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                msg.replace_header('To', row['email'])
            except KeyError:
                msg['To'] = row['email']

            mail_obj.send_message(msg)
            time.sleep(61)
