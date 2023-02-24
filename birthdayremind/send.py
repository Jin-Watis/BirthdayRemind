# coding=UTF-8
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import json


class SendMessage:
    def __init__(self, name, times):
        self.name = name
        self.times = times
        path = r"datas/emaildata.json"
        try:
            with open(path, 'r') as f:
                row = json.load(f)
        except FileNotFoundError:
            self.NoFile(path)
        self.host = row['host']
        self.user = row['user']
        self.password = row['password']
        self.sender = row['sender']
        self.addresses = row['addresses']

        self.send()

    def send(self):
        today = self.times
        txt = "今天是{}是 {} 的生日".format(today, "/".join(self.name))

        message = MIMEText('生日提醒' + today, 'plain', 'utf-8')
        message['From'] = Header("jin", 'utf-8')
        message['To'] = Header("提醒", 'utf-8')

        subject = txt
        message['Subject'] = Header(subject, 'utf-8')

        smtpObj = smtplib.SMTP()
        smtpObj.connect(self.host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(self.sender, self.password)
        smtpObj.sendmail(self.sender, self.addresses, message.as_string())

    def NoFile(self, path):
        j = {
            "host": "smtp.163.com",
            "user": "username，不是很重要",
            "password": "STMP 密码",
            "sender": "发件箱地址",
            "addresses": [
                "收件箱地址",
                "建议给发件箱自己发送一条，这样不容易被屏蔽"
            ]
        }
        with open(path, 'w+', encoding='utf-8') as f:
            json.dump(j, f, ensure_ascii=False)



