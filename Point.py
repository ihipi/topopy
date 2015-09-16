'''
Created on 15 set. 2015

@author: albert
'''
# -*- coding: utf-8 -*-
# created a wire with coordinate x y z unseparated (in the file)
#EX:
#0 0 0
#10 10 10
#15 20 25
#. . . .
 
from __future__ import unicode_literals
from FreeCAD import Base
import Draft, Part
 
fichier = "C:\yourPath\cloud.asc"                          # path and name of file.txt
 
file = open(fichier, "r")                                  # open the file read
wire = []
X=Y=Z = 0.0
 
for ligne in file:
    coordinates = ligne.split()
    X,Y,Z = coordinates                                     # separate the coordinates
#    Draft.makePoint(float(X),float(Y),float(Z))            # create points (uncomment for use)
    print X," ",Y," ",Z
    wire.append(FreeCAD.Vector(float(X),float(Y),float(Z))) # append the coordinates
 
file.close()
Draft.makeWire(wire,closed=False,face=False,support=None)   # create the wire open
#Draft.makeWire(wire,closed=True,face=False,support=None)   # create the wire closed (uncomment for use)
'''
administrar un grup
doc=App.activeDocument()
grp=doc.addObject("App::DocumentObjectGroup", "Group")
lin=doc.addObject("Part::Feature", "Line")
grp.addObject(lin) # adds the lin object to the group grp
grp.removeObject(lin) # removes the lin object from the group grp
'''