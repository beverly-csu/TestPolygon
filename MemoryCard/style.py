rbtn = '''
QRadioButton::indicator {
    width: 20px;
    height: 20px;
}

QRadioButton::indicator::unchecked {
    image: url(:/icons/unchecked);
}

QRadioButton::indicator:unchecked:hover {
    image: url(:/icons/unchecked-hover);
}

QRadioButton::indicator:unchecked:pressed {
    image: url(:/icons/unchecked-pressed);
}

QRadioButton::indicator::checked {
   image: url(:/icons/checked);
}

QRadioButton::indicator:checked:hover {
    image: url(:/icons/checked-hover);
}

QRadioButton::indicator:checked:pressed {
    image: url(:/icons/checked-pressed);
}
'''


btn_ok = '''
QPushButton {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(181, 96, 113, 255), stop:1 rgba(255, 187, 99, 255));
    padding: 10% 2% 10% 2%;
    border-radius: 5px;
    width: 150%;
    color: #262626;
}

QPushButton:hover {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(156, 83, 97, 255), stop:1 rgba(255, 187, 99, 255));
}

QPushButton:pressed {
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(140, 74, 87, 255), stop:1 rgba(232, 170, 90, 255))
}
'''

grpbox = '''
QGroupBox {
    border: 2px solid #C9C9C9;
    border-radius: 5px;
}
'''

window = '''
QWidget {
    background-color: #282828;
    font-size: 14px;
    color: #C9C9C9;
}
'''