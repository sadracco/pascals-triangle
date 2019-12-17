from PyQt5.QtWidgets import QFrame, QSizePolicy, QFileDialog
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygonF, QPen, QPixmap
from PyQt5.QtCore import QPointF

from calc_utils import pascal, parse_layer_def, get_hex

from math import sqrt


class Renderer(QFrame):
    def __init__(self, conf):
        super(Renderer, self).__init__()
        self.setMinimumSize(200, 200)
        self.qp = QPainter()

        self.size = 40
        self.colors = [
                QColor(255,0,0),
                QColor(255,255,0),
                QColor(0,0,255),
                ]

        self.generate(conf)

    def paintEvent(self, event):
        self.qp.begin(self)
        self.qp.setRenderHint(QPainter.Antialiasing)
        self.render_triangle()
        self.qp.end()

    def saveImage(self):
        x = self.frameGeometry().width()
        y = self.frameGeometry().height()
        pixmap = QPixmap(x,y)
        self.render(pixmap)
        pixmap.save(QFileDialog.getSaveFileName()[0])

    def generate(self, conf):
        self.triangle = pascal(parse_layer_def(conf['layer_def']))

        r,g,b,a = conf['cell_color0']
        if conf['cell_hidden0']: a = 0
        self.colors[0] = QColor(r,g,b,a)
        r,g,b,a = conf['cell_color1']
        if conf['cell_hidden1']: a = 0
        self.colors[1] = QColor(r,g,b,a)
        r,g,b,a = conf['cell_color2']
        if conf['cell_hidden2']: a = 0
        self.colors[2] = QColor(r,g,b,a)

        self.size = conf['cell_size']

        r,g,b,_ = conf['bg_color']
        self.setStyleSheet(f'background-color: rgb({r},{g},{b}); border-radius: 10px')

        self.border_width = conf['border_width']

        r,g,b,a = conf['border_color']
        if conf['border_hidden']:
            r,g,b,a = conf['bg_color']
        self.border_color = QColor(r,g,b,a)

        self.update()

    def draw_hex(self, x, y, cX, cY, verts, h, ys, color):
        self.qp.setBrush(QBrush(color))
        self.qp.setPen(QPen(self.border_color, self.border_width))
        poly = QPolygonF()
        for a,b in verts:
            poly.append(QPointF(
                cX + a + (x*h*2) + (y*h),
                cY + b + ys * y
                ))
        self.qp.drawPolygon(poly)

    def render_triangle(self):
        verts,h = get_hex(self.size)
        ys = sqrt((2*h)**2 - h**2)
        sw = h*2*len(self.triangle)
        sh = sqrt(3)/2*sw
        cX = self.frameGeometry().width()/2 - sw/2 + h
        cY = self.frameGeometry().height()/2 - sh/2 + self.size
        for y, layer in enumerate(self.triangle):
            for x, cell in enumerate(layer):
                self.draw_hex(x,y,cX,cY,verts,h,ys,self.colors[cell%3])
