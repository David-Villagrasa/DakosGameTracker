# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 139)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_mainTitle = QtWidgets.QLabel(self.centralwidget)
        self.lbl_mainTitle.setGeometry(QtCore.QRect(10, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_mainTitle.setFont(font)
        self.lbl_mainTitle.setObjectName("lbl_mainTitle")
        self.cbYears = QtWidgets.QComboBox(self.centralwidget)
        self.cbYears.setGeometry(QtCore.QRect(20, 60, 91, 22))
        self.cbYears.setObjectName("cbYears")
        self.cbYears.addItem("")
        self.lbl_titleNumberOf = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titleNumberOf.setGeometry(QtCore.QRect(250, 40, 51, 20))
        self.lbl_titleNumberOf.setObjectName("lbl_titleNumberOf")
        self.lbl_numberOf = QtWidgets.QLabel(self.centralwidget)
        self.lbl_numberOf.setGeometry(QtCore.QRect(320, 40, 61, 21))
        self.lbl_numberOf.setObjectName("lbl_numberOf")
        self.btnOpenYear = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenYear.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.btnOpenYear.setObjectName("btnOpenYear")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 21))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuOnline_Db = QtWidgets.QMenu(self.menubar)
        self.menuOnline_Db.setObjectName("menuOnline_Db")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSet_Folder = QtWidgets.QAction(MainWindow)
        self.actionSet_Folder.setObjectName("actionSet_Folder")
        self.actionLoad_Files = QtWidgets.QAction(MainWindow)
        self.actionLoad_Files.setObjectName("actionLoad_Files")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLogIn = QtWidgets.QAction(MainWindow)
        self.actionLogIn.setObjectName("actionLogIn")
        self.actionLogOut = QtWidgets.QAction(MainWindow)
        self.actionLogOut.setObjectName("actionLogOut")
        self.actionSign_It = QtWidgets.QAction(MainWindow)
        self.actionSign_It.setObjectName("actionSign_It")
        self.actionSave_to_DB = QtWidgets.QAction(MainWindow)
        self.actionSave_to_DB.setObjectName("actionSave_to_DB")
        self.menuOptions.addAction(self.actionSet_Folder)
        self.menuOptions.addAction(self.actionLoad_Files)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionExit)
        self.menuOnline_Db.addAction(self.actionLogIn)
        self.menuOnline_Db.addAction(self.actionLogOut)
        self.menuOnline_Db.addAction(self.actionSign_It)
        self.menuOnline_Db.addSeparator()
        self.menuOnline_Db.addAction(self.actionSave_to_DB)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuOnline_Db.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_mainTitle.setText(_translate("MainWindow", "TotallyGames"))
        self.cbYears.setItemText(0, _translate("MainWindow", "Select year"))
        self.lbl_titleNumberOf.setText(_translate("MainWindow", "Number of files loaded: "))
        self.lbl_numberOf.setText(_translate("MainWindow", "0"))
        self.btnOpenYear.setText(_translate("MainWindow", "Open"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuOnline_Db.setTitle(_translate("MainWindow", "Online Db"))
        self.actionSet_Folder.setText(_translate("MainWindow", "Set Folder"))
        self.actionLoad_Files.setText(_translate("MainWindow", "Load Files"))
        self.actionLoad_Files.setShortcut(_translate("MainWindow", "F5"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLogIn.setText(_translate("MainWindow", "LogIn"))
        self.actionLogOut.setText(_translate("MainWindow", "LogOut"))
        self.actionSign_It.setText(_translate("MainWindow", "Sign In"))
        self.actionSave_to_DB.setText(_translate("MainWindow", "Save to DB"))
