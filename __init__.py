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
 This script initializes the plugin, making it known to QGIS.
"""


def name():
    return "Sogis Suche"


def description():
    return "Sogis Suche Plugin"


def version():
    return "Version 0.1"


def icon():
    return "icon.png"


def qgisMinimumVersion():
    return "1.8"

def author():
    return "Stefan Ziegler / Amt für Geoinformation"

def email():
    return "stefan.ziegler@bd.so.ch"

def classFactory(iface):
    # load SogisSuche class from file SogisSuche
    from sogissuche import SogisSuche
    return SogisSuche(iface)
