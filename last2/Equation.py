
oquit = ()
while oquit != "q":
    a = int(input("a : "))
    b = int(input("b : "))
    c = int(input("c : "))

    deg = (str(a) + "x²" + "+" + str(b) + "x" + "+" + str(c))
    print(deg)

    a = int(a)
    b = int(b)
    c = int(c)

    #DELTA
    delta = (b*b)-(4*a*c)
    if delta > 0:
        #deux racine distincte
        for i in range(1, delta):
            k = b
            k = delta / i
            if k % i == 0 and k != delta:

                x1 = (int(-b) - int(k))/ 2*a
                x2 = (int(-b) + int(k))/ 2*a
                print("deux racine distincte ")
                print("la solution est (", str(x1), ",", str(x2), ")")

    elif delta == 0:
        #une racine double
        x = ((-b)/(2*a))
        print("une racine double"
              "la solution est x = ", str(x))

    elif delta < 0:
        #pas de solution
        print("pas de solution")
    oquit = str(input("appuiez sur 'q' pour quitter et 'entrez' pour recommencer : "))