from PyQt6.QtWidgets import *
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 200, 850,400)
        self.setWindowTitle("Primeiro programa")
    
        self.create_button()    

    def create_button(self):
        btn = QPushButton("Click Me", self)
        btn.setGeometry(50,50, 150,90)
        btn.setFont(QFont("Times",20, QFont.Weight.Bold))
        btn.setIcon(QIcon("images/botao.png")) # adiona uma imagem dentro do botao
        btn.setIconSize(QSize(100,200))
 
        # adiciona um menu no botao
        menu = QMenu()
        menu.addAction("Copy")
        menu.addAction("Paste")
        btn.setMenu(menu)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
