from .imports import *

def bg_color(master):
    label = QLabel('Background color')
    inp = QPushButton()

    r,g,b,a = master.config['bg_color']
    inp.setStyleSheet(f'background-color: rgba({r}, {g}, {b}, {a})')

    inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    inp.setFocusPolicy(Qt.NoFocus)
    inp.setProperty('class', 'colorButton')
    inp.clicked.connect(partial(action, inp, master))
    master.settings.addRow(label, inp)

def action(inp, master):
    color = QColorDialog().getColor()
    inp.setStyleSheet(f'background-color: {color.name()}')
    master.config['bg_color'] = color.getRgb()
