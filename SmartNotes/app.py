from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QListWidget,
    QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout
)
import json

# Создание виджетов
app = QApplication([])
window = QWidget()

note_field = QTextEdit()
lbl_notes = QLabel('Список заметок')
list_notes = QListWidget()

btn_note_create = QPushButton('Создать заметку')
btn_note_delete = QPushButton('Удалить заметку')
btn_note_save = QPushButton('Сохранить заметку')

lbl_tags = QLabel('Список тегов')
list_tags = QListWidget()
field_tag = QLineEdit()

btn_tag_add = QPushButton('Добавить к заметке')
btn_tag_remove = QPushButton('Открепить к заметке')
btn_tag_search = QPushButton('Искать заметки по тегу')
# Создание виджетов

# Создание лэйаутов
h_main = QHBoxLayout()
left_side = QVBoxLayout()
right_side = QVBoxLayout()

h1 = QHBoxLayout()
h2 = QHBoxLayout()
h3 = QHBoxLayout()
h4 = QHBoxLayout()
h5 = QHBoxLayout()
h6 = QHBoxLayout()
h7 = QHBoxLayout()
h8 = QHBoxLayout()
h9 = QHBoxLayout()
# Создание лэйаутов

# Размещение виджетов на лэйаутах
h1.addWidget(lbl_notes)
h2.addWidget(list_notes)
h3.addWidget(btn_note_create)
h3.addWidget(btn_note_delete)
h4.addWidget(btn_note_save)
h5.addWidget(lbl_tags)
h6.addWidget(list_tags)
h7.addWidget(field_tag)
h8.addWidget(btn_tag_add)
h8.addWidget(btn_tag_remove)
h9.addWidget(btn_tag_search)

right_side.addLayout(h1)
right_side.addLayout(h2)
right_side.addLayout(h3)
right_side.addLayout(h4)
right_side.addLayout(h5)
right_side.addLayout(h6)
right_side.addLayout(h7)
right_side.addLayout(h8)
right_side.addLayout(h9)

left_side.addWidget(note_field)

h_main.addLayout(left_side)
h_main.addLayout(right_side)
# Размещение виджетов на лэйаутах

# Настройка приложения
window.setWindowTitle('Умные заметки')
window.resize(900, 600)
field_tag.setPlaceholderText('Введите тег...')
window.setLayout(h_main)
# Настройка приложения

# Функции
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
        list_notes.addItems(notes)
        return notes
    except:
        notes = {
            'Приветственная заметка': {
                'text': 'Это первая ваша заметка в программе!',
                'tags': ['начало работы', 'первый запуск']
            }
        }
        with open('notes.json', 'w') as file:
            json.dump(notes, file)
        list_notes.addItems(notes)
        return notes

def add_note():
    note_name, ok = QInputDialog.getText(window, 'Добавить заметку', 'Название заметки: ')
    if ok and len(note_name) > 0:
        notes[note_name] = {'text': '', 'tags': []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['tags'])

def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['text'] = note_field.toPlainText()
        with open('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)

def show_note():
    key = list_notes.selectedItems()[0].text()
    note_field.setText(notes[key]['text'])
    list_tags.clear()
    list_tags.addItems(notes[key]['tags'])

def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        note_field.clear()
        list_notes.addItems(notes)
        with open('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)

def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]['tags'] and len(tag) > 0:
            notes[key]['tags'].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
            with open('notes.json', 'w') as file:
                json.dump(notes, file, sort_keys=True)

def remove_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['tags'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['tags'])
        with open('notes.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)

def search_by_tag():
    tag = field_tag.text()
    if btn_tag_search.text() != 'Сбросить поиск' and len(tag) > 0:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]['tags']:
                notes_filtered[note] = notes[note]
        list_notes.clear()
        list_tags.clear()
        note_field.clear()
        list_notes.addItems(notes_filtered)
        btn_tag_search.setText('Сбросить поиск')
    else:
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        note_field.clear()
        list_notes.addItems(notes)
        btn_tag_search.setText('Искать заметки по тегу')
# Функции

# Обработка событий
btn_note_create.clicked.connect(add_note)
btn_note_save.clicked.connect(save_note)
btn_note_delete.clicked.connect(del_note)
btn_tag_add.clicked.connect(add_tag)
btn_tag_remove.clicked.connect(remove_tag)
btn_tag_search.clicked.connect(search_by_tag)
list_notes.itemClicked.connect(show_note)
# Обработка событий

# Запуск приложения
notes = load_notes()
window.show()
app.exec()
# Запуск приложения