# 13 treeview
# tabular data
# hierarchical data

from tkinter import *
from tkinter import ttk


root=Tk()
root.title('Il nostro programma')
root.geometry('800x600')

colonne = ('nome', 'cognome', 'email')
tabella = ttk.Treeview(root, columns=colonne, show='headings')

tabella.heading('nome', text='Nome')

tabella.heading('cognome', text='Cognome')

tabella.heading('email', text='Email')

righe = []
for n in range(1,50):
    righe.append((f'nome {n}', f'cognome {n}', f'email {n}'))
for riga in righe:
    tabella.insert('', END, values=riga)

tabella.grid(row=0,column=0, sticky='nsew')

scrollbar = ttk.Scrollbar(root, orient=VERTICAL, command=tabella.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

tabella.configure(yscrollcommand=scrollbar.set)
root.mainloop()
