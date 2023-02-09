# coding=UTF-8

import json
import multiprocessing
import sys
import os
import PyQt5
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

        self.ui.RESULT.setEditTriggers(PyQt5.QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.RESULT.setColumnCount(3)
        self.ui.RESULT.setRowCount(0)
        self.inserttimes = 0

        # self.ui.AutoStart.toggled.connect(lambda: self.f())

        # 查找输入函数
        self.ui.SEARCH.clicked.connect(lambda: self.SearchByName())
        self.ui.ShowAll.clicked.connect(lambda: self.ShowAll())

    def SearchByName(self):
        name = self.ui.INPUT.text()
        try:
            nameList = self.Name2Date[name]
            for date in nameList:
                self.ui.RESULT.insertRow(int(self.ui.RESULT.rowCount()))
                self.ui.RESULT.setItem(self.inserttimes, 0,
                                       PyQt5.QtWidgets.QTableWidgetItem(str(name)))
                self.ui.RESULT.setItem(self.inserttimes, 1,
                                       PyQt5.QtWidgets.QTableWidgetItem(str(date['month'])))
                self.ui.RESULT.setItem(self.inserttimes, 2,
                                       PyQt5.QtWidgets.QTableWidgetItem(str(date['day'])))
                self.inserttimes += 1
        except KeyError:
            self.ui.RESULT.insertRow(int(self.ui.RESULT.rowCount()))
            self.ui.RESULT.setItem(self.inserttimes, 0,
                                   PyQt5.QtWidgets.QTableWidgetItem(str(name)))
            self.ui.RESULT.setItem(self.inserttimes, 1,
                                   PyQt5.QtWidgets.QTableWidgetItem(str("Nobody Here")))
            self.inserttimes += 1
        self.ui.RESULT.viewport().update()

    def ShowAll(self):
        with open('datas/all.txt', 'w') as output:
            for date in self.Date2Name:
                names = ", ".join(self.Date2Name[date])
                output.write("{}\t{}\t{}\n".format(date[0], date[1], names))

        def func():
            os.system("datas\\all.txt")

        fileopen = multiprocessing.Process(func())
        fileopen.start()

    def f(self):
        print("a")

    def Lord(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            self.Name2Date = json.load(f)
        self.Date2Name = {}
        for name in self.Name2Date:
            dateList = self.Name2Date[name]
            for date in dateList:
                date = (date['month'], date['day'])
                try:
                    self.Date2Name[date].append(name)
                except KeyError:
                    self.Date2Name[date] = [name]


def run():
    TodayData = GetToday()
    myapp = QApplication(sys.argv)
    myDlg = Main()
    myDlg.show()
    sys.exit(myapp.exec_())
