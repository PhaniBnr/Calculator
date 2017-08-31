import sys
from __UI import  calculatorUI
from PyQt4 import QtGui

class calc(QtGui.QMainWindow, calculatorUI.Ui_calculator_mainwindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.connectUI()

    def connectUI(self):
        self.one_pushbutton.clicked.connect(self.get_one)
        self.two_pushbutton.clicked.connect(self.get_two)
        self.three_pushbutton.clicked.connect(self.get_three)
        self.four_pushbutton.clicked.connect(self.get_four)
        self.five_pushbutton.clicked.connect(self.get_five)
        self.six_pushbutton.clicked.connect(self.get_six)
        self.seven_pushbutton.clicked.connect(self.get_seven)
        self.eight_pushbutton.clicked.connect(self.get_eight)
        self.nine_pushbutton.clicked.connect(self.get_nine)
        self.zero_pushbutton.clicked.connect(self.get_zero)
        self.plus_pushbutton.clicked.connect(self.addition)
        self.minus_pushbutton.clicked.connect(self.substraction)
        self.multiply_pushbutton.clicked.connect(self.multiply)
        self.divide_pushbutton.clicked.connect(self.division)
        self.equals_pushbutton.clicked.connect(self.equals)
        self.clear_pushbutton.clicked.connect(self.clear_lineedit)
        self.point_pushbutton.clicked.connect(self.get_point)

    def clear_lineedit(self):
        self.number_lineEdit.clear()

    def get_point(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '.')

    def get_val_linedit(self):
        self.get_val = str(self.number_lineEdit.text())

    def get_one(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '1')

    def get_two(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '2')

    def get_three(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '3')

    def get_four(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '4')

    def get_five(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '5')

    def get_six(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '6')

    def get_seven(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '7')

    def get_eight(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '8')

    def get_nine(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '9')

    def get_zero(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '0')

    def addition(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '+')

    def substraction(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '-')

    def division(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '/')

    def multiply(self):
        self.get_val_linedit()
        self.number_lineEdit.setText(self.get_val + '*')

    def equals(self):
        operation =  str(self.number_lineEdit.text())
        print operation
        # if '+' in operation:
        #     list_num = operation.split('+')
        #     self.result = sum([float(x) for x in list_num])
        # elif '-' in operation:
        #     list_num = operation.split('-')
        #     list_num = [float(x) for x in list_num]
        #     temp = list_num[0]
        #     for item in list_num[1:]:
        #         temp -= item
        #     self.result = temp
        # elif '*' in operation:
        #     list_num = operation.split('*')
        #     list_num = [float(x) for x in list_num]
        #     temp = list_num[0]
        #     for item in list_num[1:]:
        #         temp *= item
        #     self.result = temp
        # elif '/' in operation:
        #     list_num = operation.split('/')
        #     list_num = [float(x) for x in list_num]
        #     temp = list_num[0]
        #     for item in list_num[1:]:
        #         temp /= item
        #     self.result = temp
        # else:
        #     print "Invalid Operation"
        self.result = eval(operation)
        self.number_lineEdit.setText(str(self.result))


def main():
    app = QtGui.QApplication(sys.argv)
    myWindow = calc(None)
    myWindow.show()
    app.exec_()

if __name__ == "__main__":
    main()