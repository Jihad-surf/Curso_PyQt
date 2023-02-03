import sys
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel("a minha mãe é linda e o Apooloo também", self)
        button = QPushButton("Clique aqui", self)
        button.clicked.connect(self.showMessage)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(button)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Label and Button Example")
        self.show()

    def showMessage(self):
        print("a hanna é linda")

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec())