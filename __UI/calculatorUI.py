# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\Project\calculator\__UI\calculatorUI.ui'
#
# Created: Tue Aug 22 18:26:11 2017
#      by: PyQt4 UI code generator 4.10
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

class Ui_calculator_mainwindow(object):
    def setupUi(self, calculator_mainwindow):
        calculator_mainwindow.setObjectName(_fromUtf8("calculator_mainwindow"))
        calculator_mainwindow.resize(346, 227)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(calculator_mainwindow.sizePolicy().hasHeightForWidth())
        calculator_mainwindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(calculator_mainwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.number_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.number_lineEdit.setObjectName(_fromUtf8("number_lineEdit"))
        self.horizontalLayout_2.addWidget(self.number_lineEdit)
        spacerItem = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.clear_pushbutton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_pushbutton.sizePolicy().hasHeightForWidth())
        self.clear_pushbutton.setSizePolicy(sizePolicy)
        self.clear_pushbutton.setObjectName(_fromUtf8("clear_pushbutton"))
        self.horizontalLayout_2.addWidget(self.clear_pushbutton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.one_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.one_pushbutton.setObjectName(_fromUtf8("one_pushbutton"))
        self.horizontalLayout_6.addWidget(self.one_pushbutton)
        self.two_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.two_pushbutton.setObjectName(_fromUtf8("two_pushbutton"))
        self.horizontalLayout_6.addWidget(self.two_pushbutton)
        self.three_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.three_pushbutton.setObjectName(_fromUtf8("three_pushbutton"))
        self.horizontalLayout_6.addWidget(self.three_pushbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.four_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.four_pushbutton.setObjectName(_fromUtf8("four_pushbutton"))
        self.horizontalLayout_5.addWidget(self.four_pushbutton)
        self.five_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.five_pushbutton.setObjectName(_fromUtf8("five_pushbutton"))
        self.horizontalLayout_5.addWidget(self.five_pushbutton)
        self.six_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.six_pushbutton.setObjectName(_fromUtf8("six_pushbutton"))
        self.horizontalLayout_5.addWidget(self.six_pushbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.seven_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.seven_pushbutton.setObjectName(_fromUtf8("seven_pushbutton"))
        self.horizontalLayout_3.addWidget(self.seven_pushbutton)
        self.eight_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.eight_pushbutton.setObjectName(_fromUtf8("eight_pushbutton"))
        self.horizontalLayout_3.addWidget(self.eight_pushbutton)
        self.nine_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.nine_pushbutton.setObjectName(_fromUtf8("nine_pushbutton"))
        self.horizontalLayout_3.addWidget(self.nine_pushbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.point_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.point_pushbutton.setObjectName(_fromUtf8("point_pushbutton"))
        self.horizontalLayout_4.addWidget(self.point_pushbutton)
        self.zero_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.zero_pushbutton.setObjectName(_fromUtf8("zero_pushbutton"))
        self.horizontalLayout_4.addWidget(self.zero_pushbutton)
        self.equals_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.equals_pushbutton.setObjectName(_fromUtf8("equals_pushbutton"))
        self.horizontalLayout_4.addWidget(self.equals_pushbutton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.plus_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.plus_pushbutton.setObjectName(_fromUtf8("plus_pushbutton"))
        self.verticalLayout_2.addWidget(self.plus_pushbutton)
        self.minus_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.minus_pushbutton.setObjectName(_fromUtf8("minus_pushbutton"))
        self.verticalLayout_2.addWidget(self.minus_pushbutton)
        self.multiply_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.multiply_pushbutton.setObjectName(_fromUtf8("multiply_pushbutton"))
        self.verticalLayout_2.addWidget(self.multiply_pushbutton)
        self.divide_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.divide_pushbutton.setObjectName(_fromUtf8("divide_pushbutton"))
        self.verticalLayout_2.addWidget(self.divide_pushbutton)
        self.percentage_pushbutton = QtGui.QPushButton(self.centralwidget)
        self.percentage_pushbutton.setObjectName(_fromUtf8("percentage_pushbutton"))
        self.verticalLayout_2.addWidget(self.percentage_pushbutton)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 0, 1, 1)
        calculator_mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(calculator_mainwindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        calculator_mainwindow.setStatusBar(self.statusbar)

        self.retranslateUi(calculator_mainwindow)
        QtCore.QMetaObject.connectSlotsByName(calculator_mainwindow)

    def retranslateUi(self, calculator_mainwindow):
        calculator_mainwindow.setWindowTitle(_translate("calculator_mainwindow", "Calculator", None))
        self.clear_pushbutton.setText(_translate("calculator_mainwindow", "Clear", None))
        self.one_pushbutton.setText(_translate("calculator_mainwindow", "1", None))
        self.two_pushbutton.setText(_translate("calculator_mainwindow", "2", None))
        self.three_pushbutton.setText(_translate("calculator_mainwindow", "3", None))
        self.four_pushbutton.setText(_translate("calculator_mainwindow", "4", None))
        self.five_pushbutton.setText(_translate("calculator_mainwindow", "5", None))
        self.six_pushbutton.setText(_translate("calculator_mainwindow", "6", None))
        self.seven_pushbutton.setText(_translate("calculator_mainwindow", "7", None))
        self.eight_pushbutton.setText(_translate("calculator_mainwindow", "8", None))
        self.nine_pushbutton.setText(_translate("calculator_mainwindow", "9", None))
        self.point_pushbutton.setText(_translate("calculator_mainwindow", ".", None))
        self.zero_pushbutton.setText(_translate("calculator_mainwindow", "0", None))
        self.equals_pushbutton.setText(_translate("calculator_mainwindow", "=", None))
        self.plus_pushbutton.setText(_translate("calculator_mainwindow", "+", None))
        self.minus_pushbutton.setText(_translate("calculator_mainwindow", "-", None))
        self.multiply_pushbutton.setText(_translate("calculator_mainwindow", "*", None))
        self.divide_pushbutton.setText(_translate("calculator_mainwindow", "/", None))
        self.percentage_pushbutton.setText(_translate("calculator_mainwindow", "%", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    calculator_mainwindow = QtGui.QMainWindow()
    ui = Ui_calculator_mainwindow()
    ui.setupUi(calculator_mainwindow)
    calculator_mainwindow.show()
    sys.exit(app.exec_())
