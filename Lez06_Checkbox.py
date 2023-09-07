# 06 checkbox (checkbuttons)
# creare callback, prendere valore checkbox, cambiare valori predefiniti

from tkinter import *
from tkinter import ttk
def premo_check():
    label = Label(text=nome.get())
    label.pack()
root = Tk()
root.title('Il nostro programma')
root.geometry("600x400")
# StringVar, IntVar(), BoolVar()
# non 0 perchè i valori cambiano periodicamente
# possiamo impostare i valori predefiniti 0 e 1 con 'Andrei' 'Rosca'
nome = StringVar()
check = Checkbutton(text="Ciao", font=("Helvetica", 24), command=premo_check, \
                    variable=nome, onvalue='Andrei', offvalue='Rosca')
# uncheck all'inizio come default
# per check all'inizio si usa il metodo .select()
check.deselect()
check.pack()
root.mainloop()