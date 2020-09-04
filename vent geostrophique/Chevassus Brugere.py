# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

import os
os.chdir('c:\\Users\\Emmanuel\\desktop')

data=np.genfromtxt('M1data.txt')



## II - Lire les données et calculs du vent géostrophique en 
## coordonnées cartésiennes

###################Partie A########################
###################Question 1########################

#On calcule les modules des vents géostrophiques

#On définit nos variables       
P = np.pi/180 #Passage des degrés en radians
f = 1.2E-4 #Force de Coriolis
g = 9.81 #Accélération de pesanteur en m.s^-2
dy = 111.3E3 #Longueur méridionale

#Initialisation des tableaux
#Pour p=300hPa et p=700 hPa

u300 = np.zeros((8,13))
u700 = np.zeros((8,13))
v300 = np.zeros((8,13))
v700 = np.zeros((8,13))
z300 = np.zeros((8,13))
z700 = np.zeros((8,13))


# On insère les valeurs dans des tableaux

a = 0
b = 1
for j in range(0,1260):
    if data[j,0] == 300:
        a = a+1
        u300[b,a] = data[j,1] 
        v300[b,a] = data[j,2]
        z300[b,a] = data[j,6]
        
        if a == 12:
            a = 0
            b = b+1

a1 = 0
b1 = 1
for i in range(0,1260):
    if data[i,0] == 700:
        a1 = a1+1
        u700[b1,a1] = data[i,1] 
        v700[b1,a1] = data[i,2]
        z700[b1,a1] = data[i,6]
        
        if a1 == 12:
            a1 = 0
            b1 = b1+1


#Initialisation du tableau avec les latitudes et longitudes

Tab = np.zeros((8,13))
x = 0
y = 0
for i in range(0,166,15):
    x = x+1
    Tab[0,x] = data[i,0]
    u300[0,x] = data[i,0]
    u700[0,x] = data[i,0]
    v300[0,x] = data[i,0]
    v700[0,x] = data[i,0]
    z300[0,x] = data[i,0]
    z700[0,x] = data[i,0]
    
for j in range(0,1259,180):
    y = y+1
    Tab[y,0] = data[j,1]
    u300[y,0] = data[j,1]
    u700[y,0] = data[j,1]
    v300[y,0] = data[j,1]
    v700[y,0] = data[j,1]
    z300[y,0] = data[j,1]
    z700[y,0] = data[j,1]


print("U300",u300)
print("U700",u700)
print("V300",v300)
print("V700",v700)
print("Z300",z300)
print("Z700",z700)



#On calcule les vents géostrophiques

#On créé des tableaux pour nos valeurs de dx, dz, Ug et Vg
dx = np.zeros((8,13))
dzy300 = np.zeros((8,13))
dzy700 = np.zeros((8,13))
Ug300 = np.zeros((8,13))
Vg300 = np.zeros((8,13))
Ug700 = np.zeros((8,13))
Vg700 = np.zeros((8,13))
dzx300 = np.zeros((8,13))
dzx700 = np.zeros((8,13))

for k in range(1,7):
    for l in range(1,12):
        dx[k,l] = dy * np.cos(P*u300[k,0])  #Récupération de la colonne des latitudes
        dzx300[k,l] = z300[k+1,l]-z300[k,l]
        dzx700[k,l] = z700[k+1,l]-z700[k,l]
        dzy300[k,l] = z300[k,l+1]-z300[k,l]
        dzy700[k,l] = z700[k,l+1]-z700[k,l]
        Ug300[k,l] = -(g/f)*(dzx300[k,l]/dy)
        Ug700[k,l] = -(g/f)*(dzx700[k,l]/dy)
        Vg300[k,l] = (g/f)*(dzy300[k,l]/(dx[k,l]))
        Vg700[k,l] = (g/f)*(dzy700[k,l]/(dx[k,l]))
        


# On intègre les latitude et longitudes dans les tableaux des vents géostrophiques

Tab = np.zeros((8,13))
x = 0
y = 0
for i in range(0,166,15):
    x = x+1
    Tab[0,x] = data[i,0]
    Ug300[0,x] = data[i,0]
    Ug700[0,x] = data[i,0]
    Vg300[0,x] = data[i,0]
    Vg700[0,x] = data[i,0]
    
for j in range(0,1259,180):
    y = y+1
    Tab[y,0] = data[j,1]
    Ug300[y,0] = data[j,1]
    Ug700[y,0] = data[j,1]
    Vg300[y,0] = data[j,1]
    Vg700[y,0] = data[j,1]
    
    
print("Ug300",Ug300)
print("Ug700",Ug700)
print("Vg300",Vg300)
print("Vg700",Vg700)


###################Question 2########################

# Calcul de la norme du vent horizontale et vent géostrophique


vh300 = np.zeros((8,13))
vh700 = np.zeros((8,13))
vg300 = np.zeros((8,13))
vg700 = np.zeros((8,13))

for k in range(1,8):
    for l in range(1,13):
        vh300[k,l] = np.sqrt((u300[k,l])**2+(v300[k,l])**2)
        vh700[k,l] = np.sqrt((u700[k,l])**2+(v700[k,l])**2)
        vg300[k,l] = np.sqrt((Ug300[k,l])**2+(Vg300[k,l])**2)
        vg700[k,l] = np.sqrt((Ug700[k,l])**2+(Vg700[k,l])**2)
        
        
Tab = np.zeros((8,13))
x = 0
y = 0
for i in range(0,166,15):
    x = x+1
    Tab[0,x] = data[i,0]
    vh300[0,x] = data[i,0]
    vh700[0,x] = data[i,0]
    vg300[0,x] = data[i,0]
    vg700[0,x] = data[i,0]
    
for j in range(0,1259,180):
    y = y+1
    Tab[y,0] = data[j,1]
    vh300[y,0] = data[j,1]
    vh700[y,0] = data[j,1]
    vg300[y,0] = data[j,1]
    vg700[y,0] = data[j,1]        

print("Vh300",vh300)
print("Vh700",vh700)
print("Norme de Vg300",vg300)
print("Norme de Vg700",vg700)


###################Question 3########################

Er300 = np.zeros((8,13))
Er700 = np.zeros((8,13))

for k in range(1,8):
    for l in range(1,13):
        Er300[k,l] = (vh300[k,l]-vg300[k,l])/(vh300[k,l])*100
        Er700[k,l] = (vh700[k,l]-vg700[k,l])/(vh700[k,l])*100
        
Tab = np.zeros((8,13))
x = 0
y = 0
for i in range(0,166,15):
    x = x+1
    Tab[0,x] = data[i,0]
    Er300[0,x] = data[i,0]
    Er700[0,x] = data[i,0]
    
for j in range(0,1259,180):
    y = y+1
    Tab[y,0] = data[j,1]
    Er300[y,0] = data[j,1]
    Er700[y,0] = data[j,1]

print("Ecart relatif 300", Er300)
print("Ecart relatif 700", Er700)


###################Question 4########################


# On supprime les premières colonnes et lignes pour ne pas prendre en compte
# les latitudes et longitudes
Err300 = np.zeros((6,11))
Err700 = np.zeros((6,11))

for i in range(6):
    for j in range(11):
        Err300[i,j] = Er300[i+1,j+1]
        Err700[i,j] = Er700[i+1,j+1]

print("Ecart moyen a 300 hPa", np.mean(vh300-vg300))
print("Ecart moyen a 700 hPa", np.mean(vh700-vg700))
print("Ecart maximal a 300 hPa", np.max(vh300-vg300))
print("Ecart maximal a 700 hPa", np.max(vh700-vg700))
print("Ecart minimal a 300 hPa", np.min(vh300-vg300))
print("Ecart minimal a 700 hPa", np.min(vh700-vg700))

###################Partie B########################
###################Question 1########################

#Direction des vents géostophiques et horizontaux


ThetaVg300 = np.zeros((7,12))
ThetaVg700 = np.zeros((7,12))
ThetaVh300 = np.zeros((7,12))
ThetaVh700 = np.zeros((7,12))

for k in range(1,7):
    for l in range(1,12):
        if u300[k,l] > 0 and v300[k,l] > 0 :
            ThetaVh300[k,l] = np.degrees(np.arctan((u300[k,l]/v300[k,l]))) # Quand x et y sont positifs
        elif u300[k,l] < 0 and v300[k,l] > 0 :
            ThetaVh300[k,l] = np.degrees(np.arctan((v300[k,l]/(-u300[k,l]))))+270 # Quand x négatif et y positif
        elif u300[k,l] > 0 and v300[k,l] < 0 :
            ThetaVh300[k,l] = np.degrees(np.arctan(((-v300[k,l])/u300[k,l])))+90 # Quand x postif et y négatif
        elif u300[k,l] < 0 and v300[k,l] < 0 :
            ThetaVh300[k,l] = np.degrees(np.arctan(((u300[k,l])/(v300[k,l]))))+180 # Quand x et y sont négatifs
 
           
for k in range(1,7):
    for l in range(1,12):
        if u700[k,l] > 0 and v700[k,l] > 0 :
            ThetaVh700[k,l] = np.degrees(np.arctan((u700[k,l]/v700[k,l])))
        elif u700[k,l] < 0 and v700[k,l] > 0 :
            ThetaVh700[k,l] = np.degrees(np.arctan((v700[k,l]/(-u700[k,l]))))+270
        elif u700[k,l] > 0 and v700[k,l] < 0 :
            ThetaVh700[k,l] = np.degrees(np.arctan(((-v700[k,l])/u700[k,l])))+90
        elif u700[k,l] < 0 and v700[k,l] < 0 :
            ThetaVh700[k,l] = np.degrees(np.arctan(((u700[k,l])/(v700[k,l]))))+180

          
for k in range(1,7):
    for l in range(1,12):
        if Ug300[k,l] > 0 and Vg300[k,l] > 0 :
            ThetaVg300[k,l] = np.degrees(np.arctan((Ug300[k,l]/Vg300[k,l])))
        elif Ug300[k,l] < 0 and Vg300[k,l] > 0 :
            ThetaVg300[k,l] = np.degrees(np.arctan((Vg300[k,l]/(-Ug300[k,l]))))+270
        elif Ug300[k,l] > 0 and Vg300[k,l] < 0 :
            ThetaVg300[k,l] = np.degrees(np.arctan(((-Vg300[k,l])/Ug300[k,l])))+90
        elif Ug300[k,l] < 0 and Vg300[k,l] < 0 :
            ThetaVg300[k,l] = np.degrees(np.arctan(((Ug300[k,l])/(Vg300[k,l]))))+180
            

for k in range(1,7):
    for l in range(1,12):
        if Ug700[k,l] > 0 and Vg700[k,l] > 0 :
            ThetaVg700[k,l] = np.degrees(np.arctan((Ug700[k,l]/Vg700[k,l])))
        elif Ug700[k,l] < 0 and Vg700[k,l] > 0 :
            ThetaVg700[k,l] = np.degrees(np.arctan((Vg700[k,l]/(-Ug700[k,l]))))+270
        elif Ug700[k,l] > 0 and Vg700[k,l] < 0 :
            ThetaVg700[k,l] = np.degrees(np.arctan(((-Vg700[k,l])/Ug700[k,l])))+90
        elif Ug700[k,l] < 0 and Vg700[k,l] < 0 :
            ThetaVg700[k,l] = np.degrees(np.arctan(((Ug700[k,l])/(Vg700[k,l]))))+180
            

###################Question 2########################


E300 = np.zeros((7,12))
E700 = np.zeros((7,12))


for k in range(1,7):
    for l in range(1,12):
        E300[k,l] = np.abs(ThetaVh300[k,l]-ThetaVg300[k,l])
        if E300[k,l] > 180:
            E300[k,l] = np.abs(E300[k,l] - 360)


for k in range(1,7):
    for l in range(1,12):
        E700[k,l] = np.abs(ThetaVh700[k,l]-ThetaVg700[k,l])
        if E700[k,l] > 180:
            E700[k,l] = np.abs(E700[k,l] - 360)
        
###################Patie C########################

Z300 = np.zeros((7,12))
Z700 = np.zeros((7,12))
Ug_300 = np.zeros((7,12))
Ug_700 = np.zeros((7,12))
Vg_300 = np.zeros((7,12))
Vg_700 = np.zeros((7,12))
u_300 = np.zeros((7,12))
v_300 = np.zeros((7,12))
u_700 = np.zeros((7,12))
v_700 = np.zeros((7,12))


for k in range(7):
    for l in range(12):
        Z300[k,l] = z300[k+1,l+1]
        Z700[k,l] = z700[k+1,l+1]
        Ug_300[k,l] = Ug300[k+1,l+1]
        Ug_700[k,l] = Ug700[k+1,l+1]
        Vg_300[k,l] = Vg300[k+1,l+1]
        Vg_700[k,l] = Vg700[k+1,l+1]
        u_300[k,l] = u300[k+1,l+1]
        v_300[k,l] = v300[k+1,l+1]        
        u_700[k,l] = u700[k+1,l+1]
        v_700[k,l] = v700[k+1,l+1]  
        
        
        
        
        
x = np.linspace(322,333,12)
y = np.linspace(52,58,7)

X, Y = np.meshgrid(x, y)



fig, ax = plt.subplots()
ax.quiver(X,Y,Ug_300,Vg_300,color = 'r', width = 3E-3)
ax.quiver(X,Y,u_300,v_300,color = 'b', width = 3E-3)
CS300 = ax.contour(X, Y, Z300)
ax.clabel(CS300, inline=1, fontsize=10)
ax.set_title('Iso-contours, vents géostrophiques et horizontaux à 300hPa')



fig, ax = plt.subplots()
ax.quiver(X,Y,Ug_700,Vg_700,color = 'r', width = 3E-3)
ax.quiver(X,Y,u_700,v_700,color = 'b', width = 3E-3)
CS700 = ax.contour(X, Y, Z700)
ax.clabel(CS700, inline=1, fontsize=10)
ax.set_title('Iso-contours, vents géostrophiques et horizontaux à 700hPa')



## III - Vent Agéostrophique


###Question 1
#Evaluer le second terme du vent thermique

Omega300 = np.zeros((8,13))
Omega700 = np.zeros((8,13))
T300 = np.zeros((8,13))
T700 = np.zeros((8,13))

# On insère les valeurs dans des tableaux

a = 0
b = 1
for j in range(0,1260):
    if data[j,0] == 300:
        a = a+1
        Omega300[b,a] = data[j,5]
        T300[b,a] = data[j,3]
        if a == 12:
            a = 0
            b = b+1

a1 = 0
b1 = 1
for i in range(0,1260):
    if data[i,0] == 700:
        a1 = a1+1
        Omega700[b1,a1] = data[i,5]
        T700[b1,a1] = data[i,3]
        if a1 == 12:
            a1 = 0
            b1 = b1+1


#Initialisation du tableau avec les latitudes et longitudes

Tab = np.zeros((8,13))
x = 0
y = 0
for i in range(0,166,15):
    x = x+1
    Tab[0,x] = data[i,0]
    Omega300[0,x] = data[i,0]
    Omega700[0,x] = data[i,0]
    T300[0,x] = data[i,0]
    T700[0,x] = data[i,0]

for j in range(0,1259,180):
    y = y+1
    Tab[y,0] = data[j,1]
    Omega300[y,0] = data[j,1]
    Omega700[y,0] = data[j,1]
    T300[y,0] = data[j,1]
    T700[y,0] = data[j,1]


print('Omega à 300hPa', Omega300)
print('Omega à 700hPa', Omega700)
print('Température à 300hPa',T300)
print('Température à 700hPa',T700)

#On calcule rho grace à la loi des gaz parfaits
#On prend R = 287 J.kg-1.K-1

R = 287 #en J.kg-1.K-1

rho300 = np.zeros((8,13))
rho700 = np.zeros((8,13))

for k in range(1,8):
    for l in range(1,13):
        rho300[k,l] = 30000/(R*(T300[k,l]+273.15))
        rho700[k,l] = 70000/(R*(T700[k,l]+273.15))

print('rho à 300hPa', rho300)
print('rho à 700hPa', rho700)

#On calcule désormais la vitesse w
        
w300 = np.zeros((8,13))
w700 = np.zeros((8,13))

for k in range(1,8):
    for l in range(1,13):
        w300[k,l]=(Omega300[k,l]/(-g*rho300[k,l]))
        w700[k,l]=(Omega700[k,l]/(-g*rho700[k,l]))


print('w à 300hPa', w300)
print('w à 700hPa', w700)


#Calcul du deuixème terme de la contribution du vent thermique dans
#le repère (x,y,p)


utC2_300 = np.zeros((8,13))
vtC2_300 = np.zeros((8,13))
utC2_700 = np.zeros((8,13))
vtC2_700 = np.zeros((8,13))
for k in range(1,7):
    for l in range(1,12):
        utC2_300[k,l] = (-g*w300[k,l]/((f**2)*(T300[k,l]+273.15)))*((T300[k,l])/dx[k,l])
        vtC2_300[k,l] = (-g*w300[k,l]/((f**2)*(T300[k,l]+273.15)))*((T300[k,l])/dy)
        utC2_700[k,l] = (-g*w700[k,l]/((f**2)*(T700[k,l]+273.15)))*((T700[k,l])/dx[k,l])
        vtC2_700[k,l] = (-g*w700[k,l]/((f**2)*(T700[k,l]+273.15)))*((T700[k,l])/dy)  



###Question 2

#Normes de la deuxième composante des vents à 300 hPa et 700 hPa

VtC2_300 = np.zeros((7,12))
VtC2_700 = np.zeros((7,12))

for k in range(1,7):
    for l in range(1,12):
        VtC2_300[k,l] = np.sqrt((utC2_300[k,l])**2+(vtC2_300[k,l])**2)
        VtC2_700[k,l] = np.sqrt((utC2_700[k,l])**2+(vtC2_700[k,l])**2)


print('Norme du second terme du vent thermique C1 à 300hPa', VtC2_300)
print('Norme du second terme du vent thermique C1 à 700hPa', VtC2_700)


#contribution de vtc2 au vent agéostrophique total

Ert300 = np.zeros((7,12))
Ert700 = np.zeros((7,12))

for k in range(1,7):
    for l in range(1,12):
        Ert300[k,l] = (vh300[k,l]-vg300[k,l])/VtC2_300[k,l]*100
        Ert700[k,l] = (vh700[k,l]-vg700[k,l])/VtC2_700[k,l]*100
        


print("Ecart relatif 300", Ert300)
print("Ecart relatif 700", Ert700)
