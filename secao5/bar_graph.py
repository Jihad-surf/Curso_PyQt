import pyqtgraph as pg
from PyQt6.QtWidgets import *
import sys

class Bar_Graph(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bar_Graph")
        
        vbox = QVBoxLayout()

        plot = pg.plot()

        #valores
        y = [10,8,12,13,16]
        x = range(len(y))

        # altera o eixo x
        xdict = {0:'janeiro', 1:'fevereiro', 2:'marco',3:'abril', 4:'maio'}
        axis = pg.AxisItem(orientation='bottom')
        axis.setTicks([xdict.items()])
        plot.setAxisItems(axisItems = {'bottom': axis}) 

        # cria as barras
        grafico_barras = pg.BarGraphItem(x=x, height= y, width=0.6, brush=(0,255,0,255))

        plot.addItem(grafico_barras)
        vbox.addWidget(plot)
        self.setLayout(vbox)

app = QApplication(sys.argv)
window = Bar_Graph()
window.show()
sys.exit(app.exec())
