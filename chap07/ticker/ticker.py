#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Ticker(QWidget):

    def __init__(self, parent=None):
        super(Ticker, self).__init__(parent)
        self.offset = 0
        self.myTimerId = 0
        self.myText = ""

    def setText(self, newText):
        self.myText = newText
        self.update()
        self.updateGeometry()

    def text(self):
        return self.myText

    def sizeHint(self):
        return self.fontMetrics().size(0, self.text())

    def paintEvent(self, event):
        painter = QPainter(self)

        textWidth = self.fontMetrics().width(self.text())
        if textWidth < 1:
            return

        x = -self.offset
        while x < self.width():
            painter.drawText(x, 0, textWidth, self.height(), Qt.AlignLeft | Qt.AlignVCenter, self.text())
            x += textWidth

    def showEvent(self, event):
        self.myTimerId = self.startTimer(30)

    def timerEvent(self, event):
        if event.timerId() == self.myTimerId:
            ++self.offset
            if self.offset >= self.fontMetrics().width(self.text()):
                self.offset = 0
            self.scroll(-1, 0)
        else:
            QWidget.timerEvent(event)

    def hideEvent(self, event):
        self.killTimer(self.myTimerId)
        self.myTimerId = 0

    pyqtProperty(str, text, setText)
