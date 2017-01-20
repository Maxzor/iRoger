# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupbox.ui'
#
# Created: Sat Dec 31 06:03:56 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GroupBox(object):
    def setupUi(self, GroupBox):
        GroupBox.setObjectName(_fromUtf8("GroupBox"))
        GroupBox.setGeometry(100, 100, 340, 292)
        GroupBox.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        GroupBox.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTrailing|\
                              QtCore.Qt.AlignVCenter)
        self.tabWidget = QtGui.QTabWidget(GroupBox)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 321, 261))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.spinBox = QtGui.QSpinBox(self.tab_1)
        self.spinBox.setGeometry(QtCore.QRect(120, 20, 61, 51))
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(30)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.pushButton = QtGui.QPushButton(self.tab_1)
        self.pushButton.setGeometry(QtCore.QRect(220, 20, 81, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(self.tab_1)
        self.label_2.setGeometry(QtCore.QRect(190, 30, 20, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textBrowser = QtGui.QTextBrowser(self.tab_1)
        self.textBrowser.setGeometry(QtCore.QRect(140, 90, 121, 121))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_3 = QtGui.QLabel(self.tab_1)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 121, 51))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.tab_1)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tableView_2 = QtGui.QTableView(self.tab_2)
        self.tableView_2.setGeometry(QtCore.QRect(50, 20, 221, 121))
        self.tableView_2.setShowGrid(False)
        self.tableView_2.setObjectName(_fromUtf8("tableView_2"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, -10, 91, 41))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 150, 91, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 150, 91, 61))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 10, 101, 31))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(40, 40, 281, 181))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(GroupBox)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GroupBox)

    def retranslateUi(self, GroupBox):
        GroupBox.setWindowTitle(_translate("GroupBox", "iRoger", None))
        GroupBox.setTitle(_translate("GroupBox", "iRoger", None))
        self.pushButton.setText(_translate("GroupBox", "Go", None))
        self.label_2.setText(_translate("GroupBox", "s", None))
        self.label_3.setText(_translate("GroupBox", "Historique :", None))
        self.label_5.setText(_translate("GroupBox", "Distribuer :", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("GroupBox", "Immédiat", None))
        self.label_4.setText(_translate("GroupBox", "Programmé :", None))
        self.pushButton_2.setText(_translate("GroupBox", "Ajouter", None))
        self.pushButton_3.setText(_translate("GroupBox", "Supprimer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("GroupBox", "Différé", None))
        self.pushButton_4.setText(_translate("GroupBox", "Actualiser", None))
        self.label.setText(_translate("GroupBox", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("GroupBox", "Photo", None))

