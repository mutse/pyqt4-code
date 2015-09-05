#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_gotocelldialog import Ui_GoToCellDialog
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = Ui_GoToCellDialog()
    dialog = QDialog()
    ui.setupUi(dialog)
    dialog.show()

    sys.exit(app.exec_())

