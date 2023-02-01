# coding=UTF-8

from tkinter import messagebox
import pytz
import datetime
import numpy as np
import birthdayremind
from sys import exit
from win10toast import ToastNotifier


class Start:
    def __init__(self):
        self.toaster = ToastNotifier()
        self.data = np.load(r'datas/data.npy', allow_pickle=True).item()

        tz = pytz.timezone(r'Asia/Shanghai')
        self.t = datetime.datetime.now(tz)
        self.year = int(self.t.year)
        self.month = int(self.t.month)
        self.day = int(self.t.day)
        self.today = str(self.year) + str(self.month) + str(self.day)
        self.times = '{}-{}-{}'.format(self.year, self.month, self.day)

        self.run()

    def run(self):

        self.toaster.show_toast("BirthdayRemind", "启动成功",
                                icon_path=None, duration=2, threaded=False)

        with open(r"datas/today.txt", "r") as f:
            td = f.read()

        if td == self.today:
            exit()
        else:
            with open(r"datas/today.txt", "w") as f:
                f.write(self.today)

        """
        text:
        """
        # self.month = 2
        # self.day = 19

        self.name = self.data[self.month][self.day]

        if self.name:  # list不为空
            self.toaster.show_toast("今天是{}的生日".format("/".join(self.name)), "BirthdayRemind",
                                    icon_path=None, duration=10, threaded=True)
            # messagebox.showinfo(title='OK', message='某人的生日!')
            birthdayremind.SendMessage(self.name, self.times)
        exit()
