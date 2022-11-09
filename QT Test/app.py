from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt


def welcome():
    msg = QMessageBox()
    msg.setText('Добро пожаловать, ' + name.text() + ' ' + surname.text() )
    msg.exec()


app = QApplication([])
window = QWidget()
window.setWindowTitle('Тестовая программа')
window.resize(400, 400)

name = QLineEdit()
surname = QLineEdit()
button = QPushButton('Логин')
name_lbl = QLabel('Имя:')
surname_lbl = QLabel('Фамилия:')

button.clicked.connect(welcome)

h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
v_line = QVBoxLayout()

h_line_1.addWidget(name_lbl)
h_line_1.addWidget(name)
h_line_2.addWidget(surname_lbl)
h_line_2.addWidget(surname)

v_line.addLayout(h_line_1)
v_line.addLayout(h_line_2)
v_line.addWidget(button)

window.setLayout(v_line)

window.show()
app.exec()