from PyQt5.QtWidgets import QGroupBox, QFormLayout

from .menu_entries import *


class Settings(QGroupBox):
    def __init__(self, config):
        super().__init__()

        self.config = config

        self.settings = QFormLayout(self)

        layer_def(self)
        cell_shape(self)
        cell_size(self)
        bg_color(self)
        cell_color0(self)
        cell_color1(self)
        cell_color2(self)
        border_color(self)
        border_width(self)
