#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_gotocelldialog import Ui_GoToCellDialog

class GoToCellDialog(QDialog, Ui_GoToCellDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi(self)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)

        regExp = QRegExp("[A-Za-z][1-9][0-9]{0,2}")
        self.lineEdit.setValidator(QRegExpValidator(regExp, self))

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

    @pyqtSlot()
    def on_lineEdit_textChanged(self):
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(
            self.lineEdit.hasAcceptableInput())
