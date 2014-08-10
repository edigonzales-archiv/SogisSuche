# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SogisSuche
                                 A QGIS plugin
 Sogis Suche Plugin
                              -------------------
        begin                : 2014-03-09
        copyright            : (C) 2014 by Stefan Ziegler / Amt für Geoinformation
        email                : stefan.ziegler@bd.so.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from sogissuchedialog import SogisSucheDialog
from suggestcompletion import SuggestCompletion
import resources_rc

try:
    _encoding = QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)

class SogisSuche:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/sogissuche"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/sogissuche_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = SogisSucheDialog(self.iface.mainWindow())
        self.dlg.initGui()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(_translate("SOGIS_Suche", "Settings",  None), self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Sogis Suche", self.action)
        
        # Create own toolbar
        self.toolBar = self.iface.addToolBar(_translate("SOGIS_Suche", "SO!GIS Search",  None))
        self.toolBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)) 
                
        emptyWidget = QWidget(self.toolBar)
        toolBarLayout = QHBoxLayout(emptyWidget)
        toolBarLayout.setMargin(1)
        
        self.suggest = SuggestCompletion(emptyWidget)
        self.suggest.setMinimumWidth(600);
        toolBarLayout.addWidget(self.suggest)
        
        self.toolButtonReset = QToolButton(emptyWidget)
        self.toolButtonReset.setIcon(QIcon(':/plugins/sogissuche/icons/reset.svg'))
        
        toolBarLayout.addWidget(self.toolButtonReset)
        
        emptyWidget.setLayout(toolBarLayout)
        self.toolBar.addWidget(emptyWidget)
        
        # ACHTUNG! TODO
        # preventSuggest
        
        QObject.connect(self.toolButtonReset, SIGNAL("clicked()"), self.resetSuggest)
        QObject.connect(self.suggest, SIGNAL("returnPressed()"), self.doSomething)
        
    def resetSuggest(self):
        self.suggest.clear()
        # Und Rubberband löschen? Falls nein, wie sonst?
        
        
    def doSomething(self):
        print "HAAAAAAAAAAAAAAAALLLO"
        
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Sogis Suche", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        # Remove own toolbar
        self.iface.mainWindow().removeToolBar(self.toolBar)

    def run(self):
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
