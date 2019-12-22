from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QVBoxLayout, QSizePolicy, QPushButton
from PyQt5.QtCore import Qt

from config import app_config, triangle_config
from .renderer import Renderer
from .settings import Settings

from functools import partial


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle(app_config['title'])

        if app_config['fullscreen']:
            self.showMaximized()

        renderer = Renderer(triangle_config)
        settings = Settings(triangle_config)

        mainLayout = QHBoxLayout()
        settingsLayout = QVBoxLayout()
        bottomLayout = QHBoxLayout()

        settingsLayout.addWidget(settings, 1)

        saveButton = QPushButton('Save')
        saveButton.setFocusPolicy(Qt.NoFocus)
        saveButton.clicked.connect(renderer.saveImage)
        bottomLayout.addWidget(saveButton, 1)

        generateButton = QPushButton('Generate')
        generateButton.setFocusPolicy(Qt.NoFocus)
        generateButton.clicked.connect(partial(renderer.generate, settings.config))
        bottomLayout.addWidget(generateButton, 3)


        settingsLayout.addLayout(bottomLayout, 2)

        mainLayout.addLayout(settingsLayout, 1)
        mainLayout.addWidget(renderer, 3)

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)

        self.setCentralWidget(mainWidget)
