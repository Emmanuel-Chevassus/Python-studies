import scipy.io 
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
#-----------------------------------------------------------------------------------------------------------------
#------------partie II : Analyse statistique de la distribution des scories des puys de La Vache et de Lassolas---
#-----------------------------------------------------------------------------------------------------------------
# chargement des données :
mat = scipy.io.loadmat('puy_vache_lassolas.mat') 
WT1=mat["WT1"] # fréquence absolue échantillon 1
WT2=mat["WT2"] # fréquence absolue échantillon 2
WT3=mat["WT3"] # fréquence absolue échantillon 3
WT4=mat["WT4"] # fréquence absolue échantillon 4
PHI=mat["PHI"] # diamètres équivalents
# question a) :
# calcul des fréquences relatives :
WTQ1_rel = WT1/np.sum(WT1)*100
WTQ2_rel = WT2/np.sum(WT2)*100
WTQ3_rel = WT3/np.sum(WT3)*100
WTQ4_rel = WT4/np.sum(WT4)*100
# calcul des fréquences cumulées relatives :
WTQ1_cum=np.zeros(len(WTQ1_rel))
WTQ2_cum=np.zeros(len(WTQ2_rel))
WTQ3_cum=np.zeros(len(WTQ3_rel))
WTQ4_cum=np.zeros(len(WTQ4_rel))
for i in range(0,len(PHI)) :
    if i==0 :
        WTQ1_cum[i] = WTQ1_rel[i]
        WTQ2_cum[i] = WTQ2_rel[i]
        WTQ3_cum[i] = WTQ3_rel[i]
        WTQ4_cum[i] = WTQ4_rel[i]
    else :
        WTQ1_cum[i] = WTQ1_cum[i-1]+WTQ1_rel[i]
        WTQ2_cum[i] = WTQ2_cum[i-1]+WTQ2_rel[i]
        WTQ3_cum[i] = WTQ3_cum[i-1]+WTQ3_rel[i]
        WTQ4_cum[i] = WTQ4_cum[i-1]+WTQ4_rel[i]
# question b) détermination graphique des percentiles :
plt.figure('Freq_cum', figsize=[25.6, 19.2])
plt.title("Fréquences cumulées relatives pour les 4 jeux de données du puy de la Vache et de Lassolas",fontsize='xx-large')
plt.plot(PHI,WTQ1_cum, '-r',linewidth=3.0,label="1")
plt.plot(PHI,WTQ2_cum, '-b',linewidth=3.0,label="2")
plt.plot(PHI,WTQ3_cum, '-g',linewidth=3.0,label="3")
plt.plot(PHI,WTQ4_cum, '-k',linewidth=3.0,label="4")
plt.xlabel('PHI=-log2(d) où d est en mm',fontsize='xx-large')
plt.ylabel('Fréquences cumulées croissantes en %',fontsize='xx-large')
plt.ylim([0,100])
plt.xlim([-7.5,7.5])
plt.legend()
plt.grid(True)
plt.xticks(np.arange(-7.5,7.7,0.4),fontsize='large')
plt.yticks(np.arange(0,101,2),fontsize='large')
plt.xlabel
plt.show()
plt.savefig('Freq_cum.png')
# question d) réalisation des histogrammes :
plt.figure('Bar1', figsize=[25.6, 19.2])
plt.subplot(2,2,1)
plt.title("Histogramme des diamètres équivalents pour la série 1",fontsize='xx-large')
plt.bar(PHI, WTQ1_rel,width=0.5,align='center')
#plt.xlabel('PHI=-log2(d) où d est en mm',fontsize='xx-large')
plt.ylabel('Fréquences relatives en %',fontsize='xx-large')
plt.xlim([-7.5,7.5])
plt.ylim([0,30])
plt.xticks(np.arange(-7.5,7.7,1.),fontsize='x-large')          
plt.yticks(np.arange(0,32,5),fontsize='x-large')
plt.grid(axis='y')
#
plt.subplot(2,2,2)
plt.title("Histogramme des diamètres équivalents pour la série 2",fontsize='xx-large')
plt.bar(PHI, WTQ2_rel,width=0.5,align='center')
#plt.xlabel('PHI=-log2(d) où d est en mm',fontsize='xx-large')
plt.ylabel('Fréquences relatives en %',fontsize='xx-large')
plt.xlim([-7.5,7.5])
plt.ylim([0,30])
plt.xticks(np.arange(-7.5,7.7,1.),fontsize='x-large')
plt.yticks(np.arange(0,32,5),fontsize='x-large')
plt.grid(axis='y')
#
plt.subplot(2,2,3)
plt.title("Histogramme des diamètres équivalents pour la série 3",fontsize='xx-large')
plt.bar(PHI, WTQ3_rel,width=0.5,align='center')
plt.xlabel('PHI=-log2(d) où d est en mm',fontsize='xx-large')
plt.ylabel('Fréquences relatives en %',fontsize='xx-large')
plt.xlim([-7.5,7.5])
plt.ylim([0,30])
plt.xticks(np.arange(-7.5,7.7,1.),fontsize='x-large')
plt.yticks(np.arange(0,32,5),fontsize='x-large')
plt.grid(axis='y')
#
plt.subplot(2,2,4)
plt.title("Histogramme des diamètres équivalents pour la série 4",fontsize='xx-large')
plt.bar(PHI, WTQ4_rel,width=0.5,align='center')
plt.xlabel('PHI=-log2(d) où d est en mm',fontsize='xx-large')
plt.ylabel('Fréquences relatives en %',fontsize='xx-large')
plt.xlim([-7.5,7.5])
plt.ylim([0,30])
plt.xticks(np.arange(-7.5,7.7,1.),fontsize='x-large')
plt.yticks(np.arange(0,32,5),fontsize='x-large')
plt.grid(axis='y')
plt.show()
plt.savefig('Bar_toutes_series.png')
# question e)
percentiles=np.array([5.,16.,25.,50.,75.,84.,95.])
pserie=np.zeros([len(percentiles),4])
f1=interp1d(WTQ1_cum,PHI[:,0])
pserie[:,0]=f1(percentiles)
f2=interp1d(WTQ2_cum,PHI[:,0])
pserie[:,1]=f2(percentiles)
f3=interp1d(WTQ3_cum,PHI[:,0])
pserie[:,2]=f3(percentiles)
f4=interp1d(WTQ4_cum,PHI[:,0])
pserie[:,3]=f4(percentiles)
moy=np.zeros(4)
moyg=np.zeros(4)
ecg=np.zeros(4)
ecs=np.zeros(4)
skg=np.zeros(4)
sk=np.zeros(4)
kurg=np.zeros(4)
for i in range(0,4):
    moy[i]=(pserie[5,i]+pserie[1,i])/2
    moyg[i]=(pserie[5,i]+pserie[3,i]+pserie[1,i])/3
    ecg[i]=(pserie[5,i]-pserie[1,i])/4+(pserie[6,i]-pserie[0,i])/6.6
    ecs[i]=(pserie[5,i]-pserie[1,i])/2
    skg[i]=(pserie[5,i]-2*pserie[3,i]+pserie[1,i])/(2*(pserie[5,i]-pserie[1,i]))+(pserie[6,i]-2*pserie[3,i]+pserie[0,i])/(2*(pserie[6,i]-pserie[0,i]))
    sk[i]=(pserie[5,i]-pserie[3,i]+pserie[1,i])/ecs[i]
    kurg[i]=(pserie[6,i]-pserie[0,i])/(2.44*(pserie[4,i]-pserie[2,i]))
print('médianes=',pserie[3,:])
print('moyennes graphiques=',moy)
print('écart-type graphique=',ecg)
print('écart-type standard=',ecs)
print('skewness graphique=',skg)
print('skewness=',sk)
print('kurtosis graphique=',kurg)
#-----------------------------------------------------------------------------------------------------------------
#------------partie III : Etude de la texture de fragments de magma du Stromboli-----------------------------------
#-----------------------------------------------------------------------------------------------------------------
all = [var for var in globals() if var[0] != "_"]
for var in all:
    del globals()[var]
import scipy.io 
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d  
# chargement des données :
mat2 = scipy.io.loadmat('vesicle_stromboli.mat') 
p=mat2["p"]
Orientation=mat2["Orientation"]
Grossissement=mat2["Grossissement"]
EqDi=mat2["EqDi"]
b=mat2["b"]
A=mat2["A"]
a=mat2["a"]
ind1=np.where(Grossissement==1)
ind2=np.where(Grossissement==2)
ind3=np.where(Grossissement==3)
# rapport d'aspect :
AR1 = b[ind1]/a[ind1]
AR2 = b[ind2]/a[ind2]
AR3 = b[ind3]/a[ind3]
AR=[np.mean(AR1),np.mean(AR2),np.mean(AR3)]
print('crystal')
print('AR=',AR)
# coef d'élongation :
e1 = (a[ind1]-b[ind1])/(a[ind1]+b[ind1])
e2 = (a[ind2]-b[ind2])/(a[ind2]+b[ind2])
e3 = (a[ind3]-b[ind3])/(a[ind3]+b[ind3])
e=[np.mean(e1),np.mean(e2),np.mean(e3)]
print('e=',e)
# facteur de forme :
sf1 = 4*math.pi*A[ind1]/(p[ind1]**2)
sf2 = 4*math.pi*A[ind2]/(p[ind2]**2)
sf3 = 4*math.pi*A[ind3]/(p[ind3]**2) 
sf=[np.mean(sf1),np.mean(sf2),np.mean(sf3)]
print('sf=',sf)
# régularité :
rg1 = A[ind1]/(math.pi*a[ind1]*b[ind1])
rg2 = A[ind2]/(math.pi*a[ind2]*b[ind2])
rg3 = A[ind3]/(math.pi*a[ind3]*b[ind3])
rg=[np.mean(rg1),np.mean(rg2),np.mean(rg3)]
print('rg=',rg)
#########
# figures :
plt.figure('AR_rg', figsize=[25.6, 19.2])
plt.title("Rapport d'aspect en fonction du paramètre de régularité",fontsize='xx-large')
plt.plot(rg1,AR1, '+r',label="Grossissement 1")
plt.plot(rg2,AR2, '+b',label="Grossissement 2")
plt.plot(rg3,AR3, '+g',label="Grossissement 3")
plt.xlabel('paramètre de régularité',fontsize='xx-large')
plt.ylabel("rapport d'aspect",fontsize='xx-large')
plt.legend(loc=2,fontsize='xx-large')
xval,labelx=plt.xticks()
plt.xticks(xval,fontsize='xx-large')
yval,labely=plt.yticks()
plt.yticks(yval,fontsize='xx-large')
plt.grid(True)
plt.show()
plt.savefig('AR_rg.png')
#
plt.figure('e_rg', figsize=[25.6, 19.2])
plt.title("Coefficient d'élongation en fonction du paramètre de régularité",fontsize='xx-large')
plt.plot(rg1,e1, '+r',label="Grossissement 1")
plt.plot(rg2,e2, '+b',label="Grossissement 2")
plt.plot(rg3,e3, '+g',label="Grossissement 3")
plt.xlabel('paramètre de régularité',fontsize='xx-large')
plt.ylabel("coefficient d'élongation",fontsize='xx-large')
plt.legend(loc=2,fontsize='xx-large')
xval,labelx=plt.xticks()
plt.xticks(xval,fontsize='xx-large')
yval,labely=plt.yticks()
plt.yticks(yval,fontsize='xx-large')
plt.grid(True)
plt.show()
plt.savefig('e_rg.png')
#
plt.figure('sf_rg', figsize=[25.6, 19.2])
plt.title("Facteur de forme en fonction du paramètre de régularité",fontsize='xx-large')
plt.plot(rg1,sf1, '+r',label="Grossissement 1")
plt.plot(rg2,sf2, '+b',label="Grossissement 2")
plt.plot(rg3,sf3, '+g',label="Grossissement 3")
plt.xlabel('paramètre de régularité',fontsize='xx-large')
plt.ylabel("facteur de forme",fontsize='xx-large')
plt.legend(loc=2,fontsize='xx-large')
xval,labelx=plt.xticks()
plt.xticks(xval,fontsize='xx-large')
yval,labely=plt.yticks()
plt.yticks(yval,fontsize='xx-large')
plt.grid(True)
plt.show()
plt.savefig('sf_rg.png')