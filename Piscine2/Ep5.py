liste=["\b\t80cm\t60cm\n", "\b\t81cm\t51cm\n", "\b\t105cm\t145cm\n"]
list=[]
for i in liste:
    i=i[2:]
    i=i[:-1]
    liste=i.split("\t")
    for i in liste:
        i=int(i[:-2])
        list.append(i)
liste1 = list[0:2]
liste2 = list[2:-2]
liste3 = list[4:]

lst = [liste1,liste2,liste3]
print(lst)


def minmax(X):
    if X[0] < X[1]:
        print(X[0])
    else:
        print("no")


minmax(liste1)
minmax(liste2)
minmax(liste3)
