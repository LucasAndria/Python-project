from random import randint

reponse = True
nom = input("entrer votre nom : ")
nb_sys = randint(0, 250)
score = 10
for i in range(0, 10):
    nb = int(input("Entrer un nombre : "))
    if nb == nb_sys:
        print("Vous avez gagné !")
        print(nom, ' a eu ', score, 'points')
        break
    elif nb < nb_sys:
        print("Ajouter un peu")
    else:
        print("Diminuer un peu")
    score = score - 1
if score == 0 :
    print("vous avez perdu", nom)