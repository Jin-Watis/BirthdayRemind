# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BirthdayManager(object):
    def setupUi(self, BirthdayManager):
        BirthdayManager.setObjectName("BirthdayManager")
        BirthdayManager.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(BirthdayManager.sizePolicy().hasHeightForWidth())
        BirthdayManager.setSizePolicy(sizePolicy)
        BirthdayManager.setMinimumSize(QtCore.QSize(600, 400))
        BirthdayManager.setMaximumSize(QtCore.QSize(640, 410))
        self.centralwidget = QtWidgets.QWidget(BirthdayManager)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777210, 16777210))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SHIn = QtWidgets.QHBoxLayout()
        self.SHIn.setContentsMargins(40, -1, 77, -1)
        self.SHIn.setObjectName("SHIn")
        self.NAME = QtWidgets.QLabel(self.tab_2)
        self.NAME.setMinimumSize(QtCore.QSize(0, 0))
        self.NAME.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.NAME.setFont(font)
        self.NAME.setMouseTracking(False)
        self.NAME.setAlignment(QtCore.Qt.AlignCenter)
        self.NAME.setObjectName("NAME")
        self.SHIn.addWidget(self.NAME)
        self.INPUT = QtWidgets.QLineEdit(self.tab_2)
        self.INPUT.setMinimumSize(QtCore.QSize(0, 50))
        self.INPUT.setMaximumSize(QtCore.QSize(255, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.INPUT.setFont(font)
        self.INPUT.setObjectName("INPUT")
        self.SHIn.addWidget(self.INPUT)
        self.SEARCH = QtWidgets.QPushButton(self.tab_2)
        self.SEARCH.setObjectName("SEARCH")
        self.SHIn.addWidget(self.SEARCH)
        self.verticalLayout_3.addLayout(self.SHIn)
        self.Result = QtWidgets.QGroupBox(self.tab_2)
        self.Result.setMaximumSize(QtCore.QSize(1000000, 16777215))
        self.Result.setObjectName("Result")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.Result)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.RESULT = QtWidgets.QTableWidget(self.Result)
        self.RESULT.setMinimumSize(QtCore.QSize(400, 100))
        self.RESULT.setMaximumSize(QtCore.QSize(1000, 16777215))
        self.RESULT.setObjectName("RESULT")
        self.RESULT.setColumnCount(3)
        self.RESULT.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.RESULT.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RESULT.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.RESULT.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.RESULT.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_10.addWidget(self.RESULT)
        self.verticalLayout_3.addWidget(self.Result, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_9.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(10, 20, 10, 20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MonthFrme = QtWidgets.QHBoxLayout()
        self.MonthFrme.setContentsMargins(10, -1, 30, -1)
        self.MonthFrme.setObjectName("MonthFrme")
        self.MSh = QtWidgets.QLabel(self.tab_1)
        self.MSh.setMinimumSize(QtCore.QSize(50, 0))
        self.MSh.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.MSh.setFont(font)
        self.MSh.setMouseTracking(False)
        self.MSh.setAlignment(QtCore.Qt.AlignCenter)
        self.MSh.setObjectName("MSh")
        self.MonthFrme.addWidget(self.MSh)
        self.MIn = QtWidgets.QLineEdit(self.tab_1)
        self.MIn.setMinimumSize(QtCore.QSize(0, 50))
        self.MIn.setMaximumSize(QtCore.QSize(1000000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MIn.setFont(font)
        self.MIn.setObjectName("MIn")
        self.MonthFrme.addWidget(self.MIn)
        self.verticalLayout_2.addLayout(self.MonthFrme)
        self.DayFrme = QtWidgets.QHBoxLayout()
        self.DayFrme.setContentsMargins(10, -1, 30, -1)
        self.DayFrme.setObjectName("DayFrme")
        self.DSh = QtWidgets.QLabel(self.tab_1)
        self.DSh.setMinimumSize(QtCore.QSize(0, 0))
        self.DSh.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.DSh.setFont(font)
        self.DSh.setMouseTracking(False)
        self.DSh.setAlignment(QtCore.Qt.AlignCenter)
        self.DSh.setObjectName("DSh")
        self.DayFrme.addWidget(self.DSh)
        self.DIn = QtWidgets.QLineEdit(self.tab_1)
        self.DIn.setMinimumSize(QtCore.QSize(0, 50))
        self.DIn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DIn.setFont(font)
        self.DIn.setObjectName("DIn")
        self.DayFrme.addWidget(self.DIn)
        self.verticalLayout_2.addLayout(self.DayFrme)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.frame = QtWidgets.QFrame(self.tab_1)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(21, 11, 258, 226))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SEARCHBYDATE = QtWidgets.QPushButton(self.layoutWidget)
        self.SEARCHBYDATE.setMinimumSize(QtCore.QSize(70, 0))
        self.SEARCHBYDATE.setObjectName("SEARCHBYDATE")
        self.horizontalLayout_2.addWidget(self.SEARCHBYDATE)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.NAME_SHOW = QtWidgets.QTableWidget(self.layoutWidget)
        self.NAME_SHOW.setObjectName("NAME_SHOW")
        self.NAME_SHOW.setColumnCount(1)
        self.NAME_SHOW.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.NAME_SHOW.setHorizontalHeaderItem(0, item)
        self.verticalLayout_4.addWidget(self.NAME_SHOW)
        self.horizontalLayout_6.addWidget(self.frame)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_1, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.AutoStart = QtWidgets.QRadioButton(self.centralwidget)
        self.AutoStart.setObjectName("AutoStart")
        self.horizontalLayout_3.addWidget(self.AutoStart)
        self.ShowAll = QtWidgets.QPushButton(self.centralwidget)
        self.ShowAll.setObjectName("ShowAll")
        self.horizontalLayout_3.addWidget(self.ShowAll)
        self.SAVE = QtWidgets.QPushButton(self.centralwidget)
        self.SAVE.setObjectName("SAVE")
        self.horizontalLayout_3.addWidget(self.SAVE)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        BirthdayManager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(BirthdayManager)
        self.statusbar.setObjectName("statusbar")
        BirthdayManager.setStatusBar(self.statusbar)

        self.retranslateUi(BirthdayManager)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(BirthdayManager)

    def retranslateUi(self, BirthdayManager):
        _translate = QtCore.QCoreApplication.translate
        BirthdayManager.setWindowTitle(_translate("BirthdayManager", "BirathdayManager"))
        self.NAME.setText(_translate("BirthdayManager", "name:"))
        self.SEARCH.setText(_translate("BirthdayManager", "Search"))
        self.Result.setTitle(_translate("BirthdayManager", "结果"))
        item = self.RESULT.horizontalHeaderItem(0)
        item.setText(_translate("BirthdayManager", "name"))
        item = self.RESULT.horizontalHeaderItem(1)
        item.setText(_translate("BirthdayManager", "month"))
        item = self.RESULT.horizontalHeaderItem(2)
        item.setText(_translate("BirthdayManager", "day"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("BirthdayManager", "查找"))
        self.MSh.setText(_translate("BirthdayManager", "月份:"))
        self.DSh.setText(_translate("BirthdayManager", "日期:"))
        self.SEARCHBYDATE.setText(_translate("BirthdayManager", "Search"))
        item = self.NAME_SHOW.horizontalHeaderItem(0)
        item.setText(_translate("BirthdayManager", "name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("BirthdayManager", "编辑"))
        self.AutoStart.setText(_translate("BirthdayManager", "开机自启动"))
        self.ShowAll.setText(_translate("BirthdayManager", "All"))
        self.SAVE.setText(_translate("BirthdayManager", "保存"))
