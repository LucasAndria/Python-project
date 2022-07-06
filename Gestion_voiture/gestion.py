class Voiture:
    nb_objet = 0

    def __init__(self, im, mark):
        self.immatriculation = im
        self.type = "4*4"
        self.mark = mark
        Voiture.nb_objet += 1

    def _get_immatriculation(self):
        return self.immatriculation

    def _set_immatriculation(self, im):
        self.immatriculation = im

    def _get_type(self):
        return self.type

    def _set_type(self, type):
        self.type = type

    def _get_mark(self):
        return self.mark

    def _set_mark(self, mark):
        self.mark = mark

    def logvoiture(self, action, typeS, markS, im):
        with open('log.txt', 'a') as fichier:
            fichier.write("l'utilisatieur 1 a fait l'action ["+action+"] et a modifier les variables comme les suivants : marks ["+markS+"]: im : ["+im+"],"
                          "types : ["+typeS+"] \n")
    def showLog(self):
        with open('log.txt', 'r') as fichier:
            data = fichier.readlines()
            print("le fichier log contient : ", data)


v1 = Voiture('2567TA', 'Peugeot')
print("vous avez creer ", Voiture.nb_objet, " objets")
print("l'immatriculation de cette voiture est ", v1.immatriculation)
v2 = Voiture("2765TB", "Renault")

action = input("appuiez sur 'M' pour modifier ou 'R' pour seulement lire :")
if action == 'M' :
    mark = input('mark = ')
    type = input('type = ')
    im = input('im = ')
    v2.logvoiture(action, type, mark, im)
elif action == 'R':
    v2.showLog()
