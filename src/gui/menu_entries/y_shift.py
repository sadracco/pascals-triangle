from .imports import *

def y_shift(master):
    label = QLabel('Y offset')
    inp = QSpinBox()
    inp.setMinimum(-1000)
    inp.setMaximum(1000)
    inp.setValue(master.config['y_shift'])
    inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    inp.valueChanged.connect(partial(action, inp, master))
    master.settings.addRow(label, inp)

def action(inp, master):
    master.config['y_shift'] = inp.value()
