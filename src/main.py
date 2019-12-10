from PyQt5.QtWidgets import QApplication
from gui import Window

import sys

app = QApplication(sys.argv)

if __name__ == '__main__':
    win = Window()
    win.show()
    sys.exit(app.exec())
