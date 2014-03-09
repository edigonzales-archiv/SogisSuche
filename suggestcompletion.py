# -*- coding: utf-8 -*-

# Import the PyQt and the QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *

class SuggestCompletion(QLineEdit, QWidget):
    
    def __init__(self, parent):
        QLineEdit.__init__(self, parent)
        
        self.popup = QTreeWidget()
        self.popup.setWindowFlags(Qt.Popup);
        self.popup.setFocusPolicy(Qt.NoFocus);
        self.popup.setFocusProxy(parent);
        self.popup.setMouseTracking(True);
        
        self.popup.setColumnCount(2);
        self.popup.setUniformRowHeights(True);
        self.popup.setRootIsDecorated(False);
        self.popup.setEditTriggers(QTreeWidget.NoEditTriggers)
        self.popup.setSelectionBehavior(QTreeWidget.SelectRows)
        self.popup.setFrameStyle(QFrame.Box | QFrame.Plain)
        self.popup.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.popup.header().hide()
        
        self.popup.installEventFilter(self);
        
        self.connect(self.popup, SIGNAL("itemClicked(QTreeWidgetItem, int)"), self.doneCompletion)
        
        self.timer = QTimer(self)
        self.timer.setSingleShot(True);
        self.timer.setInterval(500);
        
        
    def doneCompletion(self):
        print "doneCompletion"
        
    def foo(self):
        print "foobar"
        
