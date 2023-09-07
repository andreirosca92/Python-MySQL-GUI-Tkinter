# 04 label
# creare label e mostrarla, background, cursore
# font, foreground, allineamento, padding, immagine
"""
import tkinter as tk 
 
class App(tk.Tk): 
    def __init__(self): 
        super().__init__() 
        self.title("My Tkinter app") 
        self.iconphoto(False, tk.PhotoImage(file='recycling.png'))

        self.geometry("400x200+10+10") 
 
if __name__ == "__main__":
    app = App()
    try:
        app.mainloop()
    except (RuntimeError, TypeError, NameError):
        print('Error generic')
    except _tkinter.TclError:
        print('No ico file found')

"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Il nostro programma')
root.geometry('600x400')
photo = PhotoImage(file='./recycling.png')
# foregruound='', background='' con il testo, compound=none la precedenza all'immagine, se tolgo image
# la precedenza al testo
label = Label(text='Ciao \n sono andrei.', padx=50, pady=50, font=('Helvetica', 24), cursor='circle', justify='right',\
              image=photo, compound='top')
label.pack()

root.mainloop()
