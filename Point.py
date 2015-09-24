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
import easygui
import Draft_topo
import FreeCAD
from topoGui import grup,name as fitxer

def importa(fitxer=None, grup = None, codis_check=[]):
    
    #if fitxer is None:
    #    fitxer = easygui.fileopenbox('Tria un fitxer de punts (nom, x, y, z, codi)')                     # path and name of file.txt
    #if grup is None:
    #    grup =  easygui.enterbox('tria un nom de grup')
    doc = FreeCAD.ActiveDocument
    grp = doc.addObject("App::DocumentObjectGroup", grup )
    
    file = open(fitxer, "r")                                  # open the file read
    X=Y=Z = 0.0
    codis = []
    llista_punts = []
    for linia in file:
        coordinates = linia.split('\t')
        N,X,Y,Z,C = coordinates                                     # separate the coordinates
        p = Draft_topo.makePoint(float(X),float(Y),float(Z),N,C)         # create points (uncomment for use)
        p.Label = str(N)
        grp.addObject(p)
        #print N," ",X," ",Y," ",Z," ",C
        if C not in codis:
            codis.append(C)
            

        llista_punts.append([C,FreeCAD.Vector(float(X),float(Y),float(Z))]) # append the coordinates
    
        for codi in codis_check:
            line =[]
            for vector in llista_punts:
                if vector[0] == codi: 
                    line.append(vector[1])  
            print line
            if len(line)>0:
                wire=Draft_topo.makeWire(line,closed=False,face=False,support=None)   # create the wire open
                wire.Label = codi
                grp.addObject(wire)
    #print codis, code_list

    file.close()
    break


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