# 10 combobox (menu a tendina)
# creare, inserire valori, esempio con mesi, readonly state, associare evento

from tkinter import *
from tkinter import ttk
from calendar import month_name
root = Tk()
root.title('Il nostro programma')
root.geometry('600x400')

mese_selezionato = StringVar()
mesi_combobox = ttk.Combobox(root, textvariable=mese_selezionato)

mesi_combobox['values']=[month_name[m] for m in range(1,13)]
mesi_combobox['state'] = 'readonly'
mesi_combobox.pack(fill=X, padx=5, pady=5)

def seleziona_mese(event):
    print(mese_selezionato.get())

mesi_combobox.bind('<<ComboboxSelected>>', seleziona_mese)
root.mainloop()