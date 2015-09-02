#!/usr/bin/python
# -*- coding:  utf-8 -*-

"""
Mutse PyQt4 code

author: mutse <yyhoo2.young@gmail.com>
website: http://mutse.github.io
last edited: September 2th, 2015
"""

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import math

M_PI = 3.14159265359
DegreesPerMinute = 7.0
DegreesPerSecond = DegreesPerMinute / 60
MaxMinutes = 45
MaxSeconds = MaxMinutes * 60
UpdateInterval = 5

class OvenTimer(QWidget):

    timeout = pyqtSignal()

    def __init__(self):
        super(OvenTimer, self).__init__()

        self.finishTime = QDateTime.currentDateTime()

        self.updateTimer = QTimer(self)
        self.updateTimer.timeout.connect(self.update)

        self.finishTimer = QTimer(self)
        self.finishTimer.setSingleShot(True)
        self.finishTimer.timeout.connect(self.timeout)
        self.finishTimer.timeout.connect(self.finishTimer.stop)
        font = QFont()
        font.setPointSize(8)
        self.setFont(font)

    def setDuration(self, secs):
        secs = self.qBound(0, secs, MaxSeconds)

        self.finishTime = QDateTime().currentDateTime().addSecs(secs)

        if secs > 0:
            self.updateTimer.start(UpdateInterval * 1000)
            self.finishTimer.start(secs * 1000)
        else:
            self.updateTimer.stop()
            self.finishTimer.stop()

        self.update()

    def qBound(self, minVal, current, maxVal):
        return max(min(current, maxVal), minVal)

    def duration(self):
        secs = QDateTime().currentDateTime().secsTo(self.finishTime)
        if secs < 0:
            secs = 0

        return secs

    def mousePressEvent(self, event):
        point = event.pos() - self.rect().center()
        theta = math.atan2(-point.x(), -point.y()) * 180.0 / M_PI
        self.setDuration(self.duration() + int(theta / DegreesPerSecond))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)

        side = min(self.width(), self.height())
        painter.setViewport((self.width() - side) / 2, (self.height() - side) / 2, side, side)
        painter.setWindow(-50, -50, 100, 100)

        self.draw(painter)

    def draw(self, painter):
        thickPen = QPen(self.palette().foreground(), 1.5)
        thinPen = QPen(self.palette().foreground(), 0.5)
        niceBlue = QColor(150, 150, 200)

        painter.setPen(thinPen)
        painter.setBrush(self.palette().foreground())
        painter.drawPolygon(QPolygon([QPoint(-2, -49), QPoint(2, -49), QPoint(0, -47)]))

        coneGradient = QConicalGradient(0, 0, -90.0)
        coneGradient.setColorAt(0.0, Qt.darkGray)
        coneGradient.setColorAt(0.2, niceBlue)
        coneGradient.setColorAt(0.5, Qt.white)
        coneGradient.setColorAt(1.0, Qt.darkGray);

        painter.setBrush(coneGradient)
        painter.drawEllipse(-46, -46, 92, 92)
        haloGradient = QRadialGradient(0, 0, 20, 0, 0)
        haloGradient.setColorAt(0.0, Qt.lightGray)
        haloGradient.setColorAt(0.8, Qt.darkGray)
        haloGradient.setColorAt(0.9, Qt.white)
        haloGradient.setColorAt(1.0, Qt.black)

        painter.setPen(Qt.NoPen)
        painter.setBrush(haloGradient)
        painter.drawEllipse(-20, -20, 40, 40)

        knobGradient = QLinearGradient(-7, -25, 7, -25)
        knobGradient.setColorAt(0.0, Qt.black)
        knobGradient.setColorAt(0.2, niceBlue)
        knobGradient.setColorAt(0.3, Qt.lightGray)
        knobGradient.setColorAt(0.8, Qt.white)
        knobGradient.setColorAt(1.0, Qt.black)

        painter.rotate(self.duration() * DegreesPerSecond)
        painter.setBrush(knobGradient)
        painter.setPen(thinPen)
        painter.drawRoundRect(-7, -25, 14, 50, 99, 49)

        for i in range(0, MaxMinutes):
            if i % 5 == 0:
                painter.setPen(thickPen)
                painter.drawLine(0, -41, 0, -44)
                painter.drawText(-15, -41, 30, 30, Qt.AlignHCenter | Qt.AlignTop, QString().number(i))
            else:
                painter.setPen(thinPen)
                painter.drawLine(0, -42, 0, -44)

            painter.rotate(-DegreesPerMinute)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ovenTimer = OvenTimer()
    ovenTimer.setWindowTitle("Oven Timer")
    ovenTimer.resize(300, 300)
    ovenTimer.show()
    sys.exit(app.exec_())

