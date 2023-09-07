# 13 notebook (tab)

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext

root=Tk()
root.title('Il nostro programma')
root.geometry('600x400')

notebook = ttk.Notebook(root)
notebook.pack(pady=10, fill=BOTH, expand=True)

frame1 = ttk.Frame(notebook, width=400, height=280)
frame2 = ttk.Frame(notebook, width=400, height=280)
frame3 = ttk.Frame(notebook, width=400, height=280)
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)

notebook.add(frame1, text="tab1")
notebook.add(frame2, text="tab2")
notebook.add(frame3, text="tab3")
label1 = Label(frame1, text="ciao").pack()
label2 = Label(frame2, text="buongiorno").pack()
label3 = Label(frame3, text="notte").pack()
root.mainloop()