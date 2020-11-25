from numpy import *
from math import *
import matplotlib.pyplot as plt

########################Fonction de calcul de l'intégrale

def calc_aire(tab,pas):
    l = len(tab)
    aire_tot = 0
    Aires = empty((l,1),float)

    for i in range(l-1):
        c1 = tab[i,1]
        c2 = tab[i+1,1]
        aire = c1*pas+(c2-c1)*pas/2
        Aires[i] = aire
        aire_tot = aire_tot + aire
    return aire_tot

#######################Question 1

#Tableau contenant les paramètres
params = array([[2900,72,3],[0.03,0.16,0.36],[0.26,0.2,0.3]])

#Initialisation du tableau de distribution
tableau_N = empty((0,2),float)

#On établit les limites inférieures et supérieures du rayon des aérosols secs et le pas
min = 0.001
max = 1
pas = 0.0001

#Calcul de notre distribution en fonction de rAP
for rAP in arange(min,max,pas):
    N = 0
    #On boucle pour les 3 modes
    for i in range(len(params)):
    
        Ni = params[0,i]*1e6            #On récupère Ni dans le tableau de paramètres, qu'on traduit en m-3
        Ri = params[1,i]                #On récupère Ri
        log_ecarttypei = params[2,i]    #On récupère le log écart-type
    
        #On additionne la valeur correspondant aux 3 modes à chaque itération
        N = N + Ni/(sqrt(2*pi)*log_ecarttypei)*exp(-log((rAP)/Ri)**2/(2*log_ecarttypei**2))
        
    #On ajoute au tableau une ligne des valeurs de rAP et du N correspondant
    tableau_N = append(tableau_N, array([[rAP,N]]), axis=0)  #On ajoute une ligne à tableau_N contenant rAp et N
  

#Calcul de l'intégrale en utilisant la fonction calc_aire définit plus haut
n1 = calc_aire(tableau_N, pas)

#Affichage

print("n1 = ",str(n1))
plt.semilogx(tableau_N[:,0],tableau_N[:,1],label="Distribution aérosols secs")
plt.xlabel("Rayon (um)")
plt.ylabel("Nombre aérosols par m^3")
plt.title("Distribution population aérosols secs en fonction de leur rayon")

#######################Question 2

sigma = 73e-3   #Tension de surface (N.m-1)
R = 461.51      #Constante spécifique (J.kg-1.K-1)
T = 273.15+20   #Température (K)
rho_w = 1000    #Masse volumique de l'eau (kg.m-3)
rho_s = 1780    #Masse volumique du sulfate d'ammonium (kg.m-3)
nu = 3          #Nombre d'ions
phi = 1         #Coefficient osmotique
eps = 0.1       #Solubilité
M_s = 132       #Masse molaire du sulfate d'ammonium (g.mol-1)
M_w = 18        #Masse molaire de l'eau (g.mol-1)
s = 0.5/100     #Sursaturation

#Calcul des termes
A = (2*sigma)/(R*T*rho_w)
B = (nu*phi*eps*rho_s*M_w)/(M_s*rho_w)
D = (2*B**2*A-6*B*A*s)/(3*B*s**2-3*B**2*s)
E = 3*B*A**2/(3*B*s**2-3*B**2*s)

#Calcul du rayon critique d'activation
ac = -D/2+sqrt(D**2/4-E)

#Calcul du rayon critique de l'aérosol sec
rnc = (ac**3*(A-s*ac)/(A+ac*(B-s)))**(1/3)

print("A = ",str(A))
print("B = ",str(B))
print("D = ",str(D))
print("E = ",str(E))
print("ac = ",str(ac))
print("rnc = ",str(rnc))

#######################Question 3

#On récupère dans un tableau les valeurs de distribution correspondant à un rayon inférieur à rnc
pop_CCN = tableau_N[where(tableau_N[:,0]>rnc*1e6)]

#Affichage
plt.semilogx(pop_CCN[:,0],pop_CCN[:,1],label="Distribution aérosols CCN",linewidth="5")
plt.legend()

#Calcul de l'intégrale
n2 = calc_aire(pop_CCN, pas)

print("n2 = ",str(n2))

#Pourcentage de la population possédant des capacités CCN
print("% = ",str(n2/n1))

#####################Question 4

k = 0.9     #Constante k empirique
s = 1/100   #Sursaturation

Nccns = []
i = 0

#On teste pour différentes valeurs de C (intervalle donné dans le tableau 6.2, valeurs correspondant aux Alpes)
for C in range(300, 4000, 100):
    i = i+1
    Nccn = C*s**k       #Calcul de NCCN
    Nccns.append(Nccn)  #On ajoute la valeur au tableau
    print("Pour C = ",str(C),"Nccn = ",str(Nccn))

#Affichage des NCCN
plt.figure()
plt.grid()
plt.plot(range(300,4000,100),Nccns)
plt.title("Nombre de particules à capacité CCN par cm^2")
plt.xlabel("C (cm-3)")
plt.ylabel("Nccn")