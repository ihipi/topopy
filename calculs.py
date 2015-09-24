'''
Created on 23 set. 2015

@author: albert
'''
import FreeCAD
from Draft_topo  import DraftVecUtils
import numpy as np
import math
from docutils.nodes import Root
from math import sqrt


class calculs():
    '''
    classdocs
    '''

    def azimut(self,p1=(100,100,1000),p2=(-5000,100,1000) ):
        
        Az = ((math.atan2( p2[0]-p1[0],p2[1]-p1[1]))*200/math.pi)
        print Az
        if p2[0]-p1[0]>0:
            if  p2[1]-p1[1]<0:
                Az = Az + 200
            if p2[1]-p1[1]==0:
                Az = 100
        if p2[0]-p1[0]<0 :
            if p2[1]-p1[1]<0:
                Az = Az + 200
            if p2[1]-p1[1]==0:
                Az =300
        if p2[0]-p1[0]<0 and  p2[1]-p1[1]>0:
            Az = Az + 400
            
        print('azimut:',Az)
        return Az
        
    def angle(self,p1=(-400,100,1000),p2=(400,400,1000),v=(100,100,1000)):
        P1 = FreeCAD.Vector(p1)
        P2 = FreeCAD.Vector(p2)
        V = FreeCAD.Vector(v)
        
        angle_v = abs(self.azimut(v,p1)-self.azimut(v,p2))
        print('angle:', angle_v)
        if angle_v>200:
            angle_v = 400-angle_v
        print('angle:', angle_v)
        return angle_v
    
    
    def valor_clotoide(self, angle=150, radi= 100):
        
        t= (200-angle)/2  # es necessita el complementari de angle/2 
        L=t*2*radi
        A=sqrt(L*radi)
        print('clotoide')
        print(L,A)
        
    def x_y(self, R=300, L=500):
        x=L-(L**5/(10*((2*R*L)**2)))+(L**9/(216*((2*R*L)**4)))-(L**13/(9360((2*R*L)**6)))    
        y=(L**3/(3*((2*R*L))))+(L**7/(42*((2*R*L)**3)))-(L**11/(1320((2*R*L)**5)))+(L**15/(75600((2*R*L)**7)))
        
        
        
angle = calculs().angle()
calculs().valor_clotoide()
       
        
