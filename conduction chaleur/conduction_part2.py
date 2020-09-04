import numpy as np

def conduction2(a,delta_t) :
    # calcule l'évolution de la température au sein d'une barre en 1D à l'aide de l'équation de la conduction thermique via l'algo T(i,k+1)=a*deltat*(T(i+1,k)-2T(i,k)+T(i-1,k))/(deltax^2)+T(i,k)
    # input :
    #   a : diffusivité thermique en m2/s du matériau constituant la barre
    #   delta_t : pas d'intégration en secondes 
    # output :
    #   teq : temps mis pour atteindre l'équilibre
    #   T : température de la barre au cours du temps (différentes lignes = différents temps, différentes colonnes = différentes abscisses de la barre)
    #   temps : durées depuis l'instant initial jusqu'à l'équilibre
    L=1. #longueur de la barre en mètres
    nb_tranches=100
    T=np.zeros(shape=(1,nb_tranches+1))+20. #température initiale de la barre
    compteur=0 #compte le pas de temps jusqu'à l'équilibre
    nb=200000 # nombre maximal de pas de temps calculé si jamais l'équilibre n'est pas atteint (schéma instable)
    tfin=60 #temps de chauffe final en secondes
    temps=np.array([0.]) # temps écoulé en secondes
    eps=10**-6 # seuil d'équilibre
    test=10*eps 
    delta_x=L/nb_tranches #pas de discrétisation horizontal en mètres
    T0=20.
    while ((test>eps) and (compteur<nb)) : # compteur < nb :  si jamais l'équilibre n'est pas atteint, on arrête au bout de nb pas de temps 
        compteur=compteur+1
        print(compteur)
        temps=np.append(temps, temps[compteur-1]+delta_t) 
        inter=np.zeros(shape=(1,nb_tranches+1))+T0
        # détermination de la température de la face gauche :
        if temps[compteur] <= tfin :
            inter[0,0]=T0+0.1*temps[compteur]
        else :
            inter[0,0]=T0+0.1*tfin
        # détermination de la températue le long de la barre à chaque pas de temps :    
        for i in range(1,nb_tranches) :
            inter[0,i]=a*delta_t*(T[compteur-1,i+1]+T[compteur-1,i-1]-2*T[compteur-1,i])/(delta_x**2)+T[compteur-1,i]
        T=np.append(T,inter,axis=0)
        test=np.max(np.abs(T[compteur,:]-T[compteur-1,:]),axis=0)    
    teq=temps[compteur-1] #temps mis pour converger vers la solution
    return teq,temps,T   