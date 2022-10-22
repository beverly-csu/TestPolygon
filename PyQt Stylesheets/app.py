from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QGroupBox
from PyQt5.QtWidgets import QPushButton, QLabel, QGroupBox, QRadioButton
import styles

# Создание экземпляра приложения
app = QApplication([])

# Создание окна и его первоначальная настройка заголовка и размеров
window = QWidget()
window.setWindowTitle('Тест стилей PyQt5')
window.resize(400, 400)

# Создание 2-ух кнопок
btn_exit = QPushButton('Выход')
btn_accept = QPushButton('Принять')

# Создание заголовка
lbl_title = QLabel('Заголовок')

# Создание GroupBox'a и кнопок (QRadioButton)
grpbox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')

# Создание горизонтальной направляющей и добавления на нее 2-ух кнопок (QRadioButton)
h_line_grpbox = QHBoxLayout()
h_line_grpbox.addWidget(rbtn_1)
h_line_grpbox.addWidget(rbtn_2)

# Установка для GroupBox'a ранее заготовленной направляющей
grpbox.setLayout(h_line_grpbox)

# Создание направляющих для окна
h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_3 = QHBoxLayout()
v_line = QVBoxLayout()

# Добавлении виджетов на направляющие
h_line_1.addWidget(lbl_title, alignment=Qt.AlignCenter)

h_line_2.addWidget(grpbox)

h_line_3.addStretch(2)
h_line_3.addWidget(btn_accept, stretch=4)
h_line_3.addStretch(1)
h_line_3.addWidget(btn_exit, stretch=4)
h_line_3.addStretch(2)

v_line.addLayout(h_line_1, stretch=1)
v_line.addLayout(h_line_2, stretch=4)
v_line.addLayout(h_line_3, stretch=2)

window.setLayout(v_line)

# Установка стилей для виджетов 
btn_accept.setStyleSheet(styles.button_accept)
btn_exit.setStyleSheet(styles.button_exit)
window.setStyleSheet(styles.window)
grpbox.setStyleSheet(styles.grpbox)
rbtn_1.setStyleSheet(styles.rbtn)

window.show()
app.exec()