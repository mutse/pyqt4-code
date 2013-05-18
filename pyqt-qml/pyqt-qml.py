#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtDeclarative import QDeclarativeView

if __name__ == "__main__":
    app = QApplication(sys.argv)

    view = QDeclarativeView()
    view.setSource(QUrl('hello.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    view.show()

    sys.exit(app.exec_())

