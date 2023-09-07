# 15 context menu
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Il nostro programma')
root.geometry('800x600')


label = Label(root, text="ciao", background="red")
label.pack(expand=True, fill=BOTH)
# context menu
ctx_menu = Menu(root, tearoff=0)
ctx_menu.add_command(label="Taglia")
ctx_menu.add_command(label="Copia")
ctx_menu.add_command(label="Incolla")
ctx_menu.add_separator()
ctx_menu.add_command(label="Prova")

def ctx_menu_popup(event):
    try:
        ctx_menu.tk_popup(event.x_root, event.y_root)
    finally:
        ctx_menu.grab_release()          
label.bind("<Button-3>", ctx_menu_popup)
root.mainloop()