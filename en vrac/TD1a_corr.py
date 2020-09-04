import numpy as np
# nz= 64 niveaux pour le calcul du prof de T, rho, p dans une atmosphere
# avec T(z)= a*z + T0 (lineaire), la resolution verticale est del_z=250 m
# a reste const sur tous les 16 km
nz=64
#
R=287.05
G=9.806
TZERO=273.16
TSURF=TZERO + 15.
PSURF=1000. * 100.
# pression de surface en Pa
ZSURF=0.
# grille verticale si nz=64
DEL_Z=250.
DELZ05=DEL_Z*0.5
# refroidissement par metre
A=-0.65*0.01          
#               alternatif au call numpy.empty 
zm =[]
tm =[]
plev =[]
rhom =[]
for k in range(nz):
        zm_val= (DEL_Z * k + DELZ05)
        zm.append(zm_val)
        tm_val=TSURF + A*(DEL_Z*(k+1)-DELZ05 )        
        tm.append(tm_val)
        plev.append(0)
        rhom.append(0)
        print( "%5d %8.1f %7.2f" % (k,zm[k],tm[k]) )
#
#zm = np.empty([nz])
#tm = np.empty([nz])
#plev = np.empty([nz])
#rhom = np.empty([nz])
t=TSURF
p=PSURF       
for k in range(nz):
        Tmoy = tm[k]
        rhomoy = p/(R * Tmoy)              
        dp1 = -(G*rhomoy)*DEL_Z
        p1 = p + dp1
        # pas correctif pour rho  
        rhomoy2 = p1 /(R * Tmoy)       
        rhofin=(rhomoy+rhomoy2)*0.5
        dp=-(G*rhofin)*DEL_Z
        p = p + dp            
        plev[k] = p

        rhom[k]=plev[k]/(R * tm[k])	 
        print  k+1, (k+1)*DEL_Z, Tmoy-TZERO, rhomoy, p*0.01
#        
with open("out_corr.dat", "w") as flw:
        for k in range(nz):
                pr_k = '{0:4d}'.format(int(k+1))
                pr_z = '{0:9.3f}'.format(float(DEL_Z*(k+1)*0.001))
                pr_press = '{0:9.3f}'.format(float(plev[k])*0.01)                
                pr_rho = '{0:13.5e}'.format(float(rhom[k]))
                print ("%5d %7.2f" %(k, rhom[k]) )
                flw.write(pr_k + pr_z + pr_rho + pr_press +'\n')
                
