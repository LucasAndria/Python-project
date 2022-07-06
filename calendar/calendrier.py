from tkinter import *
import calendar

root = Tk()
root.title("Calendrier")
root.geometry("700x700")
root.resizable(0, 0)


#definir une fonction pour l'affichage du calendrier
def show():
    b = int(spin.get())

    cal2 = calendar.calendar(b)

    txt.delete(0.0, END)
    txt.insert(INSERT, cal2)


#creer label
lbl = Label(root, text="Choisir année : ", font=('arial', 9, 'bold')).place(x=250, y=0)

#creer spinbox
spin = Spinbox(root, from_=1999, to=2100, width=4)
spin.place(x=350, y=0)

#creer button
btn = Button(root, text="Année", font=('arial', 9, 'bold'), command=show).place(x=290, y=30)

txt = Text(root, width=80, height=38)
txt.place(x=20, y=57)

root.mainloop()
