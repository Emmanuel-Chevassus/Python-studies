# -*- coding: cp1252 -*-
import numpy as np
# ============= Read =============
tablo = np.empty([10,3])
comma_filename = "commas.txt"
# 2. Read and put in matrix
# The dimension of the matrix is the first line
comma_values = []
with open(comma_filename, 'r') as f:
    first_line = f.readline()  # lire uniquement la premiere ligne
#    print first_line
    nx, ny = first_line.split(',')  # split  a l'aide de la virgule
    # .split()  donne un tableau
    
    for j in range(int(nx)):
#        print "line: " , j
        line = f.readline()
#        print line
        row_values = []  # une ligne de la matrice
        for val in line.split(','):
#            print val, float(val)
            row_values.append(float(val))
        comma_values.append(row_values)       # Add the row to matrix            
# stocker les valeurs dans une matrice (10x3) = tablo[10,3]
        nnx=len(row_values)
        for i in range(nnx):
            tablo[i,j] = row_values[i]
            print i,j,tablo[i,j]
#
# ecriture de la matrice 10x3 sir l'écran et dan le  fichier 'testout.dat'
with open("testout.dat", "w") as flw:
    for j in range(3):
        pr_data = []
        for i in range(10):
            prval='{0:10.2f}'.format(float(tablo[i,j]))
            pr_data.append(float(prval))
            # ce write ecrit les 10 valeurs d'une ligne bien formattees dans le fichier flw
            flw.write('{0:9.2f}'.format(float(tablo[i,j])))
        # ce 'print ecran' affiche les 10 valeurs d'une ligne            
        print ("%12s" % (pr_data[0:10]) )
        flw.write ('\n')  # important pour forcer la fin de la ligne      
#        
print ("ready and done")
