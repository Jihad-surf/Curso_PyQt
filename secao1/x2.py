import pyqtgraph as pg
from PyQt6.QtWidgets import *
import sys
from random import randint

# line graph
class Line_Graph(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("line_graph")

        hbox = QHBoxLayout()

        # y values to plot by line1
        y = [2,4,6,8,10,12,14,16,18,20]
        y2 = [0,1,2,4,12,14,16,17,14,22]
        x = range(10)

        # create plot
        self.plt = pg.PlotWidget()
        self.plt.showGrid(x=True,y=True)
        self.plt.addLegend()
        self.plt.setBackground('w')

        # set properties
        self.plt.setLabel('left', 'Value', units='V')
        self.plt.setLabel('bottom', 'Time', units='s')
        self.plt.setXRange(0,10)
        self.plt.setYRange(0,20)
    
        # plot
        self.plt.plot(x, y, pen='r', symbol='x', symbolPen='g', name='red')
        self.plt.plot(x, y2, pen='b', symbol='o', symbolPen='g', name='blue', brush=(0,0,0,50), fillLevel=5)

        btn = QPushButton("click",clicked=self.btn)

        hbox.addWidget(btn)
        hbox.addWidget(self.plt)
        self.setLayout(hbox)

    def btn(self):
        self.plt.clear()
        y = [2,4,6,8,10,12,14,16,18,20]
        y2 = []
        [y2.append(randint(0,20)) for i in range(10)]
        x = range(0,10)
        self.plt.plot(x, y, pen='r', symbol='x', symbolPen='g', name='red')
        self.plt.plot(x, y2, pen='b', symbol='o', symbolPen='g', name='blue', brush=(0,0,0,50), fillLevel=5)


app = QApplication(sys.argv)
window = Line_Graph()
window.show()
sys.exit(app.exec())