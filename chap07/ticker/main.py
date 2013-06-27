#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ticker import Ticker
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ticker = Ticker()
    ticker.setWindowTitle(ticker.tr("Ticker"))
    ticker.setText(ticker.tr("How long it lasted was impossible to say ++ "))
    ticker.show()
    sys.exit(app.exec_())
