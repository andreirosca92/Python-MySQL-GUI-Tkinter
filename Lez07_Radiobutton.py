# 07 radiobutton
# crearla, associare valore e variabile, generarle dinamicamente, mini esempio pratico

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Il nostro programma')
root.geometry('600x400')
"""
genere = StringVar()
r1 = ttk.Radiobutton(root, text="maschio", value="m", variable=genere).pack()
r2 = ttk.Radiobutton(root, text="femmina", value="f", variable=genere).pack()
button = Button(root, text="prova", command= lambda: print(genere.get())).pack()
"""
taglia_selezionata = StringVar()

taglie = (
    ('Small', 'S'),
    ('Medium','M'),
    ('Large', 'L'),
    ('Extra Large', 'XL')
)
for taglia in taglie:
    r = ttk.Radiobutton(root, text=taglia[0], value=taglia[1], variable=taglia_selezionata)
    r.pack(padx=5, pady=5)
button = Button(root, text="Prova", command = lambda: print(taglia_selezionata.get())).pack()
root.mainloop()