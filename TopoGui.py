'''
Created on 20 set. 2015

@author: albert
'''
import Tkinter as tk
from tkFileDialog import askopenfilename
from Tkinter import IntVar, Checkbutton, Frame, Grid
from tkMessageBox import askyesno
import Point


class Application(Frame):
    def __init__(self, master=None, quit=True):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets(quit)
    
    def createWidgets(self, quit=True):
        if quit:
            self.quitButton = tk.Button ( self, text = "Quit",
                                   command=self.quit)
            self.quitButton.grid()


def openfile():
    
    name = askopenfilename()
    nam = name.split("/")
    g=nam[-1].split(".")
    grup= g[0]
    print(nam,g)
    print(grup)
    fitxer = open(name, mode='r')
    
    
    for linia in fitxer:
        coordinates = linia.split('\t')
        N,X,Y,Z,C = coordinates           
        N = coordinates[0]
        X = coordinates[1]
        Y = coordinates[2]
        Z = coordinates[3]
        C = [coordinates[4]]
        if len(coordinates)>5:
            i=5
            for c in range(len(coordinates)-5):
                C.append(coordinates[i])
                codis.add(c)
                i = i+1
        codis.add(C[0])
        
    i= 0   
    r = 2 
    c = 1
    
    
    if askyesno('codis...','Vols unir per codis?'):
        codis_linia.clear()
        tria = tk.Toplevel()
        ok = tk.Button(tria, text='ok', width=25, command=tria.destroy)
        ok.grid(column=0, row=0,columnspan=5)
       
        
        
        for item in codis:
            codis_linia[str(item)]= IntVar()
            
            chb =Checkbutton(tria,text = str(item), variable = codis_linia[item], onvalue = True, offvalue = False, height=5 )
            if c > 5:
                c = 1
                r = r+1
            
            chb.grid(column =c, row=r)
            c = c+1
        label2 = tk.Label(tria,    text= 'Quins codis son linies')
        label2.grid(row=1, columnspan=5)  
    
                
          
def importa():
    print(codis_linia)
    codis_check=[]
    for i, v in codis_linia.items():
        if v.get() ==1 or v.get() == True:
            codis_check.append(str(i))
        print("el codi {} te el valor {}".format(i, v.get()))
    Point.importa(name , grup, codis_check)
    

name=None
grup=None
codis =  set()   
codis_linia = {}


def mainloop():
    app = Application()
    app.master.title("Sample application")              
    
    label = tk.Label(app, fg="green")
    label.grid(column =0, row=0)
    
    #listb = tk.Listbox(app)
    #listb.pack()
    
    b_fitxer = tk.Button(app, text= 'Fitxer', width=25, command = openfile)
    b_fitxer.grid(column =0, row=2)
    b_Importa = tk.Button(app, text= 'Importa', width=15, command = importa)
    b_Importa.grid(column =0, row=3)
    b_Cancela = tk.Button(app, text='Cancela', width=25, command=app.destroy)
    b_Cancela.grid(column =0, row=4)

    app.mainloop()
    
mainloop()