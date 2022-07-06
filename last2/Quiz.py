
quit = "n"
while quit != "o" and quit == "n":
    nom = str(input("votre nom : "))
    note = 0
    #Questions
    #1
    print("Quelle est le vrai nom de Nicki Minaj ?")
    print("1 - Nicki Minaj")
    print("2 - Onika Tanya Maraj")
    print("3 - Trinité Tobago")
    a = str(input("votre choix est le : "))
    if a == "2":
        print("Bien!")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note+1
    else:
        print("Faux")
        print("la bonne réponse est le 2")
        input("appuier sur entrer pour passé a la question suivante ")

    #2
    print("Qui est le frêre de Maitre gims ?")
    print("1 - Dadju")
    print("2 - Bruno mars")
    print("3 - Master just")
    a = str(input("votre choix est le : "))
    if a == "1":
        print("Wow, Bonne réponse")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note + 1
    else:
        print("Mauvaise réponse")
        print("la bonne réponse est le 1")
        input("appuier sur entrer pour passé a la question suivante ")

    #3
    print("Avec quelle titre Post malone s'est fait connaitre mondialement ?")
    print("1 - Better now")
    print("2 - White Iverson")
    print("3 - Congratulation")
    a = str(input("votre choix est le : "))
    if a == "2":
        print("Wow... la chance ")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note + 1
    else:
        print("pas très juste")
        print("la bonne réponse est le 2")
        input("appuier sur entrer pour passé a la question suivante ")

    #4
    print("Justin Timberlake a été en couple avec laquelle de ces chanteuses ?")
    print("1 - Rihana")
    print("2 - Alicia key")
    print("3 - Britney Spears")
    a = str(input("votre choix est le : "))
    if a == "3":
        print("Dans le mille, tres belle pioche!")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note + 1
    else:
        print("C'est faux biiiiip, il l'a juste biiiiip celle la!")
        print("la bonne réponse est le 3")
        input("appuier sur entrer pour passé a la question suivante ")

    #5
    print("A quelle age Michael jackson est décédé ?")
    print("1 - 60 ans")
    print("2 - 40 ans")
    print("3 - 50 ans")
    a = str(input("votre choix est le : "))
    if a == "3":
        print("incroyable")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note + 1
    else:
        print("Wow, je croyait que tout le monde réussirait à répondre cette question")
        print("la bonne réponse est le 3")
        input("appuier sur entrer pour passé a la question suivante ")

    # 6
    print("Quelle est la dernière chanson de Katy Perry ?")
    print("1 - The one that got away")
    print("2 - Part of me")
    print("3 - Teenage dream")
    a = str(input("votre choix est le : "))
    if a == "2":
        print("Bien jouer")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note + 1
    else:
        print("Diso ! ")
        print("la bonne réponse est le 2")
        input("appuier sur entrer pour passé a la question suivante ")

    # 7
    print("Avec quelle chanteuse David Guetta fait-il la chanson 'Turn me on'")
    print("1 - Nicki Minaj")
    print("2 - Kelly rowland")
    print("3 - Rihana")
    a = str(input("votre choix est le : "))
    if a == "1":
        print("Good !")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note + 1
    else:
        print("Tsy marina")
        print("la bonne réponse est le 1")
        input("appuier sur entrer pour passé a la question suivante ")

    # 8
    print("Quelle chanteur chante 'Ai su eu te pego' ?")
    print("1 - Michel telo")
    print("2 - M.pokora")
    print("3 - Christophe maé")
    a = str(input("votre choix est le : "))
    if a == "1":
        print("juste")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note + 1
    else:
        print("il faut écouter de la musique de temps en temps!")
        print("la bonne réponse est le 1")
        input("appuier sur entrer pour passé a la question suivante ")

    # 9
    print("Quelle chanteuse chante en duo avec Coldplay ?")
    print("1 - Brithney Spears")
    print("2 - Katy pery")
    print("3 - Rihanna")
    a = str(input("votre choix est le : "))
    if a == "3":
        print("bien")
        input("appuier sur entrer pour passé a la question suivante ")
        note = note + 1
    else:
        print("non")
        print("la bonne réponse est le 3")
        input("appuier sur entrer pour passé a la question suivante ")

    # 10
    print("Quelle est le vrai nom de Marshmello")
    print("1 - Sonny John Moore")
    print("2 - Shawn Peter Raul Mendes")
    print("3 - Christopher Comstock")
    a = str(input("votre choix est le : "))
    if a == "3":
        print("Excelent !")
        input("C'est terminer appuiez sur entrer pour voir votre score ")
        note = note + 1
    else:
        print("Faux")
        print("la bonne réponse est le 3")
        input("C'est terminer appuiez sur entrer pour voir votre score ")

    #END
    if note <= 4:
        print("Tu peut faire mieu ", nom, ", ton score est ", note, "/10")
    elif note == 5:
        print("C'est insufisant ", nom, "ton score est ", note, "/10")
    else:
        print("bien jouer ", nom, " votre score est ", note, "/10")
    quit = str(input("voulez vouz quitter ? o/n : "))
