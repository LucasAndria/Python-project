
a = str(input("saisir le nom du fichier : "))
a = a + ".txt"
c = open(a).read()
n = len(c)
print(n)
liste = []
T = []
def clean(X):
        i = X[4:]
        i = i[:-2]
        i.split("\\t")
        print(i)
        T.append(i)

if n == 0:
    print("ce fichier est vide")
else:
    print(c)
    clean(c)
    print(T)