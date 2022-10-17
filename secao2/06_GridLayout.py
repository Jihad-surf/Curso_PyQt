from PyQt6.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout")
        self.criar_widgets()

    def criar_widgets(self):
        btn = QPushButton("Mudar o texto")
        btn.clicked.connect(self.clicked_btn)

        btn_voltar = QPushButton("Voltar texto original")
        btn_voltar.clicked.connect(self.clicked_voltar)

        self.texto_original = "E ai galera, esse é o nosso texto original"
        self.lb = QLabel(self.texto_original)

        grid = QGridLayout()
        grid.addWidget(btn, 0,0)
        grid.addWidget(btn_voltar, 1,0)
        grid.addWidget(self.lb, 0,1)
        self.setLayout(grid)

    def clicked_btn(self):
        self.lb.setText("O texto mudou")

    def clicked_voltar(self):
        self.lb.setText(self.texto_original)
        


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())