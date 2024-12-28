import random
import string
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import hashlib


class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
        hash = username + password
        hash = hashlib.md5(hash.encode())
        hash = hash.hexdigest()
        self.__password_login_hash = hash
        smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
        smtpObj.starttls()
        smtpObj.login("work_smtp_ofkate@mail.ru", "axH8vCX8ZzPBnqHaHuUF")
        m = f"""Вы успешно зарегистрировались на сайте 'МТУСИ_student'! \n\n {name}, ждем вас на сайте"""
        subject = 'МТУСИ_student'
        msg = MIMEText(m, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        smtpObj.sendmail("work_smtp_ofkate@mail.ru", email, msg.as_string())
        smtpObj.quit()


    def check_password(self, password):
        login = self.username
        hash = login + password
        hash = hashlib.md5(hash.encode())
        hash = hash.hexdigest()
        if hash == self.__password_login_hash:
            return True
        else:
            return False

    def set_password(self, new_password):
        email = self.email
        login = self.username
        hash = login + new_password
        hash = hashlib.md5(hash.encode())
        hash = hash.hexdigest()
        self.__password = new_password
        self.__password_login_hash = hash
        smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
        smtpObj.starttls()
        smtpObj.login("work_smtp_ofkate@mail.ru", "axH8vCX8ZzPBnqHaHuUF")
        user = user[0]
        a = DataBaseManager()
        m = f"""Кто-то сменил пароль в вашем аккаунте! Если это были не Вы, обратиесь в службу поддержки!"""
        subject = 'Изменение пароля МТУСИ_student'
        msg = MIMEText(m, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        smtpObj.sendmail("work_smtp_ofkate@mail.ru", email, msg.as_string())
        smtpObj.quit()
        user.password_login_hash = ash_2

Vasya = UserAccount("Vasya_Petrov", "vasyundra_2006@gamil.com", "123456")
print(Vasya.check_password('123456'))
Vasya.set_password("qwerty")
print(Vasya.check_password('123456'))
print(Vasya.check_password('qwerty'))
print(Vasya.__password)
