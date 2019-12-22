from .imports import *

def x_shift(master):
    label = QLabel('X offset')
    inp = QSpinBox()
    inp.setMinimum(-1000)
    inp.setMaximum(1000)
    inp.setValue(master.config['x_shift'])
    inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    inp.valueChanged.connect(partial(action, inp, master))
    master.settings.addRow(label, inp)

def action(inp, master):
    master.config['x_shift'] = inp.value()
