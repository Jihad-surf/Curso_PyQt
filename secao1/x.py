from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QIcon, QMovie
from PyQt6.QtCore import QSize
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("11_SpinBox")
        self.create_widgets()
        self.label_result = QLabel("resultado")
    def create_widgets(self):

        self.combo = QComboBox()
        self.combo.currentTextChanged.connect(self.combo_select)
        self.combo.addItem("Mussarela")
        sabores = ['Calabresa', 'Portuguesa', 'Alho']
        self.combo.addItems(sabores)

        
        self.label2 = QLabel("Escolha uma pizza")

        hbox = QHBoxLayout()
        hbox.addWidget(self.label2)
        hbox.addWidget(self.combo)
        hbox.addWidget(self.label_result)
        self.setLayout(hbox)

    def combo_select(self):
        self.label_result.setText("dsf")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())