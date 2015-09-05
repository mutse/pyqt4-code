# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gotocelldialog.ui'
#
# Created: Sat Sep  5 14:37:52 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GoToCellDialog(object):
    def setupUi(self, GoToCellDialog):
        GoToCellDialog.setObjectName(_fromUtf8("GoToCellDialog"))
        GoToCellDialog.resize(190, 94)
        self.vboxlayout = QtGui.QVBoxLayout(GoToCellDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(GoToCellDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(GoToCellDialog)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.hboxlayout.addWidget(self.lineEdit)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(GoToCellDialog)
        self.okButton.setEnabled(False)
        self.okButton.setDefault(True)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.hboxlayout1.addWidget(self.okButton)
        self.cancelButton = QtGui.QPushButton(GoToCellDialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.hboxlayout1.addWidget(self.cancelButton)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(GoToCellDialog)
        QtCore.QMetaObject.connectSlotsByName(GoToCellDialog)
        GoToCellDialog.setTabOrder(self.lineEdit, self.okButton)
        GoToCellDialog.setTabOrder(self.okButton, self.cancelButton)

    def retranslateUi(self, GoToCellDialog):
        GoToCellDialog.setWindowTitle(_translate("GoToCellDialog", "Go to Cell", None))
        self.label.setText(_translate("GoToCellDialog", "&Cell Location:", None))
        self.okButton.setText(_translate("GoToCellDialog", "OK", None))
        self.cancelButton.setText(_translate("GoToCellDialog", "Cancel", None))

