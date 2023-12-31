# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'password.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 479)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(255, 76, 238);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(160, 10, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setObjectName("title")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(180, 80, 341, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.result.setFont(font)
        self.result.setStyleSheet("color: rgb(255, 255, 255);")
        self.result.setObjectName("result")
        self.cb_numbers = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_numbers.setGeometry(QtCore.QRect(120, 150, 451, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.cb_numbers.setFont(font)
        self.cb_numbers.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb_numbers.setTristate(False)
        self.cb_numbers.setObjectName("cb_numbers")
        self.cb_alphabet = QtWidgets.QCheckBox(self.centralwidget)
        self.cb_alphabet.setGeometry(QtCore.QRect(120, 230, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.cb_alphabet.setFont(font)
        self.cb_alphabet.setStyleSheet("color: rgb(255, 255, 255);")
        self.cb_alphabet.setObjectName("cb_alphabet")
        self.btn_generate = QtWidgets.QPushButton(self.centralwidget)
        self.btn_generate.setGeometry(QtCore.QRect(190, 330, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(115, 0, 255);\n"
"border: 6px solid rgb(255, 255, 255);\n"
"border-radius: 16px;")
        self.btn_generate.setObjectName("btn_generate")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Генератор паролів"))
        self.result.setText(_translate("MainWindow", "Тут буде результат"))
        self.cb_numbers.setText(_translate("MainWindow", "Використовувати числа"))
        self.cb_alphabet.setText(_translate("MainWindow", "Використовувати алфавіт"))
        self.btn_generate.setText(_translate("MainWindow", "Згенерувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
