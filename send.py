# -*- couding: UTF-8 -*-
# -*- couding: gbk -*-

def ListToStr(nums: list)->str:
    Str =  ""
    m = 1
    for i in nums:
        if m == 1:
            Str += str(i)
            m += 1
        else:
            Str += ("/" + str(i))
    return Str

def Send(name,times):
    import smtplib
    from email.mime.text import MIMEText
    import time 
    from email.header import Header
    

    today = times
    txt= "今天是{}是 {} 的生日".format(today,ListToStr(name))

    # 第三方 SMTP 服务
    mail_host="smtp.163.com"  #设置服务器
    mail_user="jin"    #用户名
    mail_pass="EQDLSRUEZKSSEECM"   #口令 
 
 
    sender = 'c1193302518@163.com'
    receivers = ['c1193302518@outlook.com','c1193302518@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
    message = MIMEText('生日提醒' + today, 'plain', 'utf-8')
    message['From'] = Header("jin", 'utf-8')
    message['To'] =  Header("提醒", 'utf-8')
 
    subject = txt
    message['Subject'] = Header(subject, 'utf-8')
 
 

    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(sender,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    #print("邮件发送成功")
    from sys import exit
    exit()
