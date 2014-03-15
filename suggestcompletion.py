# -*- coding: utf-8 -*-

# Import the PyQt and the QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtNetwork import QNetworkAccessManager
from qgis.core import *
from qgis.gui import *

class SuggestCompletion(QLineEdit, QWidget):
    
    def __init__(self, parent):
        QLineEdit.__init__(self, parent)
        
        self.GSUGGEST_URL = "http://google.com/complete/search?output=toolbar&q=%1"
        
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
        self.connect(self.timer, SIGNAL("timeout()"), self.autoSuggest);
        self.connect(self, SIGNAL("textEdited(QString)"), self.timer.start)
        
        self.networkManager = QNetworkAccessManager(self)
        self.connect(self.networkManager, SIGNAL("finished(QNetworkReply*)"), self.handleNetworkData)
        
    def eventFilter(self, obj, ev):
        try:
            if obj != self.popup:
                return False
            
            if ev.type() == QEvent.MouseButtonPress:
                self.popup.hide()
                self.setFocus()
                return True
                
            if ev.type() == QEvent.KeyPress:
                consumed = False
                key = int(ev.key())
                
                if key == Qt.Key_Enter or key == Qt.Key_Return:
                    self.doneCompletion()
                    consumed = True
                elif key == Qt.Key_Escaped:
                    self.setFocus()
                    self.popup.hide()
                    consumed = True
                elif key == Qt.Key_Up or key == Qt.Key_Down or key == Qt.Key_Home or key == Qt.Key_End or key == Qt.Key_PageUp or key == Qt.Key_PageDown:
                    pass
                else:
                    self.setFocus()
                    self.event(ev)
                    self.popup.hide()
                    pass
                    
                return consumed
            return False
        except:
            # underlying C++ ..... ???
            return False

        
    def doneCompletion(self):
        print "doneCompletion"
        
    def autoSuggest(self):
        print "fooooo"
        #str = self.
        
    def handleNetworkData(self, reply):
        print "baaaar"
        print reply
        
    def foo(self):
        print "foobar"
        
