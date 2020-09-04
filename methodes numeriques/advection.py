import matplotlib.pyplot as plt
import numpy as np
import math
from wendroff import wendroff
from upwind import upwind
from friedrich import friedrich


j=0
condini=0
while (condini != 1 and condini != 2):
    break
condini=input("choix des conditions initiales 1:Heaviside ou 2:cos(2*pi*x)   ")


for dx in range(1,0.05,- 0.05):
    j=j+1 #compteur pour la boucle sur dx
    
    #INITIALISATION DES CONSTANTES
    dt=dx/2
    k=0
    a=1
    tmax=1

    #CREATION DES MATRICES
    u = []
    u1 = []
    u2 = []
    u3 = []

    #CONDITIONS INTIALES DE REFERENCE
    dx=0.01
    x=np.arange(-5 , 5+dx , dx )
    H=np.heaviside([np.arange(- 5,6,1)], 0)

if condini==1:
        for x in range(- 5,5):
            u.append(1+H*(x)-H*(x-2))

else:
        for x in range(- 5,5):
            
            u.append(math.cos(2*math.pi*x))
       
    

    #BOUCLE TEMPORELLE
k=0
for t in range(0,tmax,dt):
        
        k=k+1 #compteur de temps
        
        #INITIALISATION DES MATRICES A t=0
        if t==0:
            
            if condini==1:
                for x in range(- 5,5):
                    u1.append(1+H*(x+1)-H*(x-1))
                
            else:
                for x in range(- 5,5):
                    u1.append(math.cos(2*math.pi*x))
                
            
            u2=u1
            u3=u1
            
        #SI t DIFFERENT DE 0 ON EXECUTE LES FONCTIONS D'ADVECTION    
        else:
            #u1=upwind(dt,dx,a,k,u1)
            u2=friedrich(dt,dx,a,k,u2)
            u3=wendroff(dt,dx,a,k,u3)
        
    
    
erreur1=sum(abs(u - u1)) / dx
erreur2=sum(abs(u - u2)) / dx
erreur3=sum(abs(u - u3)) / dx   


 # REPRESENTATION DU SCHEMA UPWIND

#plt.subplot(3,2,1)
#plt.plot(concat([np.arange(- 5,5,dx)]),u1(end(),np.arange()),'-r')
#plt.plot(concat([np.arange(- 5,5,dx)]),u,'-b')
#plt.axis(concat([- 5,5,0,3]))
#plt.subplot(3,2,2)
#plt.loglog(concat([np.arange(0.05,1,0.05)]),erreur1,'--r')
#plt.axis(concat([0.05,1,0,1000]))
    # REPRESENTATION DU SCHEMA LAX FRIEDRICH
#plt.subplot(3,2,3)
#plt.plot(concat([np.arange(- 5,5,dx)]),u2(end(),np.arange()),'-g')
#plt.plot(concat([np.arange(- 5,5,dx)]),u,'-b')
#plt.axis(concat([- 5,5,0,3]))
#plt.subplot(3,2,4)
#plt.loglog(concat([np.arange(0.05,1,0.05)]),erreur2,'--g')
#plt.axis(concat([0.05,1,0,1000]))
    # REPRESENTATION DU SCHEMA LAX WENDROFF
#plt.subplot(3,2,5)
#plt.plot(concat([np.arange(- 5,5,dx)]),u3(end(),np.arange()),'-m')
#plt.plot(concat([np.arange(- 5,5,dx)]),u,'-b')
#plt.axis(concat([- 5,5,0,3]))
#plt.subplot(3,2,6)
#plt.loglog(concat([np.arange(0.05,1,0.05)]),erreur3,'--m')
#axis(concat([0.05,1,0,1000]))




