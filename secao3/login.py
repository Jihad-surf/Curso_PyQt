# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(500,50,516, 801)
        Form.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 401, 671))
        self.label.setStyleSheet("border-image: url(C:/Users/Jihad/Desktop/Projetos Python/Curso_PyQt/secao3/images/background.jpg);\n"
"border-radius: 25px")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 361, 601))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(0, 0, 0,125);\n"
"border-radius: 20px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(210, 160, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(155, 390, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:none;\n"
"    border-bottom: 2px solid rgba(240, 240, 240,190);\n"
"    padding-left: 10px;\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-bottom: 4px solid rgb(255, 255, 255);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(155, 475, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:none;\n"
"    border-bottom: 2px solid rgba(240, 240, 240,190);\n"
"    padding-left: 10px;\n"
"    color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border-bottom: 4px solid rgb(255, 255, 255);\n"
"}")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(110, 410, 35, 35))
        self.label_4.setStyleSheet("border-image: url(C:/Users/Jihad/Desktop/Projetos Python/Curso_PyQt/secao3/images/login.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 495, 35, 35))
        self.label_5.setStyleSheet("border-image: url(C:/Users/Jihad/Desktop/Projetos Python/Curso_PyQt/secao3/images/redefinir-senha.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 600, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color:rgb(255, 255, 255);\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.00995025 rgba(0, 0, 0, 20), stop:1 rgba(0, 0, 0, 100));\n"
"    border:none;\n"
"    border-radius:25px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:1px solid rgba(255, 255, 255,180);\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.00995025 rgba(0, 0, 0, 30), stop:1 rgba(0, 0, 0, 140));\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    border:1px solid rgb(255, 255, 255);\n"
"    background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.00995025 rgba(0, 0, 0, 40), stop:1 rgba(0, 0, 0, 180));\n"
"    font:25px\n"
"}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Log In"))
        self.lineEdit.setPlaceholderText(_translate("Form", "User Name"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password"))
        self.pushButton.setText(_translate("Form", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
