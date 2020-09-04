import numpy as np

def wendroff(dt,dx,a,k,u):
    

    uligne=u(k - 1,range())

    #calcul du vecteur au centre d'une maille pour le temps 
    i=0

    for x in range(-5,5):
        i=i + 1

#La 1ere valeur de i correspond à la condition limite, on ne la prend pas car on sort du schéma si i=1
        utdemi=np.empty([i])
        if i != 1:
            utdemi[i]=dt/dx*a*((u(k-1,i-1)-u(k-1,i))/2)+u(k-1,i)

    
    
    i=0
    for x in np.arange(- 5,5,dx).reshape(-1):
        i=i + 1
        if i != 1:
            uligne[i] = dt/dx*a*((utdemi(i-1)-utdemi(i))/2)+utdemi(i)
    
    u=np.append([[u],[uligne]])

    return u
    
if __name__ == '__main__':
    pass
    