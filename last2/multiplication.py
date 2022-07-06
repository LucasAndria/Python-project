
a = ""
while not a == "oui":
    b = input("inserez un chiffre : ")
    if b.isdigit():
        b = int(b)
        for i in range(11):

            print(str(b), "*", str(i), "=", str(b*i))
        a = str(input("voudriez vous quitter? : "))
    else:
        print("svp,")
