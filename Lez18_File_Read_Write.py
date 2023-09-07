# 18 lavorare con file
# leggere da un file
# scrivere in file

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
root = Tk()
root.title('Il nostro programma')
root.geometry('800x600')

def apri_file():
    """
    # leggere da un file
    filetypes = (
        ('file di testo','*.txt'),
        ('tutti i file', '*.*')
    )
    filename = filedialog.askopenfilename(title="Apri un file", initialdir="/", filetypes=filetypes)
    f = open(filename, 'r')
    data = f.read()
    print(data)
    """
    f = filedialog.asksaveasfile(mode='w', title="salva file", defaultextension='.txt')
    data = "qwertyuiop"
    f.write(data)
    f.close()
    
bottone = ttk.Button(root, text="apri file", command=apri_file)
bottone.pack(expand=True)

root.mainloop()