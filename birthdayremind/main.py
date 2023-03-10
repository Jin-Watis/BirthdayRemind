# coding=UTF-8
import datetime
import json
from sys import exit

import pytz
from win10toast import ToastNotifier

import birthdayremind
import change.ChangeMain as Manager


class Start:
    def __init__(self):
        self.toaster = ToastNotifier()
        path = r"datas/data.json"
        self.Lord(path)

        tz = pytz.timezone(r'Asia/Shanghai')
        self.t = datetime.datetime.now(tz)
        self.year = int(self.t.year)
        self.month = int(self.t.month)
        self.day = int(self.t.day)
        self.today = str(self.year) + str(self.month) + str(self.day)
        self.times = '{}-{}-{}'.format(self.year, self.month, self.day)
        self.exact_time = self.t.replace(microsecond=0, tzinfo=None)

        try:
            self.run()
        except Exception as er:
            with open(r'datas/runtime.log', 'a+') as f:
                txt = "{}   error   {}    {}\n".format(self.exact_time, er.__class__.__name__, er)
                f.write(txt)

    def run(self):

        self.toaster.show_toast("BirthdayRemind", "启动成功",
                                icon_path=None, duration=2, threaded=False)
        self.IfAlreadyRun()

        try:
            self.name = self.Date2Name[(self.month, self.day)]
        except KeyError:
            self.name = []
        if self.name:  # list不为空
            self.toaster.show_toast("今天是{}的生日".format("/".join(self.name)), "BirthdayRemind",
                                    icon_path=None, duration=10, threaded=True)
            birthdayremind.SendMessage(self.name, self.times)
        with open(r'datas/runtime.log', 'a+') as f:
            txt = "{}   started   data: {}\n".format(self.exact_time, self.name if self.name else 'nobody')
            f.write(txt)
        exit()

    def IfAlreadyRun(self):

        with open(r"datas/today.txt", "w+") as f:
            td = f.read()
            if td == self.today:
                with open(r'datas/runtime.log', 'a+') as g:
                    txt = "{}   passed\n".format(self.exact_time)
                    g.write(txt)
                exit()
            else:
                f.write(self.today)


    def Lord(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                self.Name2Date = json.load(f)
        except FileNotFoundError:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump({}, f, ensure_ascii=False)
                self.Name2Date = {}
        self.Date2Name = Manager.ChangeData2_Date2Name(self.Name2Date)
