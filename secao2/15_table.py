from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("15_Table")
        self.create_widgets()

    def create_widgets(self):
        self.table = QTableWidget()
        dell = QPushButton("Dell", clicked= lambda: self.del_row())
        self.table.setRowCount(10)
        self.table.setColumnCount(4)

        self.table.setItem(0, 0, QTableWidgetItem("Nome"))
        self.table.setItem(0, 1, QTableWidgetItem("Cidade"))
        self.table.setItem(0, 2, QTableWidgetItem("Idade"))
        self.table.setItem(0, 3, QTableWidgetItem("Profissao"))

        dados = {
            "Joao": ["Sao Paulo", 25, "Engenheiro"],
            "Pedro": ["Rio de Janeiro", 30, "Enfermeiro"],
        }
        linha = 2
        for pessoa in dados:
            self.table.setItem(linha, 0, QTableWidgetItem(pessoa))
            self.table.setItem(linha, 1, QTableWidgetItem(dados[pessoa][0]))
            self.table.setItem(linha, 2, QTableWidgetItem(str(dados[pessoa][1])))
            self.table.setItem(linha, 3, QTableWidgetItem(dados[pessoa][2]))
            linha += 1
                

        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        vbox.addWidget(dell)
        self.setLayout(vbox)

    def del_row(self):
        print(self.table.currentRow())

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())