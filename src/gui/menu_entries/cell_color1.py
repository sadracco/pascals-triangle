from .imports import *

def cell_color1(master):
    label = QLabel('1 cell color')
    inp = QPushButton()

    r,g,b,a = master.config['cell_color1']
    inp.setStyleSheet(f'background-color: rgba({r}, {g}, {b}, {a})')
    inp.setFocusPolicy(Qt.NoFocus)
    inp.setProperty('class', 'colorButton')

    inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    inp.clicked.connect(partial(action, inp, master))
    check_box = QCheckBox()
    check_box.setChecked(master.config['cell_hidden1'])
    check_box.stateChanged.connect(partial(cb_action, check_box, master))
    layout = QHBoxLayout()
    layout.addWidget(inp)
    layout.addWidget(check_box)
    master.settings.addRow(label, layout)

def action(inp, master):
    color = QColorDialog().getColor()
    inp.setStyleSheet(f'background-color: {color.name()}')
    master.config['cell_color1'] = color.getRgb()

def cb_action(inp, master):
    master.config['cell_hidden1'] = inp.isChecked()
