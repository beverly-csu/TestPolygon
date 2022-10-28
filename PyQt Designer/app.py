from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QApplication
from calc import Ui_calculator


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_calculator()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText('1 + 10')
        self.ui.btn_solve.clicked.connect(self.calculate)

    def calculate(self):
        text = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(str(eval(text)))


app = QApplication([])
win = Calculator()
win.show()
app.exec()