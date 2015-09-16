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
import Part, easygui
import Draft_topo
import FreeCAD

fitxer = easygui.fileopenbox('Tria un fitxer de punts (nom, x, y, z, codi)')                     # path and name of file.txt
 
file = open(fitxer, "r")                                  # open the file read
wire = []
codis =[]
X=Y=Z = 0.0
grp =  easygui.enterbox('tria un nom de grup')

doc = FreeCAD.activeDocument()
grup = doc.addObject("App::DocumentObjectGroup", grp )

code_list={}

for linia in file:
    coordinates = linia.split('\t')
    N,X,Y,Z,C = coordinates                                     # separate the coordinates
    p = Draft_topo.makePoint(float(X),float(Y),float(Z),N,C)         # create points (uncomment for use)
    p.Label = str(N)
    grup.addObject(p)
    print X," ",Y," ",Z
    if not code_list.has_key(C):
        codis.append(C)
        code_list={C:[]}
    
    
    code_list[C].append(FreeCAD.Vector(float(X),float(Y),float(Z))) # append the coordinates
 
file.close()
for code in code_list.keys():
    Draft_topo.makeWire(code_list[code],closed=False,face=False,support=None)   # create the wire open
#Draft_topo.makeWire(wire,closed=True,face=False,support=None)   # create the wire closed (uncomment for use)
'''
administrar un grup
doc=App.activeDocument()
grp=doc.addObject("App::DocumentObjectGroup", "Group")
lin=doc.addObject("Part::Feature", "Line")
grp.addObject(lin) # adds the lin object to the group grp
grp.removeObject(lin) # removes the lin object from the group grp
'''