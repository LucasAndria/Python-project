#import serial
from threading import *
from tkinter import *

class Monlecteur(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        a = serial.Serial('COM5', 9600)
        print(a)
        while True:
            print("La couleur detecter est le: ")
            bytesToRead = a.inWaiting()
            data = a.readline()
            data = data.decode().strip()
            print(str(data))
            data = data[0:13]
            print(str(data))
            R = data[3:6]
            G = data[-3:]
            R = int(R)
            G = int(G)
            color = "Non reconnue"
            if R < 80 and  R > 20 and G > 80:
                        color = "Rouge"
            elif R > 50 and G > 60 and G < 100:
                        color = "Vert"
            else:
                color = "Non reconnue"
            print(color)

            btt.place_forget()
            label.pack()
            label1.place_forget()
            Nom.pack()

            if color == "Vert":
                # t.set("Rouge")
                label.configure(image=photo3)
                label.update()
                label2.place_forget()

            elif color == "Rouge":
                # t.set("Vert")
                label.configure(image=photo2)
                label2.place_forget()
                label.update()

            else:
                label.configure(image=photo4)
                label.update()
                label2.place(x=325, y=350)








def x():
 texte = t.get()
 btt.place_forget()
 label.pack()
 label1.place_forget()
 Nom.pack()

 if texte == "Vert":
     #t.set("Rouge")
     label.configure(image=photo3)
     label.update()
     label2.place_forget()

 elif texte == "Rouge":
     #t.set("Vert")
     label.configure(image=photo2)
     label2.place_forget()
     label.update()

 else:
     label.configure(image=photo4)
     label.update()
     label2.place(x=325, y=350)
 fenetre.after(1000, x)
def clean(X):
 newX = []
 for i in range(len(X)):
     temp=X[i][2:]
     newX.append(temp[:5])
 return newX

fenetre = Tk()
fenetre.configure(bg="grey")
fenetre.geometry("800x650+300+10")

photo = PhotoImage(file="PR.png")
photo2 = PhotoImage(file="SDL.png")
photo3 = PhotoImage(file="TE.png")
photo4 = PhotoImage(file="louvre.png")

label = Label(fenetre, image=photo4, width=700, height=600)
label1 = Label(fenetre, image=photo4, width=170, height=50)
label2 = Label(fenetre, text="Aucune couleur detectee")

btt = Button(fenetre, text="Commencer la visite", command=x)
btt.place(x="350", y="350")
label1.place(x='0', y='0')
t = StringVar()
t.set("")
lecteurArduino=Monlecteur()
lecteurArduino.start()
Nom = Entry(fenetre, textvariable=t)

fenetre.mainloop()