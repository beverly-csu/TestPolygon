button_accept = '''
QPushButton {
    background: transparent;
    color: #14d935;
    border: 2px solid #14d935;
    border-radius: 8%;
    padding: 7% 1% 7% 1%;
}

QPushButton:hover {
    border: 2px solid #1d9631;
    color: #1d9631;
}
'''

button_exit = '''
QPushButton {
    background: transparent;
    color: #d11a1a;
    border: 2px solid #d11a1a;
    border-radius: 8%;
    padding: 7% 1% 7% 1%;
}

QPushButton:hover {
    border: 2px solid #9e1f1f;
    color: #9e1f1f;
}
'''

window = '''
QWidget {
    background-color: #232323;
    font-family: Roboto;
    font: 14px "Arial";
    color: #F0F0F0;
}
'''

grpbox = '''
QGroupBox {
    border: 2px solid #a1a1a1;
    border-radius: 8%;    
}
'''


rbtn = '''
QRadioButton::indicator {
    width: 13px;
    height: 13px;
}

QRadioButton::indicator::unchecked {
    image: url(images/1.png);
}

QRadioButton::indicator:unchecked:hover {
    image: url(images/1.png);
}

QRadioButton::indicator:unchecked:pressed {
    image: url(images/1.png);
}

QRadioButton::indicator::checked {
    image: url(images/1.png);
}

QRadioButton::indicator:checked:hover {
    image: url(images/1.png);
}

QRadioButton::indicator:checked:pressed {
    image: url(images/1.png);
}
'''