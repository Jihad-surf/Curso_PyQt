import pyqtgraph as pg
from PyQt6.QtWidgets import *
import sys
import random

class Line_Graph(QWidget):
    def __init__(self):
        super().__init__()
        
        vbox = QVBoxLayout()

        # criar a plot
        self.plt = pg.PlotWidget()
        self.plt.addLegend()

        # propriedades 
        self.plt.setBackground('w')
        self.plt.showGrid(x=True,y=True)
        self.plt.setLabel('left', 'Velocidade', units = 'km/h')
        self.plt.setLabel('bottom', 'Tempo', units = 's')
        #self.plt.setXRange(0,15)
        #self.plt.setYRange(0,15)


        # valores de x e y
        y = [0, 3, 2, 5, 6, 9, 13 ,15,10,19]
        y2 = [2, 8, 4, 5,3, 10, 15 ,16,19,14]
        x = range(10)

        # adiconar valores na plot
        self.plt.plot(x,y, name='branco')
        self.plt.plot(x,y2, pen='b', symbol='o', symbolPen='g', fillLevel=0, brush=(255,255,255,20),  name='blue')

        btn = QPushButton("Alterar valores", clicked=self.alterar)

        vbox.addWidget(btn)
        vbox.addWidget(self.plt)
        self.setLayout(vbox)

    def alterar(self):
        self.plt.clear()
        y = [0, 3, 2, 5, 6, 9, 13 ,15,10,19]
        y2 = []
        [y2.append(random.randint(0,20)) for i in range(10)]
        x = range(10)

        self.plt.plot(x,y, name='branco')
        self.plt.plot(x,y2, pen='b', symbol='o', symbolPen='g', fillLevel=0, brush=(255,255,255,20),  name='blue')


app = QApplication(sys.argv)
window = Line_Graph()
window.show()
sys.exit(app.exec())



