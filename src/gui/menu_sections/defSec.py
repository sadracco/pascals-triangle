from PyQt5.QtWidgets import QFormLayout, QLineEdit, QLabel
from PyQt5.QtCore import pyqtSlot


class DefSec(QFormLayout):
    def __init__(self):
        super().__init__()

        defLabel = QLabel('First row definiton:')
        defInput = QLineEdit()
        self.addRow(defLabel, defInput)
