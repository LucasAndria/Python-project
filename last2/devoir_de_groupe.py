a = int(input("le nombre de virus initial : "))
print("les virus se multiplient toutes les 24h !")
b = int(input("la durée jusqu'au nouvelle examen du corps de l'hôte : "))
k = str(input("tapez 1 si la durée est en minutes, 2 si elle est en heurres et 3 si elle est en jours : "))
if k == "1":
    for i in range(0, b):
        if i % 1440 == 0:
            a = a * 2
    print("le corps de l'hôte contient ", a, "cellule vivante apres ", b, "minutes de mitose")

elif k == "2":
    for i in range(0, b):
        if i % 24 == 0:
            a = a * 2
    print("le corps de l'hôte contient ", a, "cellule vivante apres ", b, "heurres de mitose")

elif k == "3":
    for i in range(0, b):
        a = a*2
    print("le corps de l'hôte contient ", a, "cellule vivante apres ", b, "jours de mitose")
else:
    print("ERREUR")
