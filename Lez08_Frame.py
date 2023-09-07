# 09 frame
# cosa sono, crearne uno e multipli, padding, background, inserire widget all'interno

from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Il nostro programma")
root.geometry('600x400')

frame1 = LabelFrame(root,text="sono un labelframe", padx=10, pady=50, height=100, width=400)
frame2 = Frame(root, background="yellow", padx=10, pady=50, height=100, width=400)
frame3 = Frame(root, background="green", padx=10, pady=50, height=100, width=400)

#fill=BOTH riempe tutto 
#frame1.pack(fill=X, expand=True)
frame1.pack(fill=BOTH, expand=True)
frame2.pack(fill=BOTH, expand=True)
frame3.pack(fill=BOTH, expand=True)
"""
button1 = Button(frame1, text='ciao')
button1.pack()
"""
button1 = Button(frame1, text="ciao")
button2 = Button(frame2, text="hello")
button3 = Button(frame3, text="hola")
button1.pack()
button2.pack()
button3.pack()
root.mainloop()