# 15 messagebox
# messaggio di info, errore e warning
# si/no, ok/cancella, riprova/cancella
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title('Il nostro programma')
root.geometry('800x600')
# showinfo, showerror, showwarning
"""
def show_message():
    messagebox.showwarning(title="Attenzione", message="server in manutenzione fino alle 14:00")
    """
# askyesno, askokcancel, askretrycancel
def show_message():
    risposta = messagebox.askokcancel(title="prova", message="ti piace la pizza con l'ananas")
    if risposta:
        root.destroy()
    
button  = ttk.Button(root, text="mostra messaggio", command=show_message).pack(fill=BOTH, padx=10, pady=10)
root.mainloop()
