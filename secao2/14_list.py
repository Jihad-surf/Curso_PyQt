from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("14_list")
        self.create_widgets()

    def create_widgets(self):
        self.list = QListWidget()
        self.list.addItem("Mussarela")
        self.list.addItem("Calabresa")
        self.list.addItem("Alho")
        self.list.addItem("Presunto")
        self.list.clicked.connect(self.label_text)

        self.label = QLabel("Pizza sabor:")

        vbox = QVBoxLayout()
        vbox.addWidget(self.list)
        vbox.addWidget(self.label)
        self.setLayout(vbox)

    def label_text(self):
        sabor = self.list.currentItem()
        self.label.setText(f'Pizza Sabor: {sabor.text()}')


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())