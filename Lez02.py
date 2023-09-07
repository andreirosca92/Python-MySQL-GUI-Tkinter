# 02 concetti di tkinter
# widget, gerarchia widget
# layout: pack place e grid
# eventi su widget o bind

# Frame 1 Frame 2
                                        
# Layout pack una sotto l'altro
# Layout place specificare le cordinate di un widget
# Layout grid
# due eventi 1. primo: ttk.Button(mainframe, text="Calculate", command=calculate)
# secondo evento: root.bind("<Return>", calculate) se premo invio mi chiama la funzione calculate
from tkinter import *
from tkinter import ttk

root=Tk()
root.title("Feet to Meters")

mainFrame=ttk.Frame(root, padding="3 3 12 12")
# noi usiamo Layout Grid
mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.mainloop()
