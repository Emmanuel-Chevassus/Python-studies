import numpy as np
import matplotlib.pyplot as plt
fichier="CN2018020909.cor"
temps=np.zeros(4333)
altitude=np.zeros(4333)
latitude=np.zeros(4333)
longitude=np.zeros(4333)
ventest=np.zeros(4333)
ventnord=np.zeros(4333)
vvert=np.zeros(4333)
Vhor=np.zeros(4333)
Vdir=np.zeros(4333)
Dp=np.zeros(4333)
T=np.zeros(4333)
U=np.zeros(4333)
Press=np.zeros(4333)
Flag=np.zeros(4333)
i=-2


f=open(fichier, 'r')
lignes=f.readlines()
for ch in lignes :
    a=ch.split()
    i=i+1
    if i >=0 :
        temps[i]=int(a[0])
        altitude[i]=float(a[1])
        latitude[i]=float(a[2])
        longitude[i]=float(a[3])
        ventest[i]=float(a[4])
        ventnord[i]=float(a[5])
        vvert[i]=float(a[6])
        Vhor[i]=float(a[7])
        Vdir[i]=float(a[8])
        Dp[i]=float(a[9])
        T[i]=float(a[10])
        U[i]=float(a[11])
        Press[i]=float(a[12])
        Flag[i]=int(a[13])
    
plt.figure('profil vertical pression')
plt.title("Pression en fonction de l'altitude")
plt.plot(Press,altitude,'-r')
plt.xlabel('pression')
plt.ylabel('altitude')
plt.show()