from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor
from calc_utils import pascal, parse_layer_def


class Renderer(QWidget):
    def __init__(self):
        super(Renderer, self).__init__()
        self.qp = QPainter()

    def paintEvent(self, event):
        self.qp.begin(self)
        self.render_triangle(pascal(parse_layer_def(';6,r;')))
        self.qp.end()

    def draw_cell_rect(x,y,color):
        pass

    def draw_cell_hex(x,y,color):
        pass

    def render_triangle(self, triangle):
        for y, layer in enumerate(triangle):
            for x, cell in enumerate(layer):
                self.qp.setBrush(QBrush(QColor(120 * cell, 0,0)))
                self.qp.drawRect(20*x + 10*y, y*20, 20, 20)
