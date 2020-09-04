# ============= Read =============

spaces_filename = 'spaces.txt'  

space_values = []  # array
with open(spaces_filename, 'r') as lire_f:
    for line in lire_f:
        # ici: line presente la lecture d'une ligne entiere 
        line = line.split()  # ()sans parametre: recherche des espaces dans la ligne
        nx = len(line)
        print line, nx
        if line:  # i.e. line est non vide
            for valeur in line:
                print 'valeur= ',valeur
                # valeur sont les donnee entre les espaces  
                floating_val = float(valeur)
                space_values.append(floating_val)
                
print "tableau entier de space_values: "
print "nombre d'elements ",len(space_values)
print(space_values),len(space_values)
nval=len(space_values)
for i in range(nval):
    print i, space_values[i]
print # Empty line on console

