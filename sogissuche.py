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
        self.dlg = SogisSucheDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/sogissuche/icon.png"),
            u"Text for the menu item", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Sogis Suche", self.action)
        
        # Create own toolbar
        self.toolBar = self.iface.addToolBar("SO!GIS Suche")
        self.toolBar.setSizePolicy(QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)) 
        
        # Create search lineedit
        self.suggest = SuggestCompletion(self.toolBar)
        # Does not work with Qt 4.6 = Ubuntu 10.04 = SO!GIS
#        self.suggest.setPlaceholderText(QCoreApplication.translate("SogisSuche", u"Suche nach Adressen, Grundstücken, etc."))
        # Figure out what makes sense...
#        self.suggest.setMaximumWidth(400);
        self.suggest.setMinimumWidth(600);
        
        # Ugly hack to get some space between the toolbar start and the lineedit
        empty = QWidget()
        empty.setMinimumSize(3, 3)
        empty.setMaximumSize(3, 3)
        self.toolBar.addWidget(empty)

        # Add search lineedit to toolbar
        self.suggestAction = self.toolBar.addWidget(self.suggest)
        self.suggestAction.setVisible(True)
        
    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Sogis Suche", self.action)
        self.iface.removeToolBarIcon(self.action)
        
        # Remove own toolbar
        self.iface.mainWindow().removeToolBar(self.toolBar)

    # run method that performs all the real work
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
