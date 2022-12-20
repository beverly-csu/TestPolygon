import serial
from PyQt5.QtWidgets import QApplication, QColorDialog, QWidget, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        btn_color = QPushButton('Выбрать цвет')
        btn_color.clicked.connect(self.changeColor)
        v_main = QVBoxLayout()
        v_main.addWidget(btn_color)
        self.setLayout(v_main)
        self.setWindowTitle('Color test')
        self.resize(400, 400)

        self.arduino = serial.Serial(port='COM7', baudrate=115200, timeout=.1)

    def changeColor(self):
        new_color = QColorDialog.getColor()
        new_color = new_color.getRgb()
        new_color = f'{new_color[0]} {new_color[1]} {new_color[2]}'
        self.arduino.write(new_color.encode('utf-8'))


app = QApplication([])
window = MyWindow()
window.show()
app.exec()