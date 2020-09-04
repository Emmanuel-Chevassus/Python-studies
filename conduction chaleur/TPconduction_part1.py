import numpy as np
from conduction_part1 import *
import matplotlib.pyplot as plt
# question c
# pour le cuivre
a_cuivre=114E-6
tfcuivre,tcuivre,Tcuivre=conduction1(a_cuivre)
# pour le verre
a_verre=0.58E-6
tfverre,tverre,Tverre=conduction1(a_verre)
print('temps mis pour atteindre la stationnarité pour le cuivre=',tfcuivre,'secondes')
print('temps mis pour atteindre la stationnarité pour le verre=',tfverre,'secondes')
abscisse=np.array([0.01*i for i in range(101)])
#
plt.figure('figure ii')
plt.title("Température d'équilibre d'une barre de 1 m")
plt.plot(abscisse,Tverre[-1,:],'r',label="verre")
plt.plot(abscisse,Tcuivre[-1,:],'b+',label="cuivre")
plt.xlabel('longueur de la barre en mètre')
plt.ylabel('température en °C')
plt.legend()
plt.show()
plt.savefig('figureii.png')
#
plt.figure('figure iii')
plt.title("Evolution de la température du milieu de la barre au cours du temps")
plt.plot(tverre,Tverre[:,49],'r',label="verre")
plt.plot(tcuivre,Tcuivre[:,49],'b+',label="cuivre")
plt.xlabel('temps en secondes')
plt.ylabel('température en °C')
plt.legend()
plt.show()
plt.savefig('figureiii.png')
#
plt.figure('figure iv1')
plt.title("Evolution de la température de la barre de cuivre")
tcuivre=tcuivre/(60.*60.)
plt.pcolor(abscisse,tcuivre,Tcuivre)
plt.ylabel('temps en heures')
plt.xlabel('longueur de la barre en mètre')
cbar=plt.colorbar()
cbar.set_label('Température en °C')
plt.show()
plt.savefig('figureiv_cuivre.png')
#
plt.figure('figure iv2')
plt.title("Evolution de la température de la barre de verre")
tverre=tverre/(60.*60.)
plt.pcolor(abscisse,tverre,Tverre)
plt.ylabel('temps en heures')
plt.xlabel('longueur de la barre en mètre')
cbar=plt.colorbar()
cbar.set_label('Température en °C')
plt.show()
plt.savefig('figureiv_verre.png')
