import numpy as np

Sigma = 26.    #  modifier aussi le nom du fichier resultat  XXXX

ns = 41                  # nb de salinite differente a traiter
rho = Sigma + 1000.

Sali0 = 35.
# selon Fieux
T0_f = 10.
A_f = 0.15
B_f = 0.78
RHO0_f = 1026.97
# selon Bougeault+Sardourny
RHO0_bs = 1026.97
T0_bs = 283.
A_bs = 1.7e-4
B_bs = 7.6e-4
RHO0_bs = 1028.
#
Sali = np.empty([ns])
T_f =  np.empty([ns])
T_bs =  np.empty([ns])
for k in range(ns):
        Sali[k] = (0.2* k + 29. )
        Tstar_f = (rho-RHO0_f) - B_f*(Sali[k]-Sali0) - 4.5E-3 * 10.
        T_f[k] = T0_f + Tstar_f/(-1. * A_f)        
#        Tstar = (rho/RHO0) -1. - 0.76e-3*(Sali[k]-Sali0)

        print  k, Sali[k], T_f[k]
#                                        XXXX
with open("outFieuxx.txt", "w") as flw:
        for k in range(ns):
                pr_S = '{0:7.1F}'.format(float(Sali[k]))
                pr_Tf = '{0:9.3f}'.format(float(T_f[k]))
#       print pr_z,rhom[k]
                flw.write(pr_S+pr_Tf+'\n')
                print (pr_S+pr_Tf)
