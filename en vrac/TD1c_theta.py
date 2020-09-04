import numpy as np
from math import exp
# solution analytique pour le calcul de pression et masse volumique
# pour un profile de la temperature: T(z)= a*z + T0 (lineaire),
# la resolution verticale est del_z=250 m
# a est 0.0065 deg/metre jusqu'a 11000m, au-dessus 11 km A=0 donc isotherme!
#
#
# et la temperature potentielle theta

nz=64
#
R_AIR=287.05
CP= 1005.
RsurCP=R_AIR/CP
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
theta = np.empty([nz])
for k in range(nz):
        zm[k]= DEL_Z * (k+1) - DELZ05
        if zm[k] < 11000 : 
                tm[k] = TSURF - A*zm[k]
                pana[k] = PSURF*(1.0-A*zm[k]/TSURF)**GovRa
                rhoana[k] = RHOSURF*(1.0-A*zm[k]/TSURF)**GovRa_1
                theta[k] = tm[k] * (1000.*100/pana[k]) ** RsurCP
                T_LAST = tm[k]
                P_LAST = pana[k]
                Z_LAST = zm[k]
        else :
                zz = zm[k] - Z_LAST
                tm[k] = T_LAST                                 # isotherme
                pana[k] = P_LAST * exp (-1. *zz * G/(R_AIR*T_LAST))
                rhoana[k] = pana[k] / (R_AIR*T_LAST)
                theta[k] = tm[k] * (1000.*100/pana[k]) ** RsurCP
#                              
        print  (k+1, zm[k], tm[k], theta[k], pana[k])
#        
with open("thetaout.dat", "w") as flw:
        flw.write (" k      Z(m)     p(hPa)    T(K)   THETA(K) \n" )
        for k in range(nz):
                pr_k = '{0:4d}'.format(int(k+1))
                pr_z = '{0:9.3f}'.format(float(zm[k])*.001)       # convert m in km 
                pr_press = '{0:9.1f}'.format(float(0.01*pana[k]))                
                pr_tem = '{0:10.2f}'.format(float(tm[k]))
                pr_theta = '{0:10.2f}'.format(float(theta[k]))
                print ("%5d %7.2f" %(k, theta[k]) )
                flw.write(pr_k + pr_z + pr_press + pr_tem + pr_theta + '\n')
                
