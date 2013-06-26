#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from iconeditor import IconEditor
import iconeditor_qrc
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    iconEditor = IconEditor()
    iconEditor.setWindowTitle(iconEditor.tr("Icon Editor"))
    iconEditor.setIconImage(QImage(":/images/mouse.png"))
    iconEditor.show()
    sys.exit(app.exec_())
