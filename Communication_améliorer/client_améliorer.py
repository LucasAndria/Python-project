def bin(string):
    msg = string
    msg = msg.lower()
    msg_a_envoyer = b""
    for i in range(0, len(msg)):
        if msg[i] == ' ':
            msg_a_envoyer += b" "
        if msg[i] == 'a':
            msg_a_envoyer += b"a"
        if msg[i] == 'b':
            msg_a_envoyer += b"b"
        if msg[i] == 'c':
            msg_a_envoyer += b"c"
        if msg[i] == 'd':
            msg_a_envoyer += b"d"
        if msg[i] == 'e':
            msg_a_envoyer += b"e"
        if msg[i] == 'f':
            msg_a_envoyer += b"f"
        if msg[i] == 'g':
            msg_a_envoyer += b"g"
        if msg[i] == 'h':
            msg_a_envoyer += b"h"
        if msg[i] == 'i':
            msg_a_envoyer += b"i"
        if msg[i] == 'j':
            msg_a_envoyer += b"j"
        if msg[i] == 'k':
            msg_a_envoyer += b"k"
        if msg[i] == 'l':
            msg_a_envoyer += b"l"
        if msg[i] == 'm':
            msg_a_envoyer += b"m"
        if msg[i] == 'n':
            msg_a_envoyer += b"n"
        if msg[i] == 'o':
            msg_a_envoyer += b"o"
        if msg[i] == 'p':
            msg_a_envoyer += b"p"
        if msg[i] == 'q':
            msg_a_envoyer += b"q"
        if msg[i] == 'r':
            msg_a_envoyer += b"r"
        if msg[i] == 's':
            msg_a_envoyer += b"s"
        if msg[i] == 't':
            msg_a_envoyer += b"t"
        if msg[i] == 'u':
            msg_a_envoyer += b"u"
        if msg[i] == 'v':
            msg_a_envoyer += b"v"
        if msg[i] == 'w':
            msg_a_envoyer += b"w"
        if msg[i] == 'x':
            msg_a_envoyer += b"x"
        if msg[i] == 'y':
            msg_a_envoyer += b"y"
        if msg[i] == 'z':
            msg_a_envoyer += b"z"
    return msg_a_envoyer

try:
    import socket
    hote = "localhost"
    port = 12800
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((hote, port))
    print("Connexion établie avec le serveur sur le port {}".format(port))

    msg = b""
    while msg != b"bye":
        msg = input("Votre message : ")
        connexion_avec_serveur.send(bin(msg))
        msg_recu = connexion_avec_serveur.recv(1024)
        print(msg_recu.decode())
    print("Fermeture de la connexion")
    connexion_avec_serveur.close()
except:
    print("svp, lancer votre serveur! ")
