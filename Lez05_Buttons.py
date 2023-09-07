# 05 bottoni
# crearlo, personalizza, aggiungere comandi callback e lambda
# stato disabilitato, bottone immagine, immagine e testo

from tkinter import *
from tkinter import ttk
def saluta():
    print('ho cliccato il bottone')
root = Tk()
root.title('il nostro programma')
root.geometry('600x400')
# quit() da non usare perchè provoca un blocco del programma.
# usando lambda: root.destroy()
# si puo' usare ttk.Button
photo = PhotoImage(file='./recycling.png')
button = Button(root, text='ciao', command= saluta, image=photo, compound="left")
#button.state(['disabled']) per disattivare bottone
button["state"]="normal" # normal, disabled, enabled
button.pack(ipadx=50, ipady=50)

root.mainloop()