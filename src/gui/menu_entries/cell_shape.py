from .imports import *

def cell_shape(master):
    label = QLabel('Cell shape')
    inp = QComboBox()
    inp.setFocusPolicy(Qt.NoFocus)
    inp.addItem('Hexagon')
    inp.addItem('Square')
    inp.addItem('Circle')
    inp.addItem('Triangle')
    inp.setCurrentIndex(master.config['cell_shape'])
    inp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    inp.currentIndexChanged.connect(partial(action, inp, master))
    master.settings.addRow(label, inp)

def action(inp, master):
    master.config['cell_shape'] = inp.currentIndex()
