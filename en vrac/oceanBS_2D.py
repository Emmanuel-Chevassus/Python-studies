import numpy as np

# utiliser l'approximation selon le bouquin de Bougeault et Sardourny

ns = 41       # nb de salinites differentes a traiter
nrho = 9      # nb de sigma (ou rho) differentes
Sali0 = 35.

# selon Bougeault+Sardourny
RHO0_bs = 1026.97
T0_bs = 283.
A_bs = 1.7e-4
B_bs = 7.6e-4
RHO0_bs = 1028.
#
Sali = np.empty([ns])
sig =  np.empty([nrho])
T_bs =  np.empty([nrho,ns])
for ir in range(nrho):
        sig[ir] = ir*1. + 21.
        print ir, sig[ir]
        rho = sig[ir] + 1000.
        for k in range(ns):
       
                Sali[k] = (0.2* k + 29. )
                Tstar = (rho/RHO0_bs) -1. - B_bs * (Sali[k]-Sali0)        
                T_bs[ir,k] = T0_bs + Tstar/(-1. * A_bs)  - 273.15
#                print  k, sig[ir], Sali[k], T_bs[ir,k]
with open("test.txt", "w") as flw:
        for k in range(ns):
#                prt_S = ('{0:8.2f}'.format(float(Sali[k])))
#                flw.write(prt_S)                
                flw.write('{0:8.2f}'.format(float(Sali[k])))

                for ir in range(nrho):
                        flw.write('{0:9.3f}'.format(float(T_bs[ir,k])))
                flw.write('\n')
        
