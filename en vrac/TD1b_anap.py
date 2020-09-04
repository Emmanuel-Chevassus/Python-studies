# -*- coding: cp1252 -*-
import numpy as np
import matplotlib.pyplot as plt
from math import exp
# solution analytique pour le calcul de pression et masse volumique
# pour un profile de la temperature: T(z)= a*z + T0 (lineaire),
# la resolution verticale est del_z=250 m
# a est 0.0065 deg/metre jusqu'a 11000m, au-dessus 11 km A=0 donc isotherme!
nz=64
#
R_AIR=287.05
G=9.806
GovR=G/R_AIR
TZERO=273.15
TSURF=TZERO + 15.
PSURF=1000. * 100.
RHOSURF=PSURF/(R_AIR*TSURF)
# pression de surface en Pa
ZSURF=0.
# grille verticale si nz=64
DEL_Z=250.
DELZ05=DEL_Z*0.5
# refroidissement par metre (attention, ici > 0)
A=0.65*0.01
GovRa=GovR/A
GovRa_1=GovRa-1
#   definition des tableaux 
zm = np.empty([nz])
tm = np.empty([nz])
pana = np.empty([nz])
rhoana = np.empty([nz])
T_LAST =0.
P_LAST =0.
Z_LAST =0.
for k in range(nz):
        zm[k]= DEL_Z * (k+1) - DELZ05
        if zm[k] < 11000 : 
                tm[k] = TSURF - A*zm[k]
                pana[k] = PSURF*(1.0-A*zm[k]/TSURF)**GovRa
                rhoana[k] = RHOSURF*(1.0-A*zm[k]/TSURF)**GovRa_1
                T_LAST = tm[k]
                P_LAST = pana[k]
                Z_LAST = zm[k]             
        else :
                zz = zm[k] - Z_LAST
                tm[k] = T_LAST                                 # isotherme
                pana[k] = P_LAST * exp (-1. *zz * G/(R_AIR*T_LAST))
                rhoana[k] = pana[k] / (R_AIR*T_LAST)
#                              
#        print  k+1, zm[k], tm[k]-TZERO, rhoana[k], pana[k]
#        
with open("sol_analyt.dat", "w") as flw:
        for k in range(nz):
                pr_k = '{0:4d}'.format(int(k+1))
                pr_z = '{0:9.1f}'.format(float(zm[k]))
                pr_press = '{0:9.1f}'.format(float(pana[k]))                
                pr_rho = '{0:13.5e}'.format(float(rhoana[k]))
                print ("%5d %7.2f" %(k, rhoana[k]) )
                flw.write(pr_k + pr_z + pr_rho + pr_press +'\n')
# partie graphique
y = np.empty([nz])
x = np.empty([nz])               
for k in range(nz):
        y[k]=0.001*zm[k]        # from m to km
        x[k]=pana[k]*0.01       # from Pa to hPa
        
        #x[k]=tm[k] - TZERO     # activer pour tracer T(z)
        #x[k]=rhoana[k]         # activer pour tracer Rho(z)
# plot commands
# legende pour x, y et le titre 
# attention le symbole ° comme caractere ne marche pas 
plt.xlabel('p (hPa)')
# plt.xlabel('rho (kg/m3)')
# plt.xlabel('T in deg C')
plt.ylabel('z (km)')
plt.title("p(z) using dT/dz = -0.65 C/100m")
plt.plot(x,y)
plt.show()

                
