from PyQt5.QtWidgets import QHBoxLayout, QWidget, QSizePolicy, QGroupBox, QFormLayout, QLineEdit, QLabel, QColorDialog, QCheckBox, QSpinBox, QComboBox

from .menu_sections import *


class Settings(QGroupBox):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('QGroupBox{border: none; border-radius: 10px;}')
        self.settings = QFormLayout(self)

        defLabel = QLabel('First row definiton')
        defInput = QLineEdit()
        defInput.setPlaceholderText('Layer definition')
        self.settings.addRow(defLabel, defInput)

        bgColorLabel = QLabel('Cell shape')
        bgColorInput = QComboBox()
        bgColorInput.addItem('Hexagon')
        bgColorInput.addItem('Square')
        bgColorInput.addItem('Circle')
        bgColorInput.addItem('Triangle')
        bgColorInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.settings.addRow(bgColorLabel, bgColorInput)

        bgColorLabel = QLabel('Background color')
        bgColorInput = QPushButton()
        bgColorInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bgColorInput.clicked.connect(self.getColor)
        self.settings.addRow(bgColorLabel, bgColorInput)

        bgColorLabel = QLabel('0 cell color')
        bgColorInput = QPushButton()
        bgColorInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bgColorInput.clicked.connect(self.getColor)
        bgColorTrans = QCheckBox()
        bgColorLayout = QHBoxLayout()
        bgColorLayout.addWidget(bgColorInput)
        bgColorLayout.addWidget(bgColorTrans)
        self.settings.addRow(bgColorLabel, bgColorLayout)

        bgColorLabel = QLabel('1 cell color')
        bgColorInput = QPushButton()
        bgColorInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bgColorInput.clicked.connect(self.getColor)
        bgColorTrans = QCheckBox()
        bgColorLayout = QHBoxLayout()
        bgColorLayout.addWidget(bgColorInput)
        bgColorLayout.addWidget(bgColorTrans)
        self.settings.addRow(bgColorLabel, bgColorLayout)

        bgColorLabel = QLabel('2 cell color')
        bgColorInput = QPushButton()
        bgColorInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bgColorInput.clicked.connect(self.getColor)
        bgColorTrans = QCheckBox()
        bgColorLayout = QHBoxLayout()
        bgColorLayout.addWidget(bgColorInput)
        bgColorLayout.addWidget(bgColorTrans)
        self.settings.addRow(bgColorLabel, bgColorLayout)

        bgColorLabel = QLabel('Border color')
        bgColorInput = QPushButton()
        bgColorInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        bgColorInput.clicked.connect(self.getColor)
        bgColorTrans = QCheckBox()
        bgColorLayout = QHBoxLayout()
        bgColorLayout.addWidget(bgColorInput)
        bgColorLayout.addWidget(bgColorTrans)
        self.settings.addRow(bgColorLabel, bgColorLayout)

        bgColorLabel = QLabel('Border width')
        bgColorInput = QSpinBox()
        bgColorInput.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.settings.addRow(bgColorLabel, bgColorInput)



    def getColor(self):
        color = QColorDialog.getColor()
