print("f(x)=(x**7)-1")
print("a et b sont des intervalle de f(x)")
a = int(input("a="))
b = int(input("b="))


def f(x):
    return x**7-1


for x in range(a, b):
    if f(x) == 0:
        print("TVI = oui")
        print("racine =", x)
        break
    else:
        print("TVI = non")
