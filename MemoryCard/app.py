from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QRadioButton, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout, QButtonGroup
from PyQt5.QtCore import Qt
from random import shuffle
import style
import qrc


class Question:
    def __init__(self, title, right_answer, wrong1, wrong2, wrong3):
        self.title = title
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.create_widgets()
        self.setup_layout()
        self.setup_style()

        self.setWindowTitle('MemoryCard')
        # self.setWindowIcon(QIcon('img/icon.png'))
        self.setWindowIcon(QIcon(':/icons/main'))
        self.setFixedSize(400, 250)

        self.score = 0
        self.questions = self.read_questions('questions.txt')
        shuffle(self.questions)
        self.curr_index = 0

        self.setup_question()

    def setup_style(self):
        for btn in self.buttons:
            btn.setStyleSheet(style.rbtn)
        self.btn_ok.setStyleSheet(style.btn_ok)
        self.setStyleSheet(style.window)
        self.grpbox_answers.setStyleSheet(style.grpbox)
        self.grpbox_result.setStyleSheet(style.grpbox)

    def create_widgets(self):
        self.lbl_question = QLabel('Вопрос')
        self.btn_ok = QPushButton('Ответить')
        
        self.btn_ok.clicked.connect(self.button_handler)

        self.grpbox_answers = QGroupBox('Варианты ответов')
        self.grpbox_result = QGroupBox('Результат')

        self.grpbox_result.hide()

        self.lbl_result = QLabel()

        self.rbtn_1 = QRadioButton()
        self.rbtn_2 = QRadioButton()
        self.rbtn_3 = QRadioButton()
        self.rbtn_4 = QRadioButton()
        self.buttons = [self.rbtn_1, self.rbtn_2, self.rbtn_3, self.rbtn_4]

        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.rbtn_1)
        self.btn_group.addButton(self.rbtn_2)
        self.btn_group.addButton(self.rbtn_3)
        self.btn_group.addButton(self.rbtn_4)

    def setup_question(self):
        self.lbl_question.setText(self.questions[self.curr_index].title)
        shuffle(self.buttons)
        self.buttons[0].setText(self.questions[self.curr_index].right_answer)
        self.buttons[1].setText(self.questions[self.curr_index].wrong1)
        self.buttons[2].setText(self.questions[self.curr_index].wrong2)
        self.buttons[3].setText(self.questions[self.curr_index].wrong3)
        self.curr_index += 1

    def setup_layout(self):
        h_grpbox_answers = QHBoxLayout()
        v_grpbox_answers_1 = QVBoxLayout()
        v_grpbox_answers_2 = QVBoxLayout()

        v_grpbox_answers_1.addWidget(self.rbtn_1)
        v_grpbox_answers_1.addWidget(self.rbtn_2)
        v_grpbox_answers_2.addWidget(self.rbtn_3)
        v_grpbox_answers_2.addWidget(self.rbtn_4)

        h_grpbox_answers.addLayout(v_grpbox_answers_1)
        h_grpbox_answers.addLayout(v_grpbox_answers_2)

        self.grpbox_answers.setLayout(h_grpbox_answers)

        v_grpbox_result = QVBoxLayout()

        v_grpbox_result.addWidget(self.lbl_result, alignment=Qt.AlignCenter)

        self.grpbox_result.setLayout(v_grpbox_result)

        v_main = QVBoxLayout()
        h_main_1 = QHBoxLayout()
        h_main_2 = QHBoxLayout()
        h_main_3 = QHBoxLayout()

        h_main_1.addWidget(self.lbl_question, alignment=Qt.AlignCenter)
        h_main_2.addWidget(self.grpbox_answers)
        h_main_2.addWidget(self.grpbox_result)
        h_main_3.addWidget(self.btn_ok, alignment=Qt.AlignCenter)

        v_main.addLayout(h_main_1, stretch=1)
        v_main.addStretch(1)
        v_main.addLayout(h_main_2, stretch=10)
        v_main.addStretch(1)
        v_main.addLayout(h_main_3, stretch=1)

        self.setLayout(v_main)

    def read_questions(self, filename):
        result = list()
        with open(filename, 'r', encoding='utf-8') as fd:
            lines = fd.readlines()
        for i in range(len(lines) // 5):
            for_question = lines[i*5:i*5+5]
            for i in range(len(for_question)):
                for_question[i] = for_question[i].removesuffix('\n')
            result.append(Question(*for_question))
        return result

    def check_answer(self):
        if self.buttons[0].isChecked():
            return True
        else:
            return False

    def deactivate_buttons(self):
        self.btn_group.setExclusive(False)
        for button in self.buttons:
            button.setChecked(False)
        self.btn_group.setExclusive(True)

    def show_result(self):
        if self.curr_index == len(self.questions):
            self.btn_ok.setText('Узнать результат')
        else:
            self.btn_ok.setText('Следующий вопрос')
        self.grpbox_answers.hide()
        self.grpbox_result.show()
        if self.check_answer():
            result_text = 'Поздравляем! Вы ответили правильно!'
            self.score += 1
        else:
            result_text = 'К сожалению вы выбрали неверный ответ.\nПравильный ответ: ' + str(self.buttons[0].text())
        self.lbl_result.setText(result_text)
        self.deactivate_buttons()

    def show_answer(self):
        self.btn_ok.setText('Ответить')
        self.grpbox_answers.show()
        self.grpbox_result.hide()
        self.setup_question()

    def restart(self):
        self.curr_index = 0
        self.score = 0

    def show_final_result(self):
        result = round(self.score / len(self.questions) * 100, 2)
        result = 'Правильных ответов: ' + str(result) + '%'
        shuffle(self.questions)
        self.lbl_result.setText(result)
        self.btn_ok.setText('Начать заново')
        self.lbl_question.setText('')

    def button_handler(self):
        text = self.btn_ok.text()
        if text == 'Ответить':
            self.show_result()
        elif text == 'Узнать результат':
            self.show_final_result()
        elif text == 'Начать заново':
            self.restart()
            self.show_answer()
        else:
            self.show_answer()


app = QApplication([])
window = Window()
window.show()
app.exec()
