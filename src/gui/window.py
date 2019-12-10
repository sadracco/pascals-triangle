from PyQt5.QtWidgets import QMainWindow

from config import app_config
from .renderer import Renderer


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(app_config['title'])
        if app_config['fullscreen']:
            self.showMaximized()

        self.renderer = Renderer()
        self.setCentralWidget(self.renderer)
