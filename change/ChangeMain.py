# coding=UTF-8

import json
import sys
from change import Window
import datetime
import pytz
import calendar
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIntValidator


class GetToday:
    def __init__(self):
        tz = pytz.timezone('Asia/Shanghai')
        t = datetime.datetime.now(tz)
        # print(t.month,t.day)
        self.year = int(t.year)
        self.month = int(t.month)
        self.day = int(t.day)


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Window.Ui_MainWindow()
        self.ui.setupUi(self)
        path = r"datas/data.json"
        self.Lord(path)

        # self.ui.AutoStart.toggled.connect(lambda: self.f())

        # 查找输入函数
        self.ui.INPUT.editingFinished.connect(lambda: self.SearchByName())

    def SearchByName(self):
        name = self.ui.INPUT.text()
        # TODO 维护name的唯一性
        try:
            date = self.Tdata[name]
            print(date)
            return date
        except KeyError:
            print("NoBody Here")
            return None

    def f(self):
        print("a")

    def Lord(self, path):
        with open(path, 'r', encoding='gbk') as f:
            self.Tdata = json.load(f)
        self.data = {}
        odate = None
        for name in self.Tdata:
            date = self.Tdata[name]
            date = (date['month'], date['day'])
            if odate == date:
                self.data[date].append(name)
                continue
            else:
                odate = date
            self.data[date] = [name]


def run():
    TodayData = GetToday()
    myapp = QApplication(sys.argv)
    myDlg = Main()
    myDlg.show()
    sys.exit(myapp.exec_())


