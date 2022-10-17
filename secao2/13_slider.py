from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("13_slider")
        self.create_widgets()

    def create_widgets(self):
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(10)
        self.slider.setMaximum(80)
        self.slider.valueChanged.connect(self.slider_value)

        self.label = QLabel("10")
        hbox = QHBoxLayout()
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

    def slider_value(self):
        self.label.setText(str(self.slider.value()))

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())