'''
Created on 23 set. 2015

@author: albert
'''
#import FreeCAD
#from Draft_topo  import DraftVecUtils
import math
from math import sqrt, degrees, pi, radians, sin, cos, tan


class calculs():
    '''
    classdocs
    '''

    def azimut(self,p1=(100,100,1000),p2=(5000,1100,1000) ):
        '''
        Calcula l'azimyut entre dos punt i el torna en radians
        '''
        Az = ((math.atan2( p2[0]-p1[0],p2[1]-p1[1])))           #calcula  l'azimut en radians
        print('azimut: ' , Az*200/pi)
        return Az
        
    def angle(self,p1=(50000,3000,1000),p2=(10000,50000,1000),v=(10000,10000,1000)):
        '''
        Calcula l'angle entre dues rectes i el retorna com a radians
        '''
        angle_v =self.azimut(v,p1)-self.azimut(v,p2)
        print(angle_v)
        print('angle:', (math.degrees(angle_v)*400)/360)
        return angle_v
    
    def dist_recta(self,p1=(100,100,1000),p2=(5000,100,1000),dist= 50, az=None):
        '''
        Calcula un punt en un "pk" d'una recta donada per dos punts o un azimut
        '''
        if az == None:
            az = self.azimut(p1, p2)
            
        x = p1[0] + dist * sin(az)
        y = p1[1] + dist * cos(az)
        punt = [x,y]
        print(punt)
        return punt
    def pk_dist(self,p1=(100,100,1000),p2=(5000,100,1000),  pk=50 , dist= 50, az = None ,pk_i =None):
        '''
        Calcula un punt en un "pk" i distancia d'una recta donada per dos punts
        '''        
        if pk_i:
            pk = pk +pk_i
            
        if not az:
            az = self.azimut(p1, p2)
        punt = self.dist_recta(p1,dist = pk,az = az)
            
        if dist != 0:
            if dist > 0:
                az = az+ pi/2
                print(az)
            else:
                az = az-pi/2
                print(az)

            punt = self.dist_recta(punt,dist = abs(dist),az = az)
        
        
        
class circular(calculs):
        def __init__(self,p1=(50000,3000,1000),p2=(10000,50000,1000),v=(10000,10000,1000),r=300):
            self.p1 = p1
            self.p2 = p2
            self.vertex = v
            self.v=self.angle(self.p1, self.p2, self.vertex)    #angle entre les dues rectes
            self.R = r 
            self.v_R = pi-self.v
            self.tang_in = self.dist_recta(self.vertex, self.p1, self.tang_in_out())
            self.tang_out = self.dist_recta(self.vertex, self.p2, self.tang_in_out())
          
        def tang_in_out(self):
            '''
            Calcula la distancia de les tangents d'entrada i sortida
            '''
            tang = self.R * tan(self.v_R/2)  
            return tang
        def info(self):
            print('angle entre rectes: ', self.v,
                  'angle de la curva: ', self.v_R,
                  'tang entrada: ', self.tang_in,
                  'tang sortida: ', self.tang_out)
class clotoide(calculs):    
    def __init__(self,p1=(50000,3000,1000),p2=(10000,50000,1000),v=(10000,10000,1000),r=300, DesCir = None):
           
        if not DesCir:
            self.p1 = p1
            self.p2 = p2
            self.vertex = v
            self.v=self.angle(self.p1, self.p2, self.vertex)    #angle entre les dues rectes
            self.R = r                                       #radi de la curva 
            self.t = self.t()                                   #angle de la tangent del trianle isosceles amb l'annge vertes
            self.L = self.desarrollo_clotoide()#desarrollo de la clotoide
            self.param = self.valor_clotoide()
            self.F = self.punt_tang_circular() 
            self.tang_in = self.punt_recta_clotaide(self.vertex, self.p1)
            self.tang_out = self.punt_recta_clotaide(self.vertex, self.p2)
        
        else:
            self.p1 = p1
            self.p2 = p2
            self.vertex = v
            self.v=self.angle(self.p1, self.p2, self.vertex)    #angle entre les dues rectes
            self.R = r                                       #radi de la curva 
            self.desCircAngle = DesCir/self.R
            self.t = self.t(self.desCircAng)
            self.L = self.desarrollo_clotoide()             #desarrollo de la clotoide
            self.param = self.valor_clotoide()
            self.F = self.punt_tang_circular() 
        
        
    def t(self,desCircAng= None):
        '''
        Calcula l'angle de la tangent del trianle isosceles amb l'angle entre les dues rectes
        '''
        if not desCircAng:
            vd= degrees(self.v)*400/360
            vr= self.v
            

            t=  abs(200-vd)/2 # es necessita el complementari de angle/2 
        else:
            t = 100-(desCircAng/2+self.v/2)
        print('tau radiats: ', radians(t*360/400))
        return radians(t*360/400)
    
    def desarrollo_clotoide(self):
        t = self.t
        R = self.R 
        L=t*2*R 
        print(t)
        print(R)
        print('desarrollo de la clotoide')
        print(L)        
        return L
    
    def valor_clotoide(self):
        R = self.R
        L = self.L
        A=sqrt(L*R)
        print('parametre de la clotoide')
        print(A)

        return(A)
        
    def punt_tang_circular(self):
        '''
        trobem el punt on es troben les dues clotoides (el centre de la 'curva')
        '''
        
        R = float(self.R)
        L = float(self.L)
        print(R,L)
        x_f=L-(L**5/(10*((2*R*L)**2)))+(L**9/(216*((2*R*L)**4)))-(L**13/(9360*((2*R*L)**6)))    
        y_f=(L**3/(3*((2*R*L))))+(L**7/(42*((2*R*L)**3)))-(L**11/(1320*((2*R*L)**5)))+(L**15/(75600*((2*R*L)**7)))
        punt = (x_f,y_f)
        print('F: ', punt)
        return(punt)
    def tang_llarga(self):
        '''
        calcula els valors per la tangent larga
        ''' 
        punt_tangencia = self.F
        X = punt_tangencia[0]  
        Y = punt_tangencia[1]
        Tl = X-(Y/float(math.tan(self.t)))  
        
        print('tangent llarga')
        print(Tl)    
        return(Tl)
    
    def tang_curta(self):
        '''
        calcula els valors per la tangent curta
        '''
        punt_tangencia = self.F
        Y = punt_tangencia[1]
        Tc = Y/float(math.sin(self.t))
        print('tangent curta')
        print(Tc)    
        return(Tc)       
    
    def tang_in_out(self):
        VF = self.F[1]/math.sin(self.v/2)
        VC = self.tang_llarga()+(VF/math.sin(self.t))
        print("Tangent d'entrada sortida")
        print(VC)
        return VC
    
    def punt_recta_clotaide(self,vertex,punt):
        VC = self.tang_in_out()
        print("VC: ",VC)
        x = vertex[0]+((self.tang_in_out())*(math.sin(self.azimut(vertex, punt))))
        y = vertex[1]+((self.tang_in_out())*(math.cos(self.azimut(vertex, punt))))
        punt = (x,y)
        print("punt de tangencia recta clotoide")
        print(punt)
        return(punt)
        
#clotoide()
#calculs().angle()
#calculs().dist_recta([150,100], dist=-50, az=pi)
#calculs().pk_dist()
circular().info()       
        

