#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from sortdialog import SortDialog
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dialog = SortDialog()
    dialog.setColumnRange('C', 'F')
    dialog.show()

    sys.exit(app.exec_())

