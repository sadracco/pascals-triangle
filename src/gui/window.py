from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QSizePolicy, QPushButton

from config import app_config
from .renderer import Renderer
from .settings import Settings


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(app_config['title'])
        self.setStyleSheet('background-color: black;')
        if app_config['fullscreen']:
            self.showMaximized()

        renderer = Renderer()
        settings = Settings()

        mainLayout = QHBoxLayout()
        settingsLayout = QVBoxLayout()

        settingsLayout.addWidget(settings, 1)
        settingsLayout.addWidget(QPushButton('Generate'), 2)

        mainLayout.setSpacing(10)
        mainLayout.addLayout(settingsLayout, 1)
        mainLayout.addWidget(renderer, 3)

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)

        self.setCentralWidget(mainWidget)
