# 14 menubar
# creare semplice menu, aggiungere separatore, sottomenu

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Il nostro programma')
root.geometry('800x600')

menubar = Menu(root)
root.config(menu=menubar)

file_menu= Menu(menubar, tearoff=0)
file_menu.add_command(label='New', command=root.destroy)
file_menu.add_command(label='Open', command=root.destroy)

file_altro_submenu = Menu(file_menu, tearoff=0)
file_altro_submenu.add_command(label='ciao')
file_altro_submenu.add_command(label='buongiorno')
file_menu.add_cascade(label='Altro', menu=file_altro_submenu)

file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)


menubar.add_cascade(label='File', menu=file_menu)


root.mainloop()