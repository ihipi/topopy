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

class FreeTopo():
    def __init__(self):
        pass
    def importa(self, fitxer=None, grup = None):
        if fitxer == None:
            fitxer = easygui.fileopenbox('Tria un fitxer de punts (nom, x, y, z, codi)')                     # path and name of file.txt
        if grup == None:
            grup =  easygui.enterbox('tria un nom de grup')
        doc = FreeCAD.activeDocument()
        grp = doc.addObject("App::DocumentObjectGroup", grup )
        
        file = open(fitxer, "r")                                  # open the file read
        X=Y=Z = 0.0
        
        for linia in file:
            coordinates = linia.split('\t')
            N,X,Y,Z,C = coordinates                                     # separate the coordinates
            p = Draft_topo.makePoint(float(X),float(Y),float(Z),N,C)         # create points (uncomment for use)
            p.Label = str(N)
            grp.addObject(p)
            #print N," ",X," ",Y," ",Z," ",C
    
            codis.append(C)
            code_list.append(FreeCAD.Vector(float(X),float(Y),float(Z))) # append the coordinates
    
            print codis, code_list
            file.close()
        return  set(codis)
'''
for code in code_list.keys():
    Draft_topo.makeWire(code_list[code],closed=False,face=False,support=None)   # create the wire open
    
#Draft_topo.makeWire(wire,closed=True,face=False,support=None)   # create the wire closed (uncomment for use)

administrar un grup
doc=App.activeDocument()
grp=doc.addObject("App::DocumentObjectGroup", "Group")
lin=doc.addObject("Part::Feature", "Line")
grp.addObject(lin) # adds the lin object to the group grp
grp.removeObject(lin) # removes the lin object from the group grp
'''