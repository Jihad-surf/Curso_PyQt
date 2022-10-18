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
        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(4)

        self.table.setItem(0,0, QTableWidgetItem("Nome"))
        self.table.setItem(0,1, QTableWidgetItem("Cidade"))
        self.table.setItem(0,2, QTableWidgetItem("Idade"))
        self.table.setItem(0,3, QTableWidgetItem("Profissao"))

        dados = {
            "Joao": ["Sao Paulo", 25, "Engenheiro"],
            "Pedro": ["Rio de Janeiro", 30, "Enfermeiro"],
            "Maria": ["Minas gerais", 45, "Professora"],
            "Fernanda": ["Porto Alegre", 22, "Estudante"],
            "Gabriel": ["Sao Paulo", 28, "Entregador"],
            "Paula": ["Fortaleza", 54, "Medica"],
            "Hugo": ["Amazonas", 20, "Estagiario"],
            "Caique": ["Santa Catarina", 36, "Mecanico"],
            "Joao2": ["Goias", 28, "Desempregado"]
        }
        linha = 1
        for pessoa in dados:
            self.table.setItem(linha, 0, QTableWidgetItem(pessoa))
            self.table.setItem(linha, 1, QTableWidgetItem(dados[pessoa][0]))
            self.table.setItem(linha, 2, QTableWidgetItem(str(dados[pessoa][1])))
            self.table.setItem(linha, 3, QTableWidgetItem(dados[pessoa][2]))
            linha +=1

        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        self.setLayout(vbox)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())