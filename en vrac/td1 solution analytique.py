import numpy as np
# solution analytique pour le calcul de pression et de la masse volumique
# pour un profile de la temp�rature: T(z)= A*z + T0 (lineaire),
# la resolution verticale est del_z=250 m
# A reste const sur tous les 16 km
nz=64
#
R_AIR=287.05         # Joule/K/kg
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
for k in range(nz):
        zm[k]= DEL_Z * (k+1) - DELZ05
        tm[k]= TSURF - A*zm[k]
        pana[k]=PSURF*(1.0-A*zm[k]/TSURF)**GovRa
        rhoana[k]=RHOSURF*(1.0-A*zm[k]/TSURF)**GovRa_1 
        print  k+1, zm[k], tm[k]-TZERO, rhoana[k], pana[k]
#        
with open("sol_analyt.dat", "w") as flw:
        for k in range(nz):
                pr_k = '{0:4d}'.format(int(k+1))
                pr_z = '{0:9.1f}'.format(float(zm[k]))
                pr_press = '{0:9.1f}'.format(float(pana[k]))                
                pr_rho = '{0:13.5e}'.format(float(rhoana[k]))
                print ("%5d %7.2f" %(k, rhoana[k]) )
                flw.write(pr_k + pr_z + pr_rho + pr_press +'\n')
                
