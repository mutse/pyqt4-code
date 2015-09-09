#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class HexSpinBox(QSpinBox):

    def __init__(self, parent = None):
        QSpinBox.__init__(self, parent)

        self.setRange(0, 255)
        self.validator = QRegExpValidator(QRegExp("[0-9A-Fa-f]{1,8}"), self)

    def validate(self, text, pos):
        return self.validator.validate(text, pos)

    def valueFromText(self, text):
        n, ok = text.toInt(16)
        return n

    def textFromValue(self, value):
        return QString.number(value, 16).toUpper()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    spinBox = HexSpinBox()
    spinBox.setWindowTitle("Hex Spin Box")
    spinBox.resize(200, 30)
    spinBox.show()
    sys.exit(app.exec_())
