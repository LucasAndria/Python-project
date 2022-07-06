i = int(input("i = "))
x = []
y = []

if i <= 0:
    print("Impossible ! i appartient à [0, 3]")
elif i>3:
    print("Travail en cours ! i appartient à [0, 3]")
else:
    # recupération des valeur de x
    print('******************** Valeur de x ***************************')
    for j in range(0, i+1):
        nx = int(input("x" + str(j) + "= "))
        x.append(nx)
    print('******************** Valeur de y ***************************')
    # recupération des valeur de f(x)
    for j in range(0, i+1):
        ny = int(input("f(" + str(x[j]) + ")= "))
        y.append(ny)

    # linéare
    a = (y[0] - y[1]) / (x[0] - x[1])
    b = y[0] - a*(x[0])
    print("")
    if b < 0:
        print("linéaire :")
        print("P(x) = ", a, "x ", b)
    else:
        print("linéaire :")
        print("P(x) = ", a, "x +", b)

    if i >= 2:
        deg = [0, 1, 2]
        #Interpolation parabolique
        deg[2] = (y[0]/(x[0]*(x[0]-x[2]-x[1])+(x[1]*x[2]))) + (y[1]/(x[1]*(x[1]-x[2]-x[0])+(x[0]*x[2]))) + (y[2]/(x[2]*(x[2]-x[1]-x[0])+(x[0]*x[1])))
        deg[1] = (((-x[2]*y[0])-(x[1]*y[0]))/((x[0]-x[1])*(x[0]-x[2])))+(((-x[2]*y[1])-(x[0]*y[1]))/((x[1]-x[0])*(x[1]-x[2])))+(((-x[1]*y[2])-(x[0]*y[2]))/((x[2]-x[0])*(x[2]-x[1])))
        deg[0] = ((y[0]*x[1]*x[2])/(x[0]*(x[0]-x[2]-x[1])+(x[1]*x[2])))+((y[1]*x[0]*x[2])/(x[1]*(x[1]-x[2]-x[0])+(x[0]*x[2])))+((y[2]*x[0]*x[1])/(x[2]*(x[2]-x[1]-x[0])+(x[0]*x[1])))
        print("")
        print("Parabole")
        print('P(x) = ('+str(deg[2])+')x^2 + ('+str(deg[1])+')x + ('+str(deg[0])+')')

    if i > 2:
        deg = [0, 1, 2, 3]
        #Interpolation de lagrange
        den0 = ((x[0]-x[1])*(x[0]-x[2])*(x[0]-x[3]))
        den1 = ((x[1]-x[0])*(x[1]-x[2])*(x[1]-x[3]))
        den2 = ((x[2]-x[0])*(x[2]-x[1])*(x[2]-x[3]))
        den3 = ((x[3]-x[0])*(x[3]-x[1])*(x[3]-x[2]))

        deg[3] = ((y[0]/den0)+(y[1]/den1)+(y[2]/den2)+(y[3]/den3))
        deg[2] = ((-(y[0]*(x[1]+x[2]+x[3]))/den0)-((y[1]*(x[2]+x[0]+x[3]))/den1)-((y[2]*(x[0]+x[1]+x[3]))/den2)-((y[3]*(x[0]+x[1]+x[2]))/den3))

        p1 = ((y[0]*(x[1]*x[2]+x[2]*x[3]+x[1]*x[3]))/den0)
        p2 = ((y[1]*(x[0]*x[2]+x[2]*x[3]+x[0]*x[3]))/den1)
        p3 = ((y[2]*(x[0]*x[1]+x[0]*x[3]+x[1]*x[3]))/den2)
        p4 = ((y[3]*(x[0]*x[1]+x[0]*x[2]+x[1]*x[2]))/den3)
        deg[1] = p1+p2+p3+p4

        deg[0] = (-(y[0]*(x[1]*x[2]*x[3]))/den0-(y[1]*(x[0]*x[2]*x[3]))/den1-(y[2]*(x[0]*x[1]*x[3]))/den2-(y[3]*(x[0]*x[1]*x[2]))/den3)
        print("")
        print("lagrange degré 3")
        print('P(x) = ('+str(deg[3])+')x^3 + ('+str(deg[2])+')x^2 + ('+str(deg[1])+')x + ('+str(deg[0])+')')

    #calcul
    min = x[0]
    int(min)
    max = x[i]
    int(max)
    for k in range(0, i+1):
        int(x[k])
        if min > x[k]:
            min = x[k]
        if max < x[k]:
            max = x[k]

    Q = 'n'
    while (Q != 'o') :
        print("")
        ix = float(input("entrer une valeur de x dans l'intervalle {"+str(min)+", "+str(max)+"} = "))
        if ix >= min and ix <= max:
            if i == 1:
                rep = ((a)*(ix))+b
                print('f('+str(ix)+') = '+str(rep))
            elif i == 2:
                rep = ((deg[2])*(ix)**(2))+((deg[1])*(ix))+(deg[0])
                print('f('+str(ix)+') = '+str(rep))
            elif i == 3:
                rep = ((deg[3])*(ix)**(3))+((deg[2])*(ix)**(2))+((deg[1])*(ix))+(deg[0])
                print('f(' + str(ix) + ') = ' + str(rep))
            else:
                print('travail en cours')
        else:
            print('la valeur entrer doit être entre '+str(min)+' et '+str(max))
        Q = input("Appuiez sur 'o' pour quitter ou sur 'entrer' pour recommencer : ")
