# coding=UTF-8
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import json


class SendMessage:
    def __init__(self, name, times):
        self.name = name
        self.times = times
        path = "datas\\emaildata.json"
        with open(path, 'r') as f:
            row = json.load(f)
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
