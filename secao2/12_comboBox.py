from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QIcon, QMovie
from PyQt6.QtCore import QSize
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("11_SpinBox")
        self.create_widgets()

    def create_widgets(self):
        self.combo = QComboBox()
        self.combo.addItem("Sabores")
        sabores = ['Mussarela','Calabresa', 'Alho', 'Chocolate', 'Atum']
        self.combo.addItems(sabores)
        self.combo.currentTextChanged.connect(self.combo_select)

        self.label = QLabel("Selecione o sabor da pizza")

        hbox = QHBoxLayout()
        hbox.addWidget(self.combo)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
    
    def combo_select(self):
        self.label.setText(f'O sabor selecionado foi: {self.combo.currentText()}')


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())