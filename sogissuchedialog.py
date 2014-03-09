# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SogisSucheDialog
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

from PyQt4 import QtCore, QtGui
from ui_sogissuche import Ui_SogisSuche
# create the dialog for zoom to point


class SogisSucheDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_SogisSuche()
        self.ui.setupUi(self)
