import numpy as np
import matplotlib.pyplot as plt
#---------------------------------------------------------------------------------------------------------------
#INTIALISATION DES VARIABLES
a= 1 
t = np.arange(0, 1+dt, dt )
dx = 0.1
dt = 0.01
x = np.arange(-5 , 5+dx , dx )


choix1 = 1 + np.heaviside(x+1,1)  - np.heaviside(x-1,1) # condition initiale 1
choix2 = np.cos(2*np.pi*x)

#dans les algorithmes ci-dessous i correspondra à la position et k au temps

N = len(t)
X = len (x)
k= 0
U1 = np.zeros(shape=(N+1,X+1)) #UPWIND
U1[:,X] = 1
U2 = np.zeros(shape=(N+1,X+1)) #Wendroff
U2[:,X] = 1
Udemi = np.zeros(shape=(N+1,X+1)) #Wendroff pour 1/2
Udemi[:,X] = 1
U3 = np.zeros(shape=(N+1,X+1)) #Friedrichs
U3[:,X] = 1

condition_initiale = int(input( "choisir une condition initiale:\nAppuyer sur 1 pour la première fonction \nAppuyer sur 2 pour la deuxième fonction \n"))
#---------------------------------------------------------------------------------------------------------------
#SCHEMA UPWIND

if condition_initiale == 1:
    U1[0,0:X]= choix1
    for k in range(0,N):

        for i in range (0, X):
            U1[k+1,i]=U1[k,i]+a*(dt/dx)*(U1[k,i-1]-U1[k,i]) #upwind
    
    plt.plot(x, U1[0,0:X])
    plt.plot(x,U1[2,0:X])
    plt.plot(x,U1[3,0:X])
    plt.plot(x,U1[4,0:X])
    plt.plot(x,U1[5,0:X])
    plt.plot(x, U1[N-1,0:X])
    plt.title("Schema Upwind")
    plt.show()



elif condition_initiale == 2:
    U1[0,0:X]= choix2
    for k in range(0,N):
       
        for i in range (0, X):
            U1[k+1,i]=U1[k,i]+a*(dt/dx)*(U1[k,i-1]-U1[k,i]) #upwind

    plt.plot(x, U1[0,0:X])
    plt.plot(x,U1[2,0:X])
    plt.plot(x,U1[3,0:X])
    plt.plot(x,U1[4,0:X])
    plt.plot(x,U1[5,0:X])
    plt.plot(x, U1[N-1,0:X])
    plt.title("Schema Upwind")
    plt.show()

#---------------------------------------------------------------------------------------------------------------
#SCHEMA DE WENDROFF
if condition_initiale == 1:
    U2[0,0:X]= choix1
    for k in range(0,N):
       
        for i in range (1, X+1):          
            if i != 2:
                Udemi[k+2,i+1]=dt/dx*a*((Udemi[k,i]-Udemi[k,i+1])/2)+Udemi[k,i+1] #wendroff calcul de t+1/2dt
 #on ne prend pas la 1ere valeure car elle nous fait sortir du schéma
                U2[i] = dt/dx*a*((Udemi[i]-Udemi[i+1])/2)+Udemi[i+1]
                 
                   
    plt.plot(x, U2[0,0:X])
    plt.plot(x,U2[2,0:X])
    plt.plot(x,U2[3,0:X])
    plt.plot(x,U2[4,0:X])
    plt.plot(x,U2[5,0:X])
    plt.plot(x, U2[N-1,0:X])
    plt.title("Schema de WENDROFF")
    plt.show()

elif condition_initiale == 2:
    U2[0,0:X]= choix2
    for k in range(0,N):
       
        for i in range (0, X):          
            if i != 0:
                Udemi[k+1,i]=dt/dx*a*((Udemi[k-1,i-1]-Udemi[k-1,i])/2)+Udemi[k-1,i]

        for i in range (0, X):             
             if i != 0:
                 U2[i] = dt/dx*a*((Udemi[i-1]-Udemi[i])/2)+Udemi[i]
                   
    plt.plot(x, U2[0,0:X])
    plt.plot(x,U2[2,0:X])
    plt.plot(x,U2[3,0:X])
    plt.plot(x,U2[4,0:X])
    plt.plot(x,U2[5,0:X])
    plt.plot(x, U2[N-1,0:X])
    plt.title("Schema de WENDROFF")
    plt.show()
#---------------------------------------------------------------------------------------------------------------
#SCHEMA DE FRIEDRICH
    
if condition_initiale == 1:
    U3[0,0:X]= choix1
    for k in range(0,N):
             for i in range (0, X):
                 if (i!= 0 and i!= X):  #on exclut le premier et le dernier maillon
                     U3[i]=dt*a*(U3[k-1,i-1]-U3[k-1,i+1])/(2*dx)+(U3[k-1,i+1]+U3[k-1,i-1])/2

    plt.plot(x, U3[0,0:X])
    plt.plot(x,U3[2,0:X])
    plt.plot(x,U3[3,0:X])
    plt.plot(x,U3[4,0:X])
    plt.plot(x,U3[5,0:X])
    plt.plot(x, U3[N-1,0:X])
    plt.title("Schema de Friedrich")
    plt.show()



elif condition_initiale == 2:
     U3[0,0:X]= choix2
     for k in range(0,N):
        for i in range (0, X):
            if (i!= 0 and i!= X):
                U3[i]=dt*a*(U3[k-1,i-1]-U3[k-1,i+1])/(2*dx)+(U3[k-1,i+1]+U3[k-1,i-1])/2

     plt.plot(x, U3[0,0:X])
     plt.plot(x,U3[2,0:X])
     plt.plot(x,U3[3,0:X])
     plt.plot(x,U3[4,0:X])
     plt.plot(x,U3[5,0:X])
     plt.plot(x, U3[N-1,0:X])
     plt.title("Schema de Friedrich")
     plt.show()
#---------------------------------------------------------------------------------------------------------------
#Calcul des erreurs
