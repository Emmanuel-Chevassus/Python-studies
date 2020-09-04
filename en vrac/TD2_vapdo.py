import numpy as np
from math import exp
# solution analytique pour le calcul de pression et masse volumique
# pour un profile de la temperature: T(z)= a*z + T0 (lineaire),
# la resolution verticale est del_z=250 m
# a est 0.0065 deg/metre jusqu'a 11000m, au-dessus 11 km A=0 donc isotherme!
#
#  calcul du rapport de melange  (concentration massique) de la vapeur d'eau
#  suppose que l'humidite est 50 pourcent
# 

nz=64
HUM_REL = 0.5               # 50% = l'humidite relative
#
R_AIR=287.05
CP= 1005.
RsurCP=R_AIR/CP
G=9.806
GovR=G/R_AIR
TZERO=273.15
TSURF=TZERO + 15.           # temperature a la surface = 15 degC
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
e = np.empty([nz])
qv = np.empty([nz])
T_LAST =99999.
P_LAST =99999.
Z_LAST =99999.
for k in range(nz):
        zm[k]= DEL_Z * (k+1) - DELZ05
        if zm[k] < 11000 : 
                tm[k] = TSURF - A*zm[k]                # tl is in Kelvin
                pana[k] = PSURF*(1.0-A*zm[k]/TSURF)**GovRa
                T_LAST = tm[k]
                P_LAST = pana[k]
                Z_LAST = zm[k]
        else :
                zz = zm[k] - Z_LAST
                tm[k] = T_LAST                                 # isotherme
                pana[k] = P_LAST * exp (-1. *zz * G/(R_AIR*T_LAST))

# calcul de la pression saturante pour la temperature tm
        t_in_Cel = tm[k] - TZERO
        val_expo = ( 17.27 * t_in_Cel / tm[k] )                                        
        # selon la formule de Tetens
        esat = 6.1078 * exp(val_expo)
        e[k] = HUM_REL *esat
        qv[k] = e[k]/(pana[k]*0.01-e[k])*0.622
        
                
#                              
        print  k+1, zm[k], tm[k], pana[k], esat
#        
with open("vapeur_out.dat", "w") as flw:
        flw.write ("    Z(km)      T(K)     p(hPa)    e(hPa)     qvap (g/kg) \n" )
        for k in range(nz):
                pr_k = '{0:4d}'.format(int(k+1))
                pr_z = '{0:9.1f}'.format(float(zm[k]))
                pr_press = '{0:9.1f}'.format(float(0.01*pana[k]))                
                pr_tem = '{0:10.2f}'.format(float(tm[k]))
                pr_evap = '{0:10.4f}'.format(float(e[k]))
                pr_qv = '{0:12.4f}'.format(float(qv[k])*1000.)
                print ("%5d %9.5f" %(k, e[k]) )
                flw.write(pr_k + pr_z + pr_tem + pr_press +pr_evap +pr_qv + '\n')
                
