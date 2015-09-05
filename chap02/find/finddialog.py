#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Implementing FindDialog with PyQt4
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class FindDialog(QDialog):

    """
    customized signals definition
    """
    findNext = pyqtSignal(str, int)
    findPrevious = pyqtSignal(str, int)

    def __init__(self, parent = None):
        super(FindDialog, self).__init__(parent)

        label = QLabel(self.tr("Find &what:"))
        self.lineEdit = QLineEdit()
        label.setBuddy(self.lineEdit)

        self.caseCheckBox = QCheckBox(self.tr("Match &case"))
        self.backwardCheckBox = QCheckBox(self.tr("Search &backward"))

        self.findButton = QPushButton(self.tr("&Find"))
        self.findButton.setDefault(True)
        self.findButton.setEnabled(False)

        closeButton = QPushButton(self.tr("Close"))

        self.lineEdit.textChanged.connect(self.enableFindButton)
        self.findButton.clicked.connect(self.findClicked)
        closeButton.clicked.connect(self.close)

        topLeftLayout = QHBoxLayout()
        topLeftLayout.addWidget(label)
        topLeftLayout.addWidget(self.lineEdit)

        leftLayout = QVBoxLayout()
        leftLayout.addLayout(topLeftLayout)
        leftLayout.addWidget(self.caseCheckBox)
        leftLayout.addWidget(self.backwardCheckBox)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.findButton)
        rightLayout.addWidget(closeButton)
        rightLayout.addStretch()

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(leftLayout)
        mainLayout.addLayout(rightLayout)
        self.setLayout(mainLayout)

        self.setWindowTitle(self.tr("Find"))
        self.setFixedHeight(self.sizeHint().height())

    def findClicked(self):
        text = self.lineEdit.text()
        if self.caseCheckBox.isChecked():
            cs = Qt.CaseSensitive
        else:
            cs = Qt.CaseInsensitive

        if self.backwardCheckBox.isChecked():
            self.findPrevious.emit(text, cs)
        else:
            self.findNext.emit(text, cs)

    def enableFindButton(self, text):
        self.findButton.setEnabled(not text.isEmpty())

