degre = int(input("A quel degré est votre polynome ? : "))
a = []

if degre <= 2 :
    print("Entrer une valeur supérieure à 2 ")
else:
    for i in range(0, degre + 1):
        n = input("Entrer a" + str(i) + " : ")
        a.append(n)

    if degre == 3:
        X = 1
        for i in range(0, 11):
            div1 = (-(int(a[1])) * (X) - int(a[0]))
            div2 = (int(a[3]) * (X) + int(a[2]))
            X = (div1 / div2)**(1/2)
        print(X)
    else:
        X = 1
        div2 = 0
        for k in range(0, 11):
            div1 = (-(int(a[2]))*(X)**2 -(int(a[1]))*(X)**1 -(int(a[0])))
            while degre > 3:
                P = (int(a[degre])*(X)**(degre-3))
                div2 = div2 + P
                degre = degre-1
            X = (div1/div2)**(1/3)
    print(X)
