E=0
A=0
X=str(input("saisir ici : "))
n=len(X)
if X[0:2]=='EA':
    Y=int(X[3:n])
    Y=Y*4000
    print(Y,"Ar")
else:
    Y=int(X[3:n])
    Y=Y/4000
    print(Y,"Euro")
