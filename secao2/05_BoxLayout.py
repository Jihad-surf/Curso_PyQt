from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QPixmap, QMovie
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("05-boxLayout")
        self.criar_widgets()

    def criar_widgets(self):
        vbox = QVBoxLayout()

        btn1 = QPushButton("Entrar")
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Digite seu e-mail")

        line_edit2 = QLineEdit()
        line_edit2.setPlaceholderText("Insira sua senha")
        line_edit2.setEchoMode(QLineEdit.EchoMode.Password)

        vbox.addWidget(line_edit)
        vbox.addWidget(line_edit2)
        vbox.addWidget(btn1)
        
        self.setLayout(vbox)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())