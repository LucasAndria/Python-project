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


import socket
hote = ''
port = 12800
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("le serveur écoute à présent sur le port {}".format(port))
connexion_avec_client, info_connexion = connexion_principale.accept()
msg_recu = b""
while msg_recu != b"bye":
    msg_recu = connexion_avec_client.recv(1024)
    # L'instruction ci-dessous peut lever une exception si le message
    # réceptionné comporte des accents
    print(msg_recu.decode())
    msg = input("Votre réponse : ")
    connexion_avec_client.send(bin(msg))
print("Fermeture de connexion")
connexion_avec_client.close()
connexion_principale.close()
