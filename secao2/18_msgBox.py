from PyQt6.QtWidgets import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("18_messageBox")
        self.criar_widgets()
        
    def criar_widgets(self):

        # cria os botoes
        btn_warning = QPushButton("Warnig")
        btn_information = QPushButton("Information")
        btn_about = QPushButton("About")
        btn_critical = QPushButton("Critical")
        btn_customizado = QPushButton("Customizado")

        # adiciona ao layout
        grid = QGridLayout()
        grid.addWidget(btn_warning, 0, 0)
        grid.addWidget(btn_information, 0, 1)
        grid.addWidget(btn_about, 1 , 0, 1,2)
        grid.addWidget(btn_critical,2,0)
        grid.addWidget(btn_customizado,3,1,1 ,2)
        self.setLayout(grid)
    
        #vincula os botoes as funcoes
        btn_warning.clicked.connect(self.warning)
        btn_information.clicked.connect(self.information)
        btn_about.clicked.connect(self.about)
        btn_critical.clicked.connect(self.critical)
        btn_customizado.clicked.connect(self.customizado)

    def customizado(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("Titulo")
        msgBox.setText("Esse é o  texto")
        msgBox.setInformativeText("Texto secundario")
        msgBox.setIcon(QMessageBox.Icon.Question)
        msgBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msgBox.button(QMessageBox.StandardButton.Yes).setText("Confirmar")
        msgBox.button(QMessageBox.StandardButton.No).setText("Cancelar")

        exec = msgBox.exec()

        if exec == QMessageBox.StandardButton.Yes:
            print("Pedido confirmado")
        else:
            print("Pedido cancelado")


    def warning(self):
        QMessageBox.warning(self,"Titulo", "Esse é o texto")
    
    def information(self):
        QMessageBox.information(self,"titulo ", "TExtoooo")

    def about(self):
        QMessageBox.about(self,"titulo",'mensagem')

    def critical(self):
        QMessageBox.critical(self,'titulo','menssagem')
    

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())