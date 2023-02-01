# -*- couding: UTF-8 -*-
# -*- couding: gbk -*-

"""
改完源码之后记得更改pyw文件
开机自启动导向的是pyw
"""

import pytz
import datetime
import numpy as np
from send import Send, ListToStr
from sys import exit

from win10toast import ToastNotifier

toaster = ToastNotifier()

# Lode
data = 0
data = np.load("data.npy", allow_pickle=True).item()

tz = pytz.timezone('Asia/Shanghai')
t = datetime.datetime.now(tz)
# print(t.month,t.day)
year = int(t.year)
month = int(t.month)
day = int(t.day)
today = str(year) + str(month) + str(day)
times = '{}-{}-{}'.format(year, month, day)

toaster.show_toast("BirthdayRemind", "启动成功",
				   icon_path=None, duration=2, threaded=False)

f = open("today.txt", "r")
td = f.read()
f.close()

if td == today:
	exit()
else:
	w = open("today.txt", "w")
	w.write(today)
	w.close()

##text:
# month = 2
# day = 19

name = data[month][day]

if name:  # list不为空
	toaster.show_toast("今天是{}的生日".format(ListToStr(name)), "BirthdayRemind",
					   icon_path=None, duration=10, threaded=True)
	# tk.messagebox.showinfo(title='OK', message='某人的生日!')
	# print(name,today,times)
	Send(name, times)
else:  # list为空
	exit()
