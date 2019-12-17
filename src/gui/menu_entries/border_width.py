from .imports import *

def border_width(master):
    label = QLabel('Border width')
    inp = QSpinBox()
    inp.setValue(master.config['border_width'])
    inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    inp.valueChanged.connect(partial(action, inp, master))
    master.settings.addRow(label, inp)

def action(inp, master):
    master.config['border_width'] = inp.value()
