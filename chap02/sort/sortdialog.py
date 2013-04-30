#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ui_sortdialog import Ui_SortDialog

"""
Implementing SortDialog with PyQt4
"""

class SortDialog(QDialog, Ui_SortDialog):

    def __init__(self, parent = None):
        QDialog.__init__(self, parent)

        self.setupUi(self)

        self.secondaryGroupBox.hide()
        self.tertiaryGroupBox.hide()
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        self.setColumnRange('A', 'Z')

    def setColumnRange(self, first, last):
        self.primaryColumnCombo.clear()
        self.secondaryColumnCombo.clear()
        self.tertiaryColumnCombo.clear()

        self.secondaryColumnCombo.addItem(self.tr("None"))
        self.tertiaryColumnCombo.addItem(self.tr("None"))

        self.primaryColumnCombo.setMinimumSize(self.secondaryColumnCombo.sizeHint())
    
        ch = first
        while ch <= last:
            self.primaryColumnCombo.addItem(QString(ch))
            self.secondaryColumnCombo.addItem(QString(ch))
            self.tertiaryColumnCombo.addItem(QString(ch))
            ch = unicode(ch, 'utf-8') # get the unicode of the char
            ch = chr(ord(ch) + 1) # ord() gets the int value of the char


