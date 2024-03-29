# Form implementation generated from reading ui file 'novoPedido.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import requests
import sqlite3

class Novo_Pedido(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setGeometry(490, 80, 520, 700)
        Form.setStyleSheet("QWidget#Form {\n"
"    background-color: qlineargradient(spread:pad, x1:0.503, y1:0, x2:0.522, y2:1, stop:0.159204 rgba(0, 214, 38, 255), stop:1 rgba(248, 248, 248, 255));\n"
"}\n"
"\n"
"QRadioButton{\n"
"margin-top:15px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    margin-top:8px\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(-1, 11, -1, 0)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setFamily("Gabriola")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMaximumSize(QtCore.QSize(420, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        sabores = ['Alho e óleo - (mussarela, alho e queijo parmesão) - R$25,00', 'Aliche - (mussarela, aliche e tomates) - R$38,00', 'Atum - (mussarela, atum e cebola e orégano) - R$50,00', 'Bacon - (mussarela coberta com bacon e orégano) - R$49,00', 'Banana com Canela - (banana caramelizada, leite condensado e canela) - R$50,00', 'Bauru - (Presunto, mussarela, tomate, orégano e azeitonas) - R$34,00', 'Beijinho - (chocolate branco, coco e leite condensado) - R$55,00', 'Berinjela - (berinjela, cebola, parmesão, mussarela e azeitona preta) - R$56,00', 'Bolonhesa - (mussarela, molho a bolonhesa e orégano) - R$32,00', 'Brasileira - (ervilha, milho, palmito, tomate, mussarela e manjericão) - R$59,00', 'Brócolis - (brócolis refogado coberto com mussarela e alho) - R$60,00', 'Calabresa - (mussarela, linguiça calabresa e cebola) - R$53,00', 'Califórnia - (mussarela, presunto, salada de frutas e orégano) - R$31,00', 'Camarão - (camarão, molho de tomate, mussarela e catupiry) - R$58,00', 'Canadense - (mussarela, lombo, champignon, palmito e catupiry) - R$49,00', 'Carne Seca - (Carne seca, mussarela, cebola, parmesão e orégano) - R$35,00', 'Champignon - (mussarelam champignon e orégano) - R$55,00', 'Chocolate - (chocolate preto ou branco) - R$33,00', 'Escarola - (escarola refogada, mussarela e orégano) - R$26,00', 'Espanhola - (presunto, mussarela, calabresa e cebola) - R$33,00', 'Frango - (molho de tomate, mussarela e frango) - R$56,00', 'Frango com Catupiry - (molho de tomate, mussarela, frango e catupiry) - R$46,00', 'Gorgonzola - (Gorgonzola, tomate, orégano e azeitonas) - R$31,00', 'Havaiana - (mussarela, lombo e abacaxi) - R$34,00', 'Italiana - (mussarela, parmesão, salame italiano e tomates) - R$37,00', 'Lombinho - (mussarela, lombo defumado e cebola) - R$45,00', 'M&M - (chocolate e M&M) - R$58,00', 'Marguerita - (mussarela, rodelas de tomate e manjericão) - R$28,00', 'Mineira - (mussarela, catupiry e milho verde) - R$50,00', 'Mista - (mussarela, presunto e orégano) - R$35,00', 'Mussarela - (mussarela, rodelas de tomate e orégano) - R$29,00', 'Napolitana - (mussarela, rodelas de tomate, queijo parmesão e orégano) - R$36,00', 'Nutella com Morango - (nutella e morango) - R$36,00', 'Palmito - (mussarela, palmito e orégano) - R$58,00', 'Parmegiana - (presunto, mussarela, molho parmegiana) - R$55,00', 'Paçoca - (chocolate e paçoca de amendoim) - R$34,00', 'Pepperoni - (mussarela, pepperoni e cebola) - R$50,00', 'Portuguesa - (mussarela, ovos, palmito, pimentão, ervilha, presunto e cebola) - R$48,00', 'Prestígio - (chocolate, coco ralado e leite condensado) - R$54,00', 'Quatro queijos - (mussarela, provolone, parmesão e catupiry) - R$29,00', 'Romana - (mussarela aliche e queijo parmesão e orégano) - R$28,00', 'Romeu e Julieta - (goiabada e  mussarela) - R$30,00', 'Rúcula com Tomate Seco - (mussarela, rúcula, tomate seco e orégano) - R$45,00', 'Sensação - (chocolate, granulado e morangos) - R$56,00', 'Siciliana - (mussarela, bacon e champignon ao molho rose) - R$55,00', 'Sorvete - (chocolate e sorvete) - R$60,00', 'Strogonoff - (mussarela, champignon, strogonoff de frango e batata palha) - R$60,00', 'Toscana - (linguiça calabresa bacon e catupiry) - R$59,00', 'Tropical - (mussarela, frango, milho, ervilha, ovos e catupiry) - R$57,00', 'Vegetariana - (mussarela, pimentão, cebola, azeitona, ervilha, tomate, palmito) - R$26,00']
        self.comboBox.addItems(sabores)
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_2.setStyleSheet("font: bold")
        self.radioButton_catupiry = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_catupiry.setFont(font)
        self.radioButton_catupiry.setObjectName("radioButton_catupiry")
        self.verticalLayout.addWidget(self.radioButton_catupiry)
        self.radioButton_cheeder = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_cheeder.setFont(font)
        self.radioButton_cheeder.setObjectName("radioButton_cheeder")
        self.verticalLayout.addWidget(self.radioButton_cheeder)
        self.radioButton_vulcao = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_vulcao.setFont(font)
        self.radioButton_vulcao.setObjectName("radioButton_vulcao")
        self.verticalLayout.addWidget(self.radioButton_vulcao)
        self.radioButton_semBorda = QtWidgets.QRadioButton(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.radioButton_semBorda.setFont(font)
        self.radioButton_semBorda.setObjectName("radioButton_semBorda")
        self.verticalLayout.addWidget(self.radioButton_semBorda)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_numero = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_numero.setFont(font)
        self.lineEdit_numero.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_numero.setObjectName("lineEdit_numero")
        self.gridLayout.addWidget(self.lineEdit_numero, 2, 2, 1, 1)
        self.lineEdit_tel = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_tel.setFont(font)
        self.lineEdit_tel.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.gridLayout.addWidget(self.lineEdit_tel, 4, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1)
        self.lineEdit_bairro = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_bairro.setFont(font)
        self.lineEdit_bairro.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_bairro.setObjectName("lineEdit_bairro")
        self.gridLayout.addWidget(self.lineEdit_bairro, 3, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.lineEdit_rua = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_rua.setFont(font)
        self.lineEdit_rua.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_rua.setObjectName("lineEdit_rua")
        self.gridLayout.addWidget(self.lineEdit_rua, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 2, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)
        self.lineEdit_cep = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lineEdit_cep.setFont(font)
        self.lineEdit_cep.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lineEdit_cep.setObjectName("lineEdit_cep")
        self.gridLayout.addWidget(self.lineEdit_cep, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)

        self.observacao = QtWidgets.QTextEdit(Form)
        self.gridLayout.addWidget(self.observacao,5,2,1,1)
        self.observacao.setMaximumHeight(45)
        self.observacao.setViewportMargins(0,8,0,0)
        self.observacao.setPlaceholderText("Observação...")

        self.label_valorTotal = QtWidgets.QLabel(Form)
        self.label_valorTotal.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_valorTotal.setFont(font)
        self.label_valorTotal.setStyleSheet("margin-right:50px")
        self.label_valorTotal.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_valorTotal.setObjectName("label_valorTotal")
        self.label_valorTotal.setStyleSheet("font:bold")
        self.verticalLayout_2.addWidget(self.label_valorTotal)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('margin-bottom:5')
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # conectando funcoes
        self.lineEdit_cep.textChanged.connect(self.pega_cep)
        self.lineEdit_tel.textChanged.connect(self.tel)

        self.pushButton.clicked.connect(lambda: self.novo_pedido(Form))
        
        self.comboBox.currentTextChanged.connect(self.calcula_valor)
        self.radioButton_catupiry.toggled.connect(self.calcula_valor)
        self.radioButton_cheeder.toggled.connect(self.calcula_valor)
        self.radioButton_semBorda.toggled.connect(self.calcula_valor)
        self.radioButton_vulcao.toggled.connect(self.calcula_valor)

    def novo_pedido(self, Form):
        pizza_sabor = self.comboBox.currentText().split('-')[0]

        borda_sabor = ''
        if self.radioButton_catupiry.isChecked():
            borda_sabor = self.radioButton_catupiry.text().split('-')[0]
        if self.radioButton_cheeder.isChecked():
            borda_sabor = self.radioButton_cheeder.text().split('-')[0]
        if self.radioButton_semBorda.isChecked():
            borda_sabor = self.radioButton_semBorda.text().split('-')[0]
        if self.radioButton_vulcao.isChecked():
            borda_sabor = self.radioButton_vulcao.text().split('-')[0]

        obs = self.observacao.toPlainText()
        rua = self.lineEdit_rua.text()
        numero = self.lineEdit_numero.text()
        telefone = self.lineEdit_tel.text()
        bairro = self.lineEdit_bairro.text()
        status = 'Não Finalizado'
        
        valor = self.calcula_valor()

        sabor = pizza_sabor + ' borda: '+ borda_sabor
        try:
            banco = sqlite3.connect('secao4/pizzaria.db')
            cursor = banco.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS pedidos(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Pizza TEXT,
                Observacao TEXT,
                Rua TEXT,
                Bairro TEXT,
                Numero INTEGER,
                Telefone TEXT,
                Status TEXT,
                Valor_total INTEGER
            )
            ''')
            cursor.execute('''
                INSERT INTO pedidos VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);
            ''',(None, sabor, obs, rua, bairro, numero, telefone, status, valor))
            banco.commit()
            banco.close()

        except sqlite3.Error as erro:
            print(erro)

        Form.close() 
        
    def calcula_valor(self):
        pizza = self.comboBox.currentText()[-5:-3]

        borda = 0
        if self.radioButton_catupiry.isChecked():
            borda = self.radioButton_catupiry.text().split('-')[1].replace("R$",'').replace(",00",'')
        if self.radioButton_cheeder.isChecked():
            borda = self.radioButton_cheeder.text().split('-')[1].replace("R$",'').replace(",00",'')
        if self.radioButton_semBorda.isChecked():
            borda = self.radioButton_semBorda.text().split('-')[1].replace("R$",'').replace(",00",'')
        if self.radioButton_vulcao.isChecked():
            borda = self.radioButton_vulcao.text().split('-')[1].replace("R$",'').replace(",00",'')
        
        valor = str(int(pizza) + int(borda))
        self.label_valorTotal.setText(f'Valor Total: R${valor},00')

        return valor

    def tel(self):
        if len(self.lineEdit_tel.text()) ==2 and '(' not in self.lineEdit_tel.text():
            self.lineEdit_tel.setText(f'({self.lineEdit_tel.text()}) ')
        if len(self.lineEdit_tel.text()) ==3 and '(' in self.lineEdit_tel.text():
            self.lineEdit_tel.clear()

    def pega_cep(self): 
        cep = self.lineEdit_cep.text()

        if len(cep) == 8:
            try:
                link = f'https://viacep.com.br/ws/{cep}/json/'
                
                requisicao = requests.get(link)
                dic_requisicao = requisicao.json()

                self.lineEdit_rua.setText(dic_requisicao['logradouro'])
                self.lineEdit_bairro.setText(dic_requisicao['bairro'])
            except:
                self.lineEdit_rua.setText("CEP Invalido")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Cadastrar Pedido"))
        self.label_2.setText(_translate("Form", "Sabor da Borda"))
        self.radioButton_catupiry.setText(_translate("Form", "Catupiry - R$10,00"))
        self.radioButton_cheeder.setText(_translate("Form", "Cheeder - R$8,00"))
        self.radioButton_vulcao.setText(_translate("Form", "Vulcão - R$15,00"))
        self.radioButton_semBorda.setText(_translate("Form", "Sem Borda - R$0,00"))
        self.label_5.setText(_translate("Form", "Numero:"))
        self.label_7.setText(_translate("Form", "Telefone:"))
        self.label_3.setText(_translate("Form", "Cep:"))
        self.label_4.setText(_translate("Form", "Rua:"))
        self.label_6.setText(_translate("Form", "Bairro:"))
        self.label_valorTotal.setText(_translate("Form", "Valor Total:"))
        self.pushButton.setText(_translate("Form", "Criar Pedido"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Novo_Pedido()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
