#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QWidget();
    window.setWindowTitle("Enter Your Age")

    spinBox = QSpinBox();
    slider = QSlider(Qt.Horizontal)
    spinBox.setRange(0, 130)
    slider.setRange(0, 130)

    spinBox.valueChanged.connect(slider.setValue)
    slider.valueChanged.connect(spinBox.setValue)
    spinBox.setValue(35)

    layout = QHBoxLayout()
    layout.addWidget(spinBox)
    layout.addWidget(slider)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec_())

