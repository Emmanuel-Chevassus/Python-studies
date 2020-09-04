import numpy as np
# ============= Read =============
comma_filename = "commas.txt"
# 2. Read and put in matrix
with open(comma_filename, 'r') as f:
    first_line = f.readline()  # lire uniquement la premiere ligne
    print first_line, type(first_line)
    nx, ny = first_line.split(',')  # split  a l'aide de la virgule
    print nx,ny,type(nx)
    nnx=int(nx)
    nny=int(ny)
    # .split()  donne un tableau
    comma_values = []        
    for i in range(nnx):
        print "line: " , i
        line = f.readline()
        #print line
        row_values = []  # stocker les valeurs indiviudelles 
        for val in line.split(','):
            row_values.append(float(val))
            comma_values.append(float(val))  # Add the row to matrix
#        print comma_values

#print len(comma_values)
#print comma_values

allval = np.empty([nnx,nny])
for i in range(nnx):
    for j in range(nny):
        j2 = j + nny*i
#        print comma_values[j2]
        allval[i,j] = comma_values[j2]
    print i, allval[i,0:10]

print # Empty line in console
