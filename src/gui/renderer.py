from PyQt5.QtWidgets import QFrame, QSizePolicy
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygonF, QPen
from PyQt5.QtCore import QPointF

from calc_utils import pascal, parse_layer_def, get_hex

from math import sqrt


class Renderer(QFrame):
    def __init__(self):
        super(Renderer, self).__init__()
        self.setStyleSheet('background-color: white; border-radius: 10px;')
        self.setMinimumSize(200, 200)
        self.qp = QPainter()
        self.size = 40
        self.colors = (
                QColor(255,0,0),
                QColor(255,255,0),
                QColor(0,0,255),
                )

    def paintEvent(self, event):
        self.qp.begin(self)
        self.qp.setRenderHint(QPainter.Antialiasing)
        w = self.frameGeometry().width()
        h = self.frameGeometry().height()
        # self.qp.fillRect(0,0,w,h,QColor(255,255,255))
        self.render_triangle(pascal(parse_layer_def('10,r')))
        self.qp.end()

    def draw_hex(self, x, y, cX, cY, verts, h, ys, color):
        self.qp.setBrush(QBrush(color))
        self.qp.setPen(QPen(QColor(0,0,0), 8))
        poly = QPolygonF()
        for a,b in verts:
            poly.append(QPointF(
                cX + a + (x*h*2) + (y*h),
                cY + b + ys * y
                ))
        self.qp.drawPolygon(poly)

    def render_triangle(self, triangle):
        verts,h = get_hex(self.size)
        ys = sqrt((2*h)**2 - h**2)
        sw = h*2*len(triangle)
        sh = sqrt(3)/2*sw
        cX = self.frameGeometry().width()/2 - sw/2 + h
        cY = self.frameGeometry().height()/2 - sh/2 + self.size
        for y, layer in enumerate(triangle):
            for x, cell in enumerate(layer):
                self.draw_hex(x,y,cX,cY,verts,h,ys,self.colors[cell%3])
