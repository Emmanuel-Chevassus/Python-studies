import numpy as np
import matplotlib.pyplot as plt
from math import*

a= 1 # Definition de paramètres
 
#Definition pas de temps 
dx = 0.1
dt = 0.01
#Conditions initiales
x = np.arange(-5 , 5+dx , dx )
t = np.arange(0, 1+dt, dt )

y1 = 1 + np.heaviside(x+1,1)  - np.heaviside(x-1,1) # condition initiale 1
y2 = np.cos(2*np.pi*x)

# i : position 
# k : temps
N = len(t)
X = len (x)
k= 0
j=0
U = np.zeros(shape=(N+1,X+1))
U[:,X] = 1
erreur1 = np.zeros(shape=(N+1,X+1))
erreur1[:,X]=1
condition_initiale = int(input( "choisir une condition initiale:\nAppuyer sur 1 pour la première fonction \nAppuyer sur 2 pour la deuxième fonction \n"))


if condition_initiale == 1:
    j=j+1
    U[0,0:X]= y1
    for k in range(0,N):
       
        for i in range (0, X):
            U[k+1,i]=U[k,i]+a*(dt/dx)*(U[k,i-1]-U[k,i])

    plt.plot(x, U[0,0:X])
    plt.plot(x,U[2,0:X])
    plt.plot(x,U[3,0:X])
    plt.plot(x,U[4,0:X])
    plt.plot(x,U[5,0:X])
    plt.plot(x, U[N-1,0:X])
    plt.title("Schema de Upwind")
    plt.show()



elif condition_initiale == 2:
    j=j+1
    U[0,0:X]= y2
    for k in range(0,N):
       
        for i in range (0, X):
            U[k+1,i]=U[k,i]+a*(dt/dx)*(U[k,i-1]-U[k,i])

    plt.plot(x, U[0,0:X])
    plt.plot(x,U[2,0:X])
    plt.plot(x,U[3,0:X])
    plt.plot(x,U[4,0:X])
    plt.plot(x,U[5,0:X])
    plt.plot(x, U[N-1,0:X])
    plt.title("Schema de Upwind")
    plt.show()

for j in range(0,N):
                
    for i in range (0, X):

        erreur1[j]=sum(abs(y2-U[j+1,i]))/dx
    plt.loglog(x,erreur1[j])

    plt.title("erreur")
    plt.show()
