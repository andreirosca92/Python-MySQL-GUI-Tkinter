# 11 Layout management
# pack place
# grid

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Il nostro programma')
root.geometry('600x400')
"""
# Esempio pratico con Pack (accoda in verticale o in orizzontale)
label1 = Label(root, text="Label 1", background="green", foreground="white")
# padx e pady è la distanza del widget rispetto il contenito (o posizione) (padding esterno)
# ipadx e ipady è lo spazio tra il bordo dell'elemento è il suo contenuto (padding interno)
# side=RIGHT, LEFT, BOTTOM, TOP
label1.pack(ipadx=10, ipady=10, fill=X)

label2 =  Label(root, text="Label 2", background="red", foreground="white")
label2.pack(ipadx=10, ipady=10, fill=X)

label3 =  Label(root, text="Label 3", background="green", foreground="white")
label3.pack(ipadx=10, ipady=10, fill=X)

label4 =  Label(root, text="Label 4", background="purple", foreground="white")
label4.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

label5 =  Label(root, text="Label 5", background="yellow", foreground="white")
label5.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)

label6 =  Label(root, text="Label 6", background="orange", foreground="white")
label6.pack(ipadx=10, ipady=10, fill=BOTH, expand=True, side=LEFT)
"""
# Grid (Griglia)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

frame1 = Frame(root, background="red", height=200, width=200)
frame2 = Frame(root, background="purple", height=200, width=200)
frame3 = Frame(root, background="yellow", height=200, width=200)
frame4 = Frame(root, background="cyan", height=200, width=200)

frame1.grid(column=0, row=0, rowspan=2)
frame2.grid(column=1, row=0)
#frame3.grid(column=0, row=1)
frame4.grid(column=1, row=1)

root.mainloop()