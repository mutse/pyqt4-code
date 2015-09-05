#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_gotocelldialog import Ui_GoToCellDialog

class GoToCellDialog(QDialog, Ui_GoToCellDialog):
    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi(self)

        regExp = QRegExp("[A-Za-z][1-9][0-9]{0,2}")
        regExpVal = QRegExpValidator(regExp, self)
        self.lineEdit.setValidator(regExpVal)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

    @pyqtSlot()
    def on_lineEdit_textChanged(self):
        self.okButton.setEnabled(self.lineEdit.hasAcceptableInput())

