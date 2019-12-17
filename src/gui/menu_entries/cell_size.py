from .imports import *

def cell_size(master):
    label = QLabel('Cell size')
    inp = QSpinBox()
    inp.setValue(master.config['cell_size'])
    inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    inp.valueChanged.connect(partial(action, inp, master))
    master.settings.addRow(label, inp)

def action(inp, master):
    master.config['cell_size'] = inp.value()
