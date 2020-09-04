# ============= Read  OCEAN parameters ===========
eos80_data = 'A_a_L.txt'

A = []  # array
B = []  # array
C = []  # array
D = []  # array
E = []  # array
F = []  # array
G = []  # array
H = []  # array
I = []  # array
J = []  # array
K = []  # array
L = []  # array

with open(eos80_data, 'r') as rdfl:
# lire la ligne avec les valeurs pour A    
    line1 = rdfl.readline()
# lire la ligne avec les valeurs pour B
    line2 = rdfl.readline()
    line3 = rdfl.readline()
    line4 = rdfl.readline()
    line5 = rdfl.readline()
    line6 = rdfl.readline()
    line7 = rdfl.readline()
    line8 = rdfl.readline()
    line9 = rdfl.readline()
    line10 = rdfl.readline()
    line11 = rdfl.readline()
    line12 = rdfl.readline()                    
# allocate line1 to A[ ]    
    ncpt=0
    for val in line1.split(','):
        # valeur sont les donnees entre les espaces  
        A.append(float(val))
        ncpt=ncpt+1
#    for k in range(ncpt):
#        print k, A[k]
    print ncpt, A
# allocate line2 to B[ ]    
    ncpt=0
    for val in line2.split(','):
        # valeur sont les donnees entre les espaces  
        B.append(float(val))
        ncpt=ncpt+1
#    for k in range(ncpt):
#           print k, B[k]
    print ncpt, B
# allocate line3 to C[ ]    
    ncpt=0
    for val in line3.split(','):
        # valeur sont les donnees entre les espaces  
        C.append(float(val))
        ncpt=ncpt+1
#    for k in range(ncpt):
#           print k, C[k]
    print ncpt, C
# allocate line4 to D[ ]    
    ncpt=0
    for val in line4.split(','):
        # valeur sont les donnees entre les espaces  
        D.append(float(val))
        ncpt=ncpt+1
#    for k in range(ncpt):
#           print k, D[k]
    print ncpt," D=", D
# allocate line5 to E[ ]    
    ncpt=0
    for val in line5.split(','):
        # valeur sont les donnees entre les espaces  
        E.append(float(val))
        ncpt=ncpt+1
#    for k in range(ncpt):
#           print k, E[k]
    print ncpt, E
# allocate line6 to F[ ]    
    ncpt=0
    for val in line6.split(','):
        # valeur sont les donnees entre les espaces  
        F.append(float(val))
        ncpt=ncpt+1
#    for k in range(ncpt):
#           print k, F[k]
    print ncpt, F
# allocate line7 to G[ ]    
    ncpt=0
    for val in line7.split(','):
        # valeur sont les donnees entre les espaces  
        G.append(float(val))
        ncpt=ncpt+1
#    for k in range(ncpt):
#           print k, G[k]
    print ncpt, G
# allocate line8 to H[ ]    
    ncpt=0
    for val in line8.split(','):
        # valeur sont les donnees entre les espaces  
        H.append(float(val))
        ncpt=ncpt+1
    print ncpt, H
# allocate line8 to I[ ]    
    ncpt=0
    for val in line9.split(','):
        # valeur sont les donnees entre les espaces  
        I.append(float(val))
        ncpt=ncpt+1
    print ncpt, I
# allocate line10 to J[ ]    
    ncpt=0
    for val in line10.split(','):
        # valeur sont les donnees entre les espaces  
        J.append(float(val))
        ncpt=ncpt+1
    print ncpt, J
# allocate line11 to K[ ]    
    ncpt=0
    for val in line11.split(','):
        # valeur sont les donnees entre les espaces  
        K.append(float(val))
        ncpt=ncpt+1
    print ncpt, K
# allocate line12 to L[ ]    
    ncpt=0
    for val in line12.split(','):
        # valeur sont les donnees entre les espaces  
        L.append(float(val))
        ncpt=ncpt+1
    print ncpt, L


# INPUT T,S,P 	    # T en deg C, S en ups, P en dbar

P = 10.             # P reste 1 bar - 10dbar
P = P / 10.         # La pression est convertie en bar

Tstrt = -5.5
nT = 81 

Sstrt = 28.5
nS = 17
with open("rho_out.dat", "w") as wrfl:
    for k in range (nT):
        T  = Tstrt + 0.5 * (k+1)
        for ks in range (nS):
            S = Sstrt  + 0.5 * (ks+1)
    
            SR = (S)**(0.5)     # ?????

            Aval = A[0]+(A[1]+(A[2]+(A[3]+(A[4]+A[5]*T)*T)*T)*T)*T
            Bval = B[0]+(B[1]+(B[2]+(B[3]+B[4]*T)*T)*T)*T
            Cval = C[0]+(C[1]+C[2]*T)*T
            Dval = Aval + (Bval + Cval *SR + D[0]*S) *S

            Eval = E[0]+(E[1]+(E[2]+(E[3]+E[4]*T)*T)*T)*T
            Fval = (F[0]+(F[1]+(F[2]+F[3]*T)*T)*T)*S
            Gval=  Eval + Fval + (G[0]+(G[1]+G[2]*T)*T)*SR*S

            Hval = H[0] + (H[1]+(H[2]+H[3]*T) *T) *T
            Ival = I[0] + (I[1]+I[2]*T) *T
            Jval = Hval +( Ival +J[0]*SR) *S
            Kval = K[0] + (K[1]+K[2]*T) *T
            Lval = Kval + (L[0]+ (L[1]+L[2]*T) *T) * S 

            Mval =Gval + (Jval+Lval*P) *P

            RHO = Dval/(1.-P/Mval) # Masse volumique en kg/m3

#   print RHO

#       wrfl.write (" T       S       RHO     \n" )
            pr_T = '{0:9.2f}'.format(float(T))
            pr_S = '{0:9.2f}'.format(float(S))
            pr_RHO = '{0:10.3f}'.format(float(RHO-1000.))
            wrfl.write(pr_T + pr_S + pr_RHO + "\n" )
            print (pr_T + pr_S + pr_RHO )

