from .imports import *

def border_color(master):
    label = QLabel('Border color')
    inp = QPushButton()

    r,g,b,a = master.config['border_color']
    inp.setStyleSheet(f'background-color: rgba({r}, {g}, {b}, {a})')
    inp.setFocusPolicy(Qt.NoFocus)
    inp.setProperty('class', 'colorButton')

    inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    inp.clicked.connect(partial(action, inp, master))
    check_box = QCheckBox()
    check_box.setChecked(master.config['border_hidden'])
    check_box.stateChanged.connect(partial(cb_action, check_box, master))
    layout = QHBoxLayout()
    layout.addWidget(inp)
    layout.addWidget(check_box)
    master.settings.addRow(label, layout)

def action(inp, master):
    color = QColorDialog().getColor()
    inp.setStyleSheet(f'background-color: {color.name()}')
    master.config['border_color'] = color.getRgb()

def cb_action(inp, master):
    master.config['border_hidden'] = inp.isChecked()
