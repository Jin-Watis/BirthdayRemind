import sys
from change import ChangeWindow
import datetime
import pytz
import calendar
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np


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
        self.ui = ChangeWindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.DayData = [None, None]

        self.ui.Month.addItems([str(x) for x in range(1, 13)])

    def ChangeDayNumber(self):
        self.ui.Day.clear()
        self.ChooseMonth = int(self.ui.Month.currentText())
        self.MaxDay = calendar.monthrange(TodayData.year, self.ChooseMonth)[1]
        self.ui.Day.addItems([str(x) for x in range(1, self.MaxDay + 1)])
        self.UpData_DayData()

    def UpData_DayData(self):
        self.m = int(self.ui.Month.currentText())
        self.d = int(self.ui.Day.currentText())
        self.DayData = [m, d]

    def Find(self):
        old_data = Data[self.m][self.d]
        self.ui.infoWindow.setPlaceholderText(_translate("MainWindow", str(old_data)))

    def Add(self):
        ...

    def All(self):
        ...

    def Back(self):
        ...


class Datas():
    def __init__(self):
        ...

    def Save(self, data, file):
        dictionary = data
        np.save(file, dictionary)


if __name__ == '__main__':
    TodayData = GetToday()
    Data = np.load("../datas/data.npy", allow_pickle=True).item()

    myapp = QApplication(sys.argv)
    myDlg = Main()
    myDlg.show()
    sys.exit(myapp.exec_())
