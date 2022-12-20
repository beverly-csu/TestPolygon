from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QApplication, QWidget,
    QPushButton, QLabel, QListWidget, QFileDialog
)
import os

# Создание виджетов
app = QApplication([])
window = QWidget()
btn_open_dir = QPushButton('Открыть папку')
btn_rotate_left = QPushButton('Лево')
btn_rotate_right = QPushButton('Право')
btn_mirror = QPushButton('Отзеркалить')
btn_contrast = QPushButton('Резкость')
btn_black_white = QPushButton('Ч/Б')
image = QLabel('Тут должны быть картинка, но она потерялась')
image_list = QListWidget()

h_main = QHBoxLayout()
v_left = QVBoxLayout()
v_right = QVBoxLayout()
h_add = QHBoxLayout()
# Создание виджетов

# Размещение на layout'ах
h_add.addWidget(btn_rotate_left)
h_add.addWidget(btn_rotate_right)
h_add.addWidget(btn_mirror)
h_add.addWidget(btn_contrast)
h_add.addWidget(btn_black_white)

v_left.addWidget(btn_open_dir)
v_left.addWidget(image_list)

v_right.addWidget(image)
v_right.addLayout(h_add)

h_main.addLayout(v_left, stretch=2)
h_main.addLayout(v_right, stretch=6)
# Размещение на layout'ах

# Функции обработчики
workDir = ''

def chooseDir():
    current_dir = QFileDialog.getExistingDirectory(window)
    return current_dir

def showFiles():
    path = chooseDir()
    if len(path) > 0:
        global workDir
        workDir = path
        files = os.listdir(path)
        images = filter(files, ['.png', '.jpg', '.bpm', '.jpeg'])
        image_list.clear()
        image_list.addItems(images)

def filter(files, extensions):
    result = []
    for filename in files:
        for extension in extensions:
            if filename.endswith(extension):
                result.append(filename)
                break
    return result
# Функции обработчики

# Привязка кнопок
btn_open_dir.clicked.connect(showFiles)
# Привязка кнопок

# Настройка
window.resize(900, 600)
window.setWindowTitle('EasyEditor')
window.setLayout(h_main)
# Настройка

# Запуск приложения
window.show()
app.exec()
# Запуск приложения