# -*- coding: utf-8 -*-

"""
***************************************************************************
    GeoServerToolsAlgorithmProvider.py
    ---------------------
    Date                 : October 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'October 2012'
__copyright__ = '(C) 2012, Victor Olaya'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'


import os
from sextante.servertools.CreateWorkspace import CreateWorkspace
from sextante.servertools.ImportVectorIntoGeoServer import ImportVectorIntoGeoServer
from sextante.servertools.ImportRasterIntoGeoServer import ImportRasterIntoGeoServer
from sextante.servertools.DeleteWorkspace import DeleteWorkspace
from sextante.servertools.DeleteDatastore import DeleteDatastore
from sextante.servertools.StyleGeoServerLayer import StyleGeoServerLayer
from sextante.core.AlgorithmProvider import AlgorithmProvider
from PyQt4 import QtGui

class GeoServerToolsAlgorithmProvider(AlgorithmProvider):

    def __init__(self):
        AlgorithmProvider.__init__(self)
        self.alglist = [ImportVectorIntoGeoServer(), ImportRasterIntoGeoServer(), 
                        CreateWorkspace(), DeleteWorkspace(), DeleteDatastore(), 
                        StyleGeoServerLayer()]#, TruncateSeedGWC()]

    def initializeSettings(self):
        AlgorithmProvider.initializeSettings(self)


    def unload(self):
        AlgorithmProvider.unload(self)


    def getName(self):
        return "geoserver"

    def getDescription(self):
        return "Geoserver management tools"

    def getIcon(self):
        return QtGui.QIcon(os.path.dirname(__file__) + "/../images/geoserver.png")

    def _loadAlgorithms(self):
        self.algs = self.alglist

    def supportsNonFileBasedOutput(self):
        return True