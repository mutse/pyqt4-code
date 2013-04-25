#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    button = QPushButton("Quit")
    button.clicked.connect(app.quit)
    button.show()

    sys.exit(app.exec_())

