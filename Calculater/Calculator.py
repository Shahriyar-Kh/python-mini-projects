from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.op=None
        self.value1=None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 550)
        MainWindow.setStyleSheet("\n"
"     QMainWindow {\n"
"       background-color: #1C1C1C; /* Dark gray background */\n"
"       border: 2px solid #444444;\n"
"       border-radius: 15px;\n"
"     }\n"
"     QPushButton {\n"
"       color: #FFFFFF;\n"
"       border: 2px solid #444444;\n"
"       border-radius: 15px;\n"
"       font-family: \"Segoe UI\";\n"
"       font-size: 24px;\n"
"       font-weight: bold;\n"
"       padding: 15px;\n"
"     }\n"
"     QPushButton:pressed {\n"
"       background-color: #5A5A5A;\n"
"     }\n"
"     QPushButton#btn_percent, \n"
"     QPushButton#btn_arrow,\n"
"     QPushButton#btn_clear, \n"
"     QPushButton#btn_div, \n"
"     QPushButton#btn_mul, \n"
"     QPushButton#btn_sub, \n"
"     QPushButton#btn_plus, \n"
"     QPushButton#btn_equal {\n"
"       background-color: #FF5722; /* Deep orange for operator buttons */\n"
"      \n"
"     }\n"
"     QPushButton#btn_percent:hover, \n"
"     QPushButton#btn_arrow:hover,\n"
"     QPushButton#btn_clear:hover, \n"
"     QPushButton#btn_div:hover, \n"
"     QPushButton#btn_mul:hover, \n"
"     QPushButton#btn_sub:hover, \n"
"     QPushButton#btn_plus:hover, \n"
"     QPushButton#btn_equal:hover {\n"
"       background-color: #FF7043 ; /* Lighter shade of orange for hover effect */\n"
"     }\n"
"     QPushButton#btn_zero, \n"
"     QPushButton#btn_one, \n"
"     QPushButton#btn_two, \n"
"     QPushButton#btn_three, \n"
"     QPushButton#btn_four, \n"
"     QPushButton#btn_five, \n"
"     QPushButton#btn_six, \n"
"     QPushButton#btn_seven, \n"
"     QPushButton#btn_eight, \n"
"     QPushButton#btn_nine, \n"
"     QPushButton#btn_dot {\n"
"       background-color: #009688; /* Teal for digit buttons */\n"
"     }\n"
"     QPushButton#btn_zero:hover, \n"
"     QPushButton#btn_one:hover, \n"
"     QPushButton#btn_two:hover, \n"
"     QPushButton#btn_three:hover, \n"
"     QPushButton#btn_four:hover, \n"
"     QPushButton#btn_five:hover, \n"
"     QPushButton#btn_six:hover, \n"
"     QPushButton#btn_seven:hover, \n"
"     QPushButton#btn_eight:hover, \n"
"     QPushButton#btn_nine:hover, \n"
"     QPushButton#btn_dot:hover {\n"
"       background-color: #26A69A; /* Lighter shade of teal for hover effect */\n"
"     }\n"
"     QLineEdit {\n"
"       background-color:#FFFFFF; /* Darker gray for line edit */\n"
"       color: black;\n"
"       border: 2px solid #CCCCCC;\n"
"       border-radius: 10px;\n"
"       padding: 15px;\n"
"       font-size: 28px;\n"
"       font-family: \"Segoe UI\";\n"
"       font-weight: bold;\n"
"\n"
"     }\n"
"   ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_percent = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.percent("%"))
        self.btn_percent.setGeometry(QtCore.QRect(10, 110, 75, 75))
        self.btn_percent.setObjectName("btn_percent")
        self.btn_arrow = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.remove_it())
        self.btn_arrow.setGeometry(QtCore.QRect(185, 110, 75, 75))
        self.btn_arrow.setObjectName("btn_arrow")
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("C"))
        self.btn_clear.setGeometry(QtCore.QRect(95, 110, 75, 75))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("/"))
        self.btn_div.setGeometry(QtCore.QRect(275, 110, 75, 75))
        self.btn_div.setObjectName("btn_div")
        self.btn_mul = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("*"))
        self.btn_mul.setGeometry(QtCore.QRect(275, 200, 75, 75))
        self.btn_mul.setObjectName("btn_mul")
        self.btn_seven = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("7"))
        self.btn_seven.setGeometry(QtCore.QRect(10, 200, 75, 75))
        self.btn_seven.setObjectName("btn_seven")
        self.btn_eight = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("8"))
        self.btn_eight.setGeometry(QtCore.QRect(95, 200, 75, 75))
        self.btn_eight.setObjectName("btn_eight")
        self.btn_nine = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("9"))
        self.btn_nine.setGeometry(QtCore.QRect(185, 200, 75, 75))
        self.btn_nine.setObjectName("btn_nine")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("-"))
        self.btn_sub.setGeometry(QtCore.QRect(275, 290, 75, 75))
        self.btn_sub.setObjectName("btn_sub")
        self.btn_four = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("4"))
        self.btn_four.setGeometry(QtCore.QRect(10, 290, 75, 75))
        self.btn_four.setObjectName("btn_four")
        self.btn_five = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("5"))
        self.btn_five.setGeometry(QtCore.QRect(95, 290, 75, 75))
        self.btn_five.setObjectName("btn_five")
        self.btn_six = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("6"))
        self.btn_six.setGeometry(QtCore.QRect(185, 290, 75, 75))
        self.btn_six.setObjectName("btn_six")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("+"))
        self.btn_plus.setGeometry(QtCore.QRect(275, 380, 75, 75))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_one = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("1"))
        self.btn_one.setGeometry(QtCore.QRect(10, 380, 75, 75))
        self.btn_one.setObjectName("btn_one")
        self.btn_two = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("2"))
        self.btn_two.setGeometry(QtCore.QRect(95, 380, 75, 75))
        self.btn_two.setObjectName("btn_two")
        self.btn_three = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("3"))
        self.btn_three.setGeometry(QtCore.QRect(185, 380, 75, 75))
        self.btn_three.setObjectName("btn_three")
        self.btn_dot = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.decimal())
        self.btn_dot.setGeometry(QtCore.QRect(185, 470, 75, 75))
        self.btn_dot.setObjectName("btn_dot")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.math())
        self.btn_equal.setGeometry(QtCore.QRect(275, 470, 75, 75))
        self.btn_equal.setObjectName("btn_equal")
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.press_it("0"))
        self.btn_zero.setGeometry(QtCore.QRect(10, 470, 160, 75))
        self.btn_zero.setObjectName("btn_zero")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 341, 91))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def percent(self,pressed):
        self.value1=float(self.lineEdit.text())
        self.op=pressed
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText("Total value")
        #function for calculation
    def math(self):
        screen=self.lineEdit.text()
        if self.op is None:
            result = eval(screen)
            self.lineEdit.setText(f"{result:.2f}")  # Format result to 2 decimal places
        else:     
           try:
            total_value=float(screen)
            percent=(self.value1/total_value)*100
            self.lineEdit.setText(f"{percent:.2f}")
           except Exception:
               self.lineEdit.setText("Error")


    def remove_it(self):
        screen=self.lineEdit.text()
        screen=screen[:-1]
        self.lineEdit.setText(screen)

    #function for decimal
    def decimal(self):
        #store the current text
        current_text=self.lineEdit.text()
        #find the last part of the last opernad of the current text
        last_op=current_text.split("+")[-1].split("*")[-1].split("-")[-1].split("/")[-1]

        if "." not in last_op:
            self.lineEdit.setText(f"{current_text}.")

    def press_it(self,pressed):
        if pressed=="C":
            self.lineEdit.setText("0")
        else:
            #check to see if start with 0
            if self.lineEdit.text()=="0":
                self.lineEdit.setText("")
            #cancatenate pressed button with the output    
            self.lineEdit.setText(f"{self.lineEdit.text()}{pressed}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn_percent.setText(_translate("MainWindow", "%"))
        self.btn_arrow.setText(_translate("MainWindow", "<<"))
        self.btn_clear.setText(_translate("MainWindow", "C"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_mul.setText(_translate("MainWindow", "x"))
        self.btn_seven.setText(_translate("MainWindow", "7"))
        self.btn_eight.setText(_translate("MainWindow", "8"))
        self.btn_nine.setText(_translate("MainWindow", "9"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_four.setText(_translate("MainWindow", "4"))
        self.btn_five.setText(_translate("MainWindow", "5"))
        self.btn_six.setText(_translate("MainWindow", "6"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_one.setText(_translate("MainWindow", "1"))
        self.btn_two.setText(_translate("MainWindow", "2"))
        self.btn_three.setText(_translate("MainWindow", "3"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_zero.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
