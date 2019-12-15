from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QColorDialog, QWidget, QFormLayout
from PyQt5.QtCore import pyqtSlot


class ColorsSec(QFormLayout):
    def __init__(self):
        super().__init__()
        button.clicked.connect(self.on_click)
        self.layout.addWidget(button)
        self.show()

    @pyqtSlot()
    def on_click(self):
        self.openColorDialog()

    def openColorDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            print(color.name())

