from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QPixmap, QMovie
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("04-LineEdit")
        self.create_line_edit()

    
    def create_line_edit(self):
        line_edit = QLineEdit(self)
        line_edit.setFont(QFont("Sanserif",15))
        line_edit.setPlaceholderText("Digite sua senha...")
        #line_edit.setText("Ola, tudo bem")
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)



app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())