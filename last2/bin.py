Quit = ""

while Quit != "q" and Quit == "":

        nb_a_convertir = int(input("entrez un nombre = "))
        res_bin = []
        while nb_a_convertir > 0:
                res_bin = res_bin+[nb_a_convertir % 2]
                nb_a_convertir //= 2
        res_bin.reverse()
        for i in res_bin:
            print(i)
        Quit = str(input("appuiez sur q pour quitter et sur entrer pour continuer : "))
