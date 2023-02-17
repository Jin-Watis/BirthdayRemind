# coding=UTF-8

import json
import multiprocessing
import os
import subprocess
import sys
import winreg

import PyQt5
import setproctitle
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QMessageBox, QCompleter

from change import Window


class ChangedData:
    def __init__(self, date=(0, 0), name='', config='', index=0):
        self.date = date
        self.name = name
        self.config = config
        self.index = index
        self.all = {
            'time': self.date,
            'data': {'name': self.name, 'config': self.config},
            'index': self.index,
        }

    def __str__(self) -> str:
        return str(self.all)

    def GetIndex(self) -> tuple:
        t = (self.date[0], self.date[1], self.index)
        return t


class History:
    def __init__(self):
        self.members = []
        self.map = {}

    def __iter__(self):
        self.k = 0
        return self

    def __next__(self):
        if self.k < len(self.members):
            a = self.members[self.k]
            self.k += 1
            return a
        else:
            raise StopIteration

    def __getitem__(self, key):
        return self.members[self.map[key]]

    def __setitem__(self, key, value):
        self.members.pop(self.map[key])
        self.members.append(value)
        self.map[key] = self.members.index(value)

    def In(self, item):
        return item in self.members

    def IsNone(self):
        return not bool(self.members)

    def append(self, member: ChangedData):
        self.members.append(member)
        self.map[member.GetIndex()] = self.members.index(member)

    def showInfo(self):
        show = []
        for m in self.members:
            month, day = m.date[0], m.date[1]
            name = m.name
            config = m.config
            if config == 'add' or config == 'del':
                t = "{}月{}日, {}, {}".format(month, day, name, config)
            else:
                t = "{}月{}日, {}, 修改_{} ".format(month, day, name, config)
            show.append(t)
        return show


class Main(QMainWindow):
    def __init__(self, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = Window.Ui_BirthdayManager()
        self.ui.setupUi(self)

        self.path = r"datas/data.json"
        self.Lord()

        self.ui.NAME_SHOW.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.RESULT.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.RESULT.setEditTriggers(PyQt5.QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.RESULT.setColumnCount(3)
        self.ui.RESULT.setRowCount(0)
        self.ui.DIn.setValidator(QIntValidator())   # 只允许整数输入
        self.ui.MIn.setValidator(QIntValidator())
        self.insert_times = 0
        self.just_searched = 0
        self.have_Changed_datas = History()
        self.AutoCompletionForNameSearch()
        self.LordAutoStart()

        # 绑定槽函数
        self.ui.SEARCH.clicked.connect(lambda: self.SearchByName())
        self.ui.SEARCHBYDATE.clicked.connect(lambda: self.SearchByDate())
        self.ui.ShowAll.clicked.connect(lambda: self.ShowAll())
        self.ui.SAVE.clicked.connect(lambda: self.Save())
        self.ui.AutoStart.toggled.connect(lambda: self.AutoStart())
        self.ui.NAME_SHOW.itemChanged.connect(self.HasChanged)

    def SearchByName(self):
        name = self.ui.INPUT.text()
        if not name:
            QMessageBox.information(self, '一般错误', '请输入数据', QMessageBox.Ok, QMessageBox.Ok)
            return
        try:
            nameList = self.Name2Date[name]
            for date in nameList:
                self.ui.RESULT.insertRow(int(self.ui.RESULT.rowCount()))
                self.ui.RESULT.setItem(self.insert_times, 0,
                                       PyQt5.QtWidgets.QTableWidgetItem(str(name)))
                self.ui.RESULT.setItem(self.insert_times, 1,
                                       PyQt5.QtWidgets.QTableWidgetItem(str(date['month'])))
                self.ui.RESULT.setItem(self.insert_times, 2,
                                       PyQt5.QtWidgets.QTableWidgetItem(str(date['day'])))
                self.insert_times += 1
        except KeyError:
            self.ui.RESULT.insertRow(int(self.ui.RESULT.rowCount()))
            self.ui.RESULT.setItem(self.insert_times, 0,
                                   PyQt5.QtWidgets.QTableWidgetItem(str(name)))
            self.ui.RESULT.setItem(self.insert_times, 1,
                                   PyQt5.QtWidgets.QTableWidgetItem(str("Nobody Here")))
            self.insert_times += 1
        self.ui.RESULT.viewport().update()

    def SearchByDate(self):
        if (not self.ui.MIn.text()) or (not self.ui.DIn.text()):
            QMessageBox.information(self, '一般错误', '请输入数据', QMessageBox.Ok, QMessageBox.Ok)
            return
        try:
            month = int(self.ui.MIn.text())
            day = int(self.ui.DIn.text())
        except ValueError:
            QMessageBox.critical(self, '操作失败', '输入值异常', QMessageBox.Yes)
            return
        date_couple = (month, day)
        self.ui.NAME_SHOW.setRowCount(0)
        self.ui.NAME_SHOW.clearContents()
        _translate = QtCore.QCoreApplication.translate
        item = self.ui.NAME_SHOW.horizontalHeaderItem(0)
        item.setText(_translate("BirthdayManager", "name_{}.{}".format(month, day)))
        num = 0
        try:
            names = self.Date2Name[date_couple]
            self.just_searched += len(names)
            for name in names:
                self.ui.NAME_SHOW.insertRow(int(self.ui.NAME_SHOW.rowCount()))
                self.ui.NAME_SHOW.setItem(num, 0, PyQt5.QtWidgets.QTableWidgetItem(str(name)))
                num += 1
            self.ui.NAME_SHOW.insertRow(int(self.ui.NAME_SHOW.rowCount()))
        except KeyError:
            self.just_searched += 1
            self.ui.NAME_SHOW.insertRow(int(self.ui.NAME_SHOW.rowCount()))
            self.ui.NAME_SHOW.setItem(num, 0,
                                      PyQt5.QtWidgets.QTableWidgetItem(str('None')))
        self.ui.NAME_SHOW.viewport().update()
        self.basic_data = [self.ui.NAME_SHOW.item(i, 0).text() for i in range(self.ui.NAME_SHOW.rowCount() - 1)]

    def HasChanged(self, item: QTableWidgetItem = None) -> None:
        if self.just_searched != 0:
            self.just_searched -= 1
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
            name = item.text()
            config = config
        else:
            name = self.basic_data[item.row()]
            config = 'del'
        changed_data = ChangedData(date=(month, day), name=name, config=config, index=item.row())

        if changed_data.GetIndex() in self.have_Changed_datas.map.keys():
            self.have_Changed_datas[changed_data.GetIndex()] = changed_data
        else:
            self.have_Changed_datas.append(changed_data)

    def ShowAll(self):
        with open('datas/all.txt', 'w') as output:
            for date in self.Date2Name:
                names = ", ".join(self.Date2Name[date])
                output.write("{}\t{}\t{}\n".format(date[0], date[1], names))

        def func():
            subprocess.run("datas\\all.txt", shell=True)

        fileopen = multiprocessing.Process(func())
        fileopen.start()

    def Save(self):
        if self.have_Changed_datas.IsNone():
            QMessageBox.information(self, 'Manager', '无更改', QMessageBox.Yes)
        start_msg = '是否保存数据: \n'
        st = start_msg
        for s in self.have_Changed_datas.showInfo():
            st += str(s) + '\n'
        MakeSure = QMessageBox.question(self, '保存', st, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if MakeSure == QMessageBox.No:
            return
        """
        开始保存
        """
        self.LordChangedData()
        self.Name2Date = {k: v for k, v in sorted(self.Name2Date.items(),
                                                  key=lambda item: (item[1][0]['month'], item[1][0]['day']))}
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.Name2Date, f, ensure_ascii=False)
        QMessageBox.information(self, '保存成功', st[len(start_msg):], QMessageBox.Ok, QMessageBox.Ok)
        self.have_Changed_datas.__init__()
        self.AutoCompletionForNameSearch()
        self.Make_Date2Name()
        self.SearchByDate()

    def LordChangedData(self):
        for people in self.have_Changed_datas:
            date = {
                "month": int(people.date[0]),
                "day": int(people.date[1])
            }
            name, config = people.name, people.config
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

    def LordAutoStart(self):
        def get_path(name):
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                 r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
            return winreg.QueryValueEx(key, name)[0]

        self.start_path = get_path("Startup")
        self.start_files = os.listdir(self.start_path)
        self.lnk_filename = 'BirthRemind.lnk'
        self.ui.AutoStart.setChecked(self.lnk_filename in self.start_files)

    def AutoStart(self):
        config = self.ui.AutoStart.isChecked()
        workspace = os.path.abspath('.')
        comm1 = "cd /d \"{}\"".format(self.start_path)
        if config:
            to = workspace + r'\ink\BirthRemind.lnk'
            comm2 = 'copy {} {}'.format(to, r".\\")
            com = "{} && {}".format(comm1, comm2)
            subprocess.run(com, shell=True)
            self.start_files = os.listdir(self.start_path)
            if "BirthRemind.lnk" in self.start_files:
                QMessageBox.information(self, '添加成功', '添加快捷方式到启动目录:\n {}'.format(self.start_path),
                                        QMessageBox.Ok, QMessageBox.Ok)
                return
        else:
            comm2 = 'del {}'.format('BirthRemind.lnk')
            com = "{} && {}".format(comm1, comm2)
            subprocess.run(com, shell=True)
            self.start_files = os.listdir(self.start_path)
            if "BirthRemind.lnk" not in self.start_files:
                QMessageBox.information(self, '删除成功', '以删除快捷方式从启动目录:\n {}'.format(self.start_path),
                                        QMessageBox.Ok, QMessageBox.Ok)
                return
        QMessageBox.critical(self, '操作失败', com, QMessageBox.Yes)

    def AutoCompletionForNameSearch(self):
        names_list = [name for name in self.Name2Date]
        self.completer = QCompleter(names_list)
        self.completer.setFilterMode(Qt.MatchContains)
        self.completer.setCompletionMode(QCompleter.PopupCompletion)
        self.completer.setModelSorting(QCompleter.CaseSensitivelySortedModel)
        self.completer.modelSorting()
        self.ui.INPUT.setCompleter(self.completer)

    def keyPressEvent(self, event):
        key = event.key()
        tab_name = self.ui.tabWidget.tabText(self.ui.tabWidget.currentIndex())
        if key == QtCore.Qt.Key_Enter or key == Qt.Key_Return:
            if tab_name == '查找':
                self.SearchByName()
            if tab_name == '编辑':
                self.SearchByDate()


def run():
    setproctitle.setproctitle("BirthdayManager")
    myapp = QApplication(sys.argv)
    myDlg = Main()
    myDlg.show()
    sys.exit(myapp.exec_())
