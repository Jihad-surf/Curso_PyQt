from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont,QPixmap, QMovie
import sys


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("02-QLabel")
        self.setMinimumHeight(80)
        self.setMinimumWidth(250)

        label = QLabel(self)
        movie = QMovie("images/fundoGif.gif")
        movie.setSpeed(40)
        label.setMovie(movie)
        movie.start()

"""
        label = QLabel(self)
        pixmap = QPixmap('images/fundoimg.png')
        label.setPixmap(pixmap)

        label = QLabel(self)
        label.setText("Hello World!!!")
        label.move(100,20)
        label.setFont(QFont("Sanserif", 20))
        label.setStyleSheet('color: red')
        label.clear()
"""

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())