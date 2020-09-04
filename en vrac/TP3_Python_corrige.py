import scipy.io 
import numpy as np
import matplotlib.pyplot as plt
import math
#-------------------------------------------------------------------------------------------------------
#------------question 1---------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
# chargement des données :
mat = scipy.io.loadmat('Station_PDD_horaire_1995_2017.mat') 
CO=mat["CO"]
CO2=mat["CO2"]
Temp=mat["Temp"]
O3=mat["O3"]
temps=mat["temps_fractionne"]
mois=mat["mois"]
#
plt.figure('figure O3')
plt.title("Evolution de la concentration en ozone de 1995 à 2007 au sommet du puy de Dôme")
plt.plot(temps.transpose(),O3.transpose(),'-r')
plt.xlabel('Années')
plt.ylabel('Concentration en ozone en ppbv')
plt.show()
plt.savefig('figureO3.png')
#
plt.figure('figure CO')
plt.title("Evolution de la concentration en CO de 1995 à 2007 au sommet du puy de Dôme")
plt.plot(temps.transpose(),CO.transpose(),'-r')
plt.xlabel('Années')
plt.ylabel('Concentration en monoxide de carbone en ppbv')
plt.show()
plt.savefig('figureCO.png')
#
plt.figure('figure CO2')
plt.title("Evolution de la concentration en CO2 de 1995 à 2007 au sommet du puy de Dôme")
plt.plot(temps.transpose(),CO2.transpose(),'-r')
plt.xlabel('Années')
plt.ylabel('Concentration en dioxide de carbone en ppmv')
plt.show()
plt.savefig('figureCO2.png')
#
plt.figure('figure Temp')
plt.title("Evolution de la température de 1995 à 2007 au sommet du puy de Dôme")
plt.plot(temps.transpose(),Temp.transpose(),'-r')
plt.xlabel('Années')
plt.ylabel('Température en °C')
plt.show()
plt.savefig('figureTemp.png')
CO[temps<2002]=np.nan
#
plt.figure('figure CO modifié')
plt.title("Evolution de la concentration en CO de 1995 à 2007 au sommet du puy de Dôme")
plt.plot(temps.transpose(),CO.transpose(),'-r')
plt.xlabel('Années')
plt.ylabel('Concentration en monoxide de carbone en ppbv')
plt.show()
plt.savefig('figureCOmod.png')
O3[O3<=0]=np.nan
#
plt.figure('figure O3cor')
plt.title("Evolution de la concentration en ozone de 1995 à 2007 au sommet du puy de Dôme")
plt.plot(temps.transpose(),O3.transpose(),'-r')
plt.xlabel('Années')
plt.ylabel('Concentration en ozone en ppbv')
plt.show()
plt.savefig('figureO3cor.png')
# enregistrement des données corrigées :
M=np.concatenate((temps.transpose(),O3.transpose(),CO.transpose(),CO2.transpose(),Temp.transpose(),mois.transpose()),axis=1)
np.savetxt('test.txt', M, fmt='%13.8f   %8.4f  %10.6f  %10.6f  %9.5f    %2i')
#-------------------------------------------------------------------------------------------------------
#------------question 2---------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]
import scipy.io 
import numpy as np
import matplotlib.pyplot as plt
import math
Mok = np.loadtxt('test.txt')
temps=Mok[:,0]
O3=Mok[:,1]
CO=Mok[:,2]
CO2=Mok[:,3]
Temp=Mok[:,4]
Mois=Mok[:,5]
#
plt.figure('figure CO2versusCO')
plt.title("CO2 en fonction de CO")
plt.plot(CO,CO2,'+r')
plt.xlabel('CO en ppbv')
plt.ylabel('CO2 en ppmv')
plt.show()
plt.savefig('figureCO2versusCO.png')
#
plt.figure('figure CO2versusO3')
plt.title("CO2 en fonction de O3")
plt.plot(O3,CO2,'+r')
plt.xlabel('O3 en ppbv')
plt.ylabel('CO2 en ppmv')
plt.show()
plt.savefig('figureCO2versusO3.png')
#
plt.figure('figure CO2versusTemp')
plt.title("CO2 en fonction de la température")
plt.plot(Temp,CO2,'+r')
plt.xlabel('Température en °C')
plt.ylabel('CO2 en ppmv')
plt.show()
plt.savefig('figureCO2versusTemp.png')
#
plt.figure('figure COversusO3')
plt.title("CO en fonction de O3")
plt.plot(O3,CO,'+r')
plt.xlabel('O3 en ppbv')
plt.ylabel('CO en ppbv')
plt.show()
plt.savefig('figureCOversusO3.png')
#
plt.figure('figure COversusTemp')
plt.title("CO en fonction de la température")
plt.plot(Temp,CO,'+r')
plt.xlabel('Température en °C')
plt.ylabel('CO en ppbv')
plt.show()
plt.savefig('figureCOversusTemp.png')
#
plt.figure('figure O3versusTemp')
plt.title("O3 en fonction de la température")
plt.plot(Temp,O3,'+r')
plt.xlabel('Température en °C')
plt.ylabel('O3 en ppbv')
plt.show()
plt.savefig('figureO3versusTemp.png')
#-------------------------------------------------------------------------------------------------------
#------------question 3---------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
x=Temp[np.logical_and(~np.isnan(Temp),~np.isnan(CO2))]
y=CO2[np.logical_and(~np.isnan(Temp),~np.isnan(CO2))]
N=len(x)
delta=N*np.sum(x**2)-(np.sum(x))**2
a=(N*np.sum(x*y)-np.sum(x)*np.sum(y))/delta
b=(np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/delta
print('y=',a,'x+',b)
coef=np.polyfit(x, y, 1)
print('coef=',coef)
cor=np.corrcoef(x,y)
print('correlation=',cor)
tabx=np.array([-20.,30.])
taby=a*tabx+b
plt.figure('figure CO2versusTempfit')
plt.title("CO2 en fonction de la température")
plt.plot(Temp,CO2,'+r')
plt.plot(tabx,taby,'-b')
plt.xlabel('Température en °C')
plt.ylabel('CO2 en ppmv')
plt.show()
plt.savefig('figureCO2versusTempfit.png')
#-------------------------------------------------------------------------------------------------------
#------------question 4---------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
Temp2=Temp[np.logical_and(~np.isnan(Temp),~np.isnan(temps))]
temps2=temps[np.logical_and(~np.isnan(Temp),~np.isnan(temps))]
coef=np.polyfit(temps2,Temp2, 1)
print('tendance température y=',coef[0],'x',coef[1])
cor=np.corrcoef(temps2,Temp2)
print('correlation température/temps =',cor)
tabx=np.array([np.min(temps2),np.max(temps2)])
taby=coef[0]*tabx+coef[1]
plt.figure('figure EvolTempt')
plt.title("Evolution temporelle de la température")
plt.plot(temps2,Temp2,'+r')
plt.plot(tabx,taby,'-b')
plt.ylabel('Température en °C')
plt.xlabel('temps en années')
plt.show()
plt.savefig('figureEvolTemp.png')
#
CObis=CO[np.logical_and(~np.isnan(CO),~np.isnan(temps))]
temps3=temps[np.logical_and(~np.isnan(CO),~np.isnan(temps))]
coef=np.polyfit(temps3,CObis, 1)
print('tendance CO y=',coef[0],'x',coef[1])
cor=np.corrcoef(temps3,CObis)
print('correlation CO/temps =',cor)
tabx=np.array([np.min(temps3),np.max(temps3)])
taby=coef[0]*tabx+coef[1]
plt.figure('figure EvolCOt')
plt.title("Evolution temporelle de la concentration en monoxide de carbone")
plt.plot(temps3,CObis,'+r')
plt.plot(tabx,taby,'-b')
plt.ylabel('CO en ppbv ')
plt.xlabel('temps en années')
plt.show()
plt.savefig('figureEvolCO.png')
#
CO2bis=CO2[np.logical_and(~np.isnan(CO2),~np.isnan(temps))]
temps4=temps[np.logical_and(~np.isnan(CO2),~np.isnan(temps))]
coef=np.polyfit(temps4,CO2bis, 1)
print('tendance CO2 y=',coef[0],'x',coef[1])
cor=np.corrcoef(temps4,CO2bis)
print('correlation CO2/temps =',cor)
tabx=np.array([np.min(temps4),np.max(temps4)])
taby=coef[0]*tabx+coef[1]
plt.figure('figure EvolCO2t')
plt.title("Evolution temporelle de la concentration en dioxide de carbone")
plt.plot(temps4,CO2bis,'+r')
plt.plot(tabx,taby,'-b')
plt.ylabel('CO2 en ppmv ')
plt.xlabel('temps en années')
plt.show()
plt.savefig('figureEvolCO2.png')
#
O3bis=O3[np.logical_and(~np.isnan(O3),~np.isnan(temps))]
temps5=temps[np.logical_and(~np.isnan(O3),~np.isnan(temps))]
coef=np.polyfit(temps5,O3bis, 1)
print('tendance O3 y=',coef[0],'x',coef[1])
cor=np.corrcoef(temps5,O3bis)
print('correlation O3/temps =',cor)
tabx=np.array([np.min(temps5),np.max(temps5)])
taby=coef[0]*tabx+coef[1]
plt.figure('figure EvolO3t')
plt.title("Evolution temporelle de la concentration en ozone")
plt.plot(temps5,O3bis,'+r')
plt.plot(tabx,taby,'-b')
plt.ylabel('O3 en ppbv ')
plt.xlabel('temps en années')
plt.show()
plt.savefig('figureEvolO3.png')
#-------------------------------------------------------------------------------------------------------
#------------question 5---------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------
mois4=Mois[np.logical_and(~np.isnan(CO2),~np.isnan(temps))]
CO2_mensuel=np.zeros(12)
for i in range(1,13) :
    ind=np.where(mois4==i)
    print(ind)
    CO2_mensuel[i-1]=np.mean(CO2bis[ind])
print(CO2_mensuel)
residu=np.zeros(len(CO2bis))
for i in range(0,len(CO2bis)):
    residu[i]=CO2bis[i]-CO2_mensuel[int(mois4[i])-1]
coef=np.polyfit(temps4,residu, 1)
print('tendance CO2 residu y=',coef[0],'x',coef[1])
cor=np.corrcoef(temps4,residu)
print('correlation CO2residu/temps =',cor)
tabx=np.array([np.min(temps4),np.max(temps4)])
taby=coef[0]*tabx+coef[1]
plt.figure('figure EvolCO2residut')
plt.title("Evolution temporelle de la concentration en dioxide de carbone sans le cycle saisonnier")
plt.plot(temps4,residu,'+r')
plt.plot(tabx,taby,'-b')
plt.ylabel('CO2 résiduel en ppmv ')
plt.xlabel('temps en années')
plt.show()
plt.savefig('figureEvolCO2residu.png')   
#
mois5=Mois[np.logical_and(~np.isnan(Temp),~np.isnan(temps))]
Temp_mensuel=np.zeros(12)
for i in range(1,13) :
    ind=np.where(mois5==i)
    Temp_mensuel[i-1]=np.mean(Temp2[ind])
residu2=np.zeros(len(Temp2))
for i in range(0,len(Temp2)):
    residu2[i]=Temp2[i]-Temp_mensuel[int(mois5[i])-1]
coef=np.polyfit(temps2,residu2, 1)
print('tendance temperature residu y=',coef[0],'x',coef[1])
cor=np.corrcoef(temps2,residu2)
print('correlation Tempresidu/temps =',cor)
tabx=np.array([np.min(temps2),np.max(temps2)])
taby=coef[0]*tabx+coef[1]
plt.figure('figure EvolTempresidut')
plt.title("Evolution temporelle de la température sans le cycle saisonnier")
plt.plot(temps2,residu2,'+r')
plt.plot(tabx,taby,'-b')
plt.ylabel('Température résiduelle en °C ')
plt.xlabel('temps en années')
plt.show()
plt.savefig('figureEvolTempresidu.png')  