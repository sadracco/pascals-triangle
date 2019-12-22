from PyQt5.QtWidgets import QFrame, QSizePolicy, QFileDialog
from PyQt5.QtGui import QPainter, QBrush, QColor, QPolygonF, QPen, QPixmap
from PyQt5.QtCore import QPointF, Qt

from calc_utils import pascal, parse_layer_def, get_hex

from math import sqrt


class Renderer(QFrame):
    def __init__(self, conf):
        super(Renderer, self).__init__()
        self.setMinimumSize(200, 200)
        self.qp = QPainter()

        self.render_functions = (
                self.render_hex,
                self.render_box,
                self.render_circle
                )

        self.render_func_index = 0

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
        self.render_functions[self.render_func_index]()
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

        self.render_func_index = conf['cell_shape']

        self.x_shift = conf['x_shift']
        self.y_shift = conf['y_shift']

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

    def render_hex(self):
        verts,h = get_hex(self.size)
        ys = sqrt((2*h)**2 - h**2)
        sw = h*2*len(self.triangle)
        sh = sqrt(3)/2*sw
        cX = self.frameGeometry().width()/2 - sw/2 + h
        cY = self.frameGeometry().height()/2 - sh/2 + self.size
        for y, layer in enumerate(self.triangle):
            for x, cell in enumerate(layer):
                self.draw_hex(x,y,cX+self.x_shift,cY-self.y_shift,verts,h,ys,self.colors[cell%3])

    def draw_box(self, x, y, cX, cY, verts, h, ys, color):
        self.qp.setBrush(QBrush(color))
        pen = QPen()
        pen.setColor(self.border_color)
        pen.setWidth(self.border_width)
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        self.qp.setPen(pen)
        poly = QPolygonF()
        boxPoints = []
        for a,b in verts:
            i = cX + a + (x*h*2) + (y*h)
            j = cY + b + ys * y
            poly.append(QPointF(i,j))
            boxPoints.append((i,j))
        self.qp.drawPolygon(poly)

        x = cX + x*h*2 + (y*h)
        y = cY + ys * y
        xx, yy = boxPoints[1]
        self.qp.drawLine(x,y, xx,yy)
        xx, yy = boxPoints[3]
        self.qp.drawLine(x,y, xx,yy)
        xx, yy = boxPoints[5]
        self.qp.drawLine(x,y, xx,yy)

    def render_box(self):
        verts,h = get_hex(self.size)
        ys = sqrt((2*h)**2 - h**2)
        sw = h*2*len(self.triangle)
        sh = sqrt(3)/2*sw
        cX = self.frameGeometry().width()/2 - sw/2 + h
        cY = self.frameGeometry().height()/2 - sh/2 + self.size
        for y, layer in enumerate(self.triangle):
            for x, cell in enumerate(layer):
                self.draw_box(x,y,cX+self.x_shift,cY-self.y_shift,verts,h,ys,self.colors[cell%3])

    def draw_circle(self, x, y, cX, cY, h, ys, color):
        self.qp.setBrush(QBrush(color))
        self.qp.setPen(QPen(self.border_color, self.border_width))
        c_x = cX + x*h*2 + (y*h)
        c_y = cY + ys * y
        self.qp.drawEllipse(c_x,c_y,h*2,h*2)

    def render_circle(self):
        _,h = get_hex(self.size)
        ys = sqrt((2*h)**2 - h**2)
        sw = h*2*len(self.triangle)
        sh = sqrt(3)/2*sw
        cX = self.frameGeometry().width()/2 - sw/2 + h
        cY = self.frameGeometry().height()/2 - sh/2 + h
        for y, layer in enumerate(self.triangle):
            for x, cell in enumerate(layer):
                self.draw_circle(x,y,cX+self.x_shift,cY-self.y_shift,h,ys,self.colors[cell%3])
