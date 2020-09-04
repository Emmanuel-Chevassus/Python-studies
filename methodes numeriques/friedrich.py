    

def friedrich(dt,dx,a,k,u):
    

    i=0
    nbx=len (x)
    uligne=u(k - 1,range())
    for x in range(- 5,5):
        i=i + 1
        if i != 1 and i != nbx:
            uligne[i]=dt*a*(u(k-1,i-1)-u(k-1,i+1))/(2*dx)+(u(k-1,i+1)+u(k-1,i-1))/2
    
    u.append(uligne)  
    return u
    
if __name__ == '__main__':
    pass
    