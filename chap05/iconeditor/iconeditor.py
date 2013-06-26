#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class IconEditor(QWidget):

    def __init__(self, parent=None):
        super(IconEditor, self).__init__(parent)

        self.setAttribute(Qt.WA_StaticContents)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.curColor = Qt.black
        self.zoom = 8

        self.image = QImage(16, 16, QImage.Format_ARGB32)
        self.image.fill(qRgba(0, 0, 0, 0))

    def setPenColor(self, newColor):
        self.curColor = newColor;

    def penColor(self):
        return self.curColor

    def setZoomFactor(self, newZoom):
        if newZoom < 1:
            newZoom = 1

        if newZoom != self.zoom:
            self.zoom = newZoom
            self.update()
            self.updateGeometry()

    def zoomFactor(self):
        return self.zoom

    def setIconImage(self, newImage):
        if newImage != self.image:
            self.image = newImage.convertToFormat(QImage.Format_ARGB32)
            self.update()
            self.updateGeometry()

    def iconImage(self):
        return self.image

    def sizeHint(self):
        size = self.zoom * self.image.size()
        if self.zoom >= 3:
            size += QSize(1, 1)

        return size

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setImagePixel(event.pos(), True)
        elif event.button() == Qt.RightButton:
            self.setImagePixel(event.pos(), False)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.setImagePixel(event.pos(), True)
        elif event.buttons() & Qt.RightButton:
            self.etImagePixel(event.pos(), False)

    def paintEvent(self, event):
        painter = QPainter(self)

        if self.zoom >= 3:
            painter.setPen(self.palette().foreground().color())

            for i in range(0, self.image.width() + 1):
                painter.drawLine(self.zoom * i, 0, self.zoom * i, self.zoom * self.image.height())

            for j in range(0, self.image.height() + 1):
                painter.drawLine(0, self.zoom * j, self.zoom * self.image.width(), self.zoom * j)

        for i in range(0, self.image.width()):
            for j in range(0, self.image.height()):
                rect = self.pixelRect(i, j)
                if event.region().intersected(rect).isEmpty() == False:
                    color = QColor.fromRgba(self.image.pixel(i, j))
                    if color.alpha() < 255:
                        painter.fillRect(rect, Qt.white)
                    painter.fillRect(rect, color)

    def setImagePixel(self, pos, opaque):
        i = pos.x() / self.zoom
        j = pos.y() / self.zoom

        if self.image.rect().contains(i, j):
            if opaque:
                self.image.setPixel(i, j, self.penColor())
            else:
                self.image.setPixel(i, j, qRgba(0, 0, 0, 0))

            self.update(self.pixelRect(i, j))

    def pixelRect(self, i, j):
        if self.zoom >= 3:
            return QRect(self.zoom * i + 1, self.zoom * j + 1, self.zoom - 1, self.zoom - 1)
        else:
            return QRect(self.zoom * i, self.zoom * j, self.zoom, self.zoom)

    pyqtProperty(QColor, penColor, setPenColor)
    pyqtProperty(QImage, iconImage, setIconImage)                           
    pyqtProperty(int, zoomFactor, setZoomFactor)
