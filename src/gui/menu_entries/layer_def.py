from .imports import *

def layer_def(master):
    label = QLabel('First row definiton')
    inp = QLineEdit()
    inp.setText(master.config['layer_def'])
    inp.textChanged.connect(partial(action, inp, master))
    inp.setPlaceholderText('Layer definition')
    master.settings.addRow(label, inp)

def action(inp, master):
    master.config['layer_def'] = inp.text()
