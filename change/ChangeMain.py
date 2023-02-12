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
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox
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

        self.path = r"datas/data.json"
        self.Lord()

        self.ui.NAME_SHOW.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.RESULT.setEditTriggers(PyQt5.QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.RESULT.setColumnCount(3)
        self.ui.RESULT.setRowCount(0)
        self.inserttimes = 0
        self.just_search = 0
        self.have_Changed_datas = []



        # 绑定槽函数
        self.ui.SEARCH.clicked.connect(lambda: self.SearchByName())
        self.ui.SEARCHBYDATE.clicked.connect(lambda: self.SearchByDate())
        self.ui.ShowAll.clicked.connect(lambda: self.ShowAll())
        self.ui.SAVE.clicked.connect(lambda: self.Save())
        self.ui.AutoStart.toggled.connect(lambda: self.AutoStart())
        self.ui.NAME_SHOW.itemChanged.connect(self.HasChanged)

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

    def SearchByDate(self):
        month = int(self.ui.MIn.text())
        day = int(self.ui.DIn.text())
        date_couple = (month, day)
        self.ui.NAME_SHOW.setRowCount(0)
        self.ui.NAME_SHOW.clearContents()
        num = 0
        try:
            names = self.Date2Name[date_couple]
            self.just_search += len(names)
            for name in names:
                self.ui.NAME_SHOW.insertRow(int(self.ui.NAME_SHOW.rowCount()))
                self.ui.NAME_SHOW.setItem(num, 0, PyQt5.QtWidgets.QTableWidgetItem(str(name)))
                num += 1
            self.ui.NAME_SHOW.insertRow(int(self.ui.NAME_SHOW.rowCount()))
        except KeyError:
            self.just_search += 1
            self.ui.NAME_SHOW.insertRow(int(self.ui.NAME_SHOW.rowCount()))
            self.ui.NAME_SHOW.setItem(num, 0,
                                      PyQt5.QtWidgets.QTableWidgetItem(str('None')))
        self.ui.NAME_SHOW.viewport().update()
        self.basic_data = [self.ui.NAME_SHOW.item(i, 0).text() for i in range(self.ui.NAME_SHOW.rowCount() - 1)]
        # 如果值为None  那么self.basic_data是空列表
        # print(self.basic_data)

    def HasChanged(self, item: QTableWidgetItem = None) -> None:
        if self.just_search != 0:
            self.just_search -= 1
            return

        try:
            if item is None or self.basic_data[item.row()] == item.text():
                return
        except IndexError:  # self.basic_data是空列表
            if item.text() is None:
                return

        month = int(self.ui.MIn.text())
        day = int(self.ui.DIn.text())
        if item.text() != '':
            # 不为删除
            if item.row() + 1 > len(self.basic_data):
                config: str = 'add'
            else:
                # config是过去的名字
                config: str = self.basic_data[item.row()]

            changed_data = {
                'time': (month, day),
                'data': {'name': item.text(), 'config': config}
            }
        else:
            changed_data = {
                'time': (month, day),
                'data': {'name': self.basic_data[item.row()], 'config': 'del'}
            }
        self.have_Changed_datas.append(changed_data)

    def ShowAll(self):
        with open('datas/all.txt', 'w') as output:
            for date in self.Date2Name:
                names = ", ".join(self.Date2Name[date])
                output.write("{}\t{}\t{}\n".format(date[0], date[1], names))

        def func():
            os.system("datas\\all.txt")

        fileopen = multiprocessing.Process(func())
        fileopen.start()

    def Save(self):
        if not self.have_Changed_datas:
            return
        st = '是否保存数据: \n'
        for s in self.have_Changed_datas:
            st += str(s)+'\n'
        MakeSure = QMessageBox.question(self, '保存', st, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if MakeSure == QMessageBox.No:
            return

        self.LordChangedData()
        self.Name2Date = {k: v for k, v in sorted(self.Name2Date.items(),
                                                  key=lambda item: (item[1][0]['month'], item[1][0]['day'])
                                                  )}
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.Name2Date, f, ensure_ascii=False)
        self.have_Changed_datas = []
        self.Make_Date2Name()

    def LordChangedData(self):
        for people in self.have_Changed_datas:
            date = {
                "month": int(people['time'][0]),
                "day": int(people['time'][1])
            }
            data = people['data']
            name, config = data['name'], data['config']
            if config == 'del':
                self.Name2Date[name].remove(date)
                if not self.Name2Date[name]:
                    del self.Name2Date[name]
                return

            elif config != 'add':
                self.Name2Date[config].remove(date)
                if not self.Name2Date[config]:
                    del self.Name2Date[config]

            try:
                self.Name2Date[name].append(date)
            except KeyError:
                self.Name2Date[name] = [date]

    def Lord(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            self.Name2Date: dict = json.load(f)
        self.Make_Date2Name()

    def Make_Date2Name(self):
        self.Date2Name = {}
        for name in self.Name2Date:
            dateList = self.Name2Date[name]
            for date in dateList:
                date = (date['month'], date['day'])
                try:
                    self.Date2Name[date].append(name)
                except KeyError:
                    self.Date2Name[date] = [name]

    def AutoStart(self):
        # TODO 想办法完善它
        ...


def run():
    TodayData = GetToday()
    myapp = QApplication(sys.argv)
    myDlg = Main()
    myDlg.show()
    sys.exit(myapp.exec_())
