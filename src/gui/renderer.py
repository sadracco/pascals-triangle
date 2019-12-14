from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygonF
from calc_utils import pascal, parse_layer_def


class Renderer(QWidget):
    def __init__(self):
        super(Renderer, self).__init__()
        self.qp = QPainter()
        self.size = 30

    def paintEvent(self, event):
        self.qp.begin(self)
        self.render_triangle(pascal(parse_layer_def(';6,r;')))
        self.qp.end()

    def draw_cell_rect(self, x, y, color):
        self.qp.setBrush(QBrush(color))
        self.qp.drawRect(x*self.size + y*(self.size/2), y*self.size, self.size, self.size)

    def draw_cell_hex(x,y,s,color):
        pass

    def render_triangle(self, triangle):
        for y, layer in enumerate(triangle):
            for x, cell in enumerate(layer):
                self.draw_cell_rect(x,y,QColor(255,0,0))
