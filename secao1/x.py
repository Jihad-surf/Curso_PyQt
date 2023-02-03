from PyQt6 import QtWidgets
import sys

class MyLineEdit(QtWidgets.QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.textChanged.connect(self.on_text_changed)
        self.textEdited.connect(self.on_text_edited)
        self.setProperty("last_text", self.text())

    def on_text_changed(self):
        if len(self.text()) == 4:
            self.setText(self.text() + '/')

    def on_text_edited(self):
        if len(self.text()) < len(self.property("last_text")):
            self.setProperty("last_text", self.text())
            return
        if len(self.text()) == 4:
            self.setText(self.text() + '/')
        self.setProperty("last_text", self.text())


app = QtWidgets.QApplication(sys.argv)
window = MyLineEdit()
window.show()
sys.exit(app.exec())