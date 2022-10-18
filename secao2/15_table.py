from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("15_Table")
        self.create_widgets()

    def create_widgets(self):
        table = QTableWidget()
        table.setRowCount(10)
        table.setColumnCount(4)

        table.setItem(0, 0, QTableWidgetItem("Nome"))
        table.setItem(0, 1, QTableWidgetItem("Cidade"))
        table.setItem(0, 2, QTableWidgetItem("Idade"))
        table.setItem(0, 3, QTableWidgetItem("Profissao"))

        table.setItem(1, 0, QTableWidgetItem("Thiago"))
        table.setItem(1, 1, QTableWidgetItem("Parana"))
        table.setItem(1, 2, QTableWidgetItem("25"))
        table.setItem(1, 3, QTableWidgetItem("Pedreiro"))

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
        linha = 2
        for pessoa in dados:
            table.setItem(linha, 0, QTableWidgetItem(pessoa))
            table.setItem(linha, 1, QTableWidgetItem(dados[pessoa][0]))
            table.setItem(linha, 2, QTableWidgetItem(str(dados[pessoa][1])))
            table.setItem(linha, 3, QTableWidgetItem(dados[pessoa][2]))
            linha += 1
                

        vbox = QVBoxLayout()
        vbox.addWidget(table)
        self.setLayout(vbox)



app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())