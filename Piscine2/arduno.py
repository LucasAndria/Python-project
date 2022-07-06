import arduino as arduino
from tkinter import*

import serial

#ouverture de la liaison serie
a = serial.Serial('/dev/ttyUSB0', 9600)
print(a)


while True:
    print("La distance en cm : ")
    bytesToRead = a.inWaiting()
    data = a.readline()
    data = data.decode().strip()
    print(str(data))

def condition():
    texte = Message.get()

    if texte == "Parking Complet":
        Message.set("Parking vide")
        #photo= PhotoImage(file="image1.png")
        label.configure(image=photo2)
        label.update()
    else:
        Message.set("Parking Complet")
        #photo = PhotoImage(file="image2.png")
        label.configure(image=photo)
        label.update()

fenetre=Tk()

fenetre.geometry("600x700")
photo = PhotoImage(file="image1.png")
photo2=PhotoImage(file="image2.png")
label = Label(fenetre, image=photo, width=500, height=300)
label.pack()

bouton=Button(fenetre, text="Initialiser", command=condition)
bouton.pack()

Message=StringVar()
Message.set("Parking Complet")
label1=Label(fenetre, textvariable=Message)
label1.pack()

fenetre.mainloop()
