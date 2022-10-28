from PyQt5.QtWidgets import (QApplication, QWidget, QButtonGroup, QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QSizePolicy)
from PyQt5.QtCore import Qt, QTimer
import core
import random
import sys


class Block(QLabel):
    def __init__(self, start_text='2', i=0, j=0):
        super().__init__()
        self.i, self.j = i, j
        self.setText(start_text)
        self.setAlignment(Qt.AlignCenter)
        style = '''
        border-radius: 10%;
        font-size: 16px;
        font-weight: 600;
        font-family: "Arial";
        '''
        self.setStyleSheet(style)
        self.setMinimumSize(50, 50)


class TestWindow(QWidget):
    def __init__(self, size=4):
        super().__init__()
        self.size = size
        self.layout = self.init_blocks(size)
        self.setLayout(self.layout)

    def init_blocks(self, size):
        layout = QGridLayout()
        self.blocks = []
        self.matrix = core.create_null_matrix(self.size)
        for i in range(1, size + 1):
            line = []
            for j in range(1, size + 1):
                block = Block('', i - 1, j - 1)
                layout.addWidget(block, i, j)
                line.append(block)
            self.blocks.append(line)
        return layout

    def start_game(self):
        blocks = self.findChildren(Block)
        ids = random.sample(range(0, len(blocks)), 2)
        for i, block in enumerate(blocks):
            if i in ids:
                self.matrix[i // self.size][i % self.size] = 2
                block.setText('2')
            else:
                block.setText('')

    def resizeEvent(self, event):
        if self.width() > self.height():
            self.resize(self.width(), self.width())
        else:
            self.resize(self.height(), self.height())

    def new_block(self):
        while True:
            block = random.choice(self.findChildren(Block))
            if self.matrix[block.i][block.j] == 0:
                self.matrix[block.i][block.j] = random.choices([2, 4], [0.7, 0.3])[0]
                break

    def update_blocks(self):
        for i in range(self.size):
            for j in range(self.size):
                text = '' if self.matrix[i][j] == 0 else str(self.matrix[i][j])
                self.blocks[i][j].setText(text)
                self.blocks[i][j].setStyleSheet('''
                border-radius: 10%;
                font-size: 16px;
                font-weight: 600;
                font-family: "Arial";
                background-color: #ffd866;
                ''')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_R:
            self.start_game()
        elif event.key() == Qt.Key_Left:
            self.matrix = core.left(self.matrix)
        elif event.key() == Qt.Key_Right:
            self.matrix = core.right(self.matrix)
        elif event.key() == Qt.Key_Up:
            self.matrix = core.up(self.matrix)
        elif event.key() == Qt.Key_Down:
            self.matrix = core.down(self.matrix)
        self.new_block()
        self.update_blocks()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TestWindow()
    window.start_game()
    window.show()
    sys.exit(app.exec())
