# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sogissuche.ui'
#
# Created: Sun Mar  9 17:02:18 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SogisSuche(object):
    def setupUi(self, SogisSuche):
        SogisSuche.setObjectName(_fromUtf8("SogisSuche"))
        SogisSuche.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(SogisSuche)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(SogisSuche)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SogisSuche.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SogisSuche.reject)
        QtCore.QMetaObject.connectSlotsByName(SogisSuche)

    def retranslateUi(self, SogisSuche):
        SogisSuche.setWindowTitle(QtGui.QApplication.translate("SogisSuche", "SogisSuche", None, QtGui.QApplication.UnicodeUTF8))

