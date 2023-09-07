# 03 finestre in tk

# creare finestra, geometry (dimensioni e posizione), icona
# resizable, dimensioni minime e massime, trasparenza
# stack con topmost, lift e lower
# www.flaticon.com
# www.converti.co
import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("il nostro programma")
root.geometry('600x400') # dimensione 600x400,  x e y +50+50
#root.iconbitmap('/home/andrei/PROGRAMMAZIONE_GENERALE/PYTHON/Youtube/Midali_youtube/Tkinter_tutorial/google.ico')
#root.iconphoto(False, root.PhotoImage(file="./prova.png"))
  
#root.resizable(False, False) # resize x non è possibile

root.minsize(400, 100)
root.maxsize(1000, 1000)

#root.attributes('-alpha', 0.5)
# stack delle finestre

#root.attributes('-topmost',1)
root.lower()
root.mainloop()
