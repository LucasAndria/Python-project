msg = input("Votre message : ")
msg = msg.lower()
msg_to_send = b""
for i in range(0, len(msg)):
    if msg[i] == 'a':
        msg_to_send += b"a"
    if msg[i] == 'b':
        msg_to_send += b"b"
    if msg[i] == 'c':
        msg_to_send += b"c"
    if msg[i] == 'd':
        msg_to_send += b"d"
    if msg[i] == 'e':
        msg_to_send += b"e"
    if msg[i] == 'f':
        msg_to_send += b"f"
    if msg[i] == 'g':
        msg_to_send += b"g"
    if msg[i] == 'h':
        msg_to_send += b"h"
    if msg[i] == 'i':
        msg_to_send += b"i"
    if msg[i] == 'j':
        msg_to_send += b"j"
    if msg[i] == 'k':
        msg_to_send += b"k"
    if msg[i] == 'l':
        msg_to_send += b"l"
    if msg[i] == 'm':
        msg_to_send += b"m"
    if msg[i] == 'n':
        msg_to_send += b"n"
    if msg[i] == 'o':
        msg_to_send += b"o"
    if msg[i] == 'p':
        msg_to_send += b"p"
    if msg[i] == 'q':
        msg_to_send += b"q"
    if msg[i] == 'r':
        msg_to_send += b"r"
    if msg[i] == 's':
        msg_to_send += b"s"
    if msg[i] == 't':
        msg_to_send += b"t"
    if msg[i] == 'u':
        msg_to_send += b"u"
    if msg[i] == 'v':
        msg_to_send += b"v"
    if msg[i] == 'w':
        msg_to_send += b"w"
    if msg[i] == 'x':
        msg_to_send += b"x"
    if msg[i] == 'y':
        msg_to_send += b"y"
    if msg[i] == 'z':
        msg_to_send += b"z"
print(msg_to_send)
