# 12 scrollbar
# scrollbar applicata a listbox, scrolltext


from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo

root=Tk()
root.title('il nostro programma')
root.geometry('600x400')
"""
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

linguaggi= ('Javascript','Java', 'C', 'C++', 'Pytho', 'PHP', 'Ruby', 'Go',
            'Javascript','Java', 'C', 'C++', 'Pytho', 'PHP', 'Ruby', 'Go',
            'Javascript','Java', 'C', 'C++', 'Pytho', 'PHP', 'Ruby', 'Go',
            'Javascript','Java', 'C', 'C++', 'Pytho', 'PHP', 'Ruby', 'Go',
            'Javascript','Java', 'C', 'C++', 'Pytho', 'PHP', 'Ruby', 'Go',
            'Javascript','Java', 'C', 'C++', 'Pytho', 'PHP', 'Ruby', 'Go',
            'Javascript','Java', 'C', 'C++', 'Pytho', 'PHP', 'Ruby', 'Go',
            
    )

linguaggio_selezionato = StringVar(value=linguaggi)

listbox = Listbox(root, listvariable=linguaggio_selezionato, height=6, selectmode='extended')
listbox.grid(column=0, row=0, sticky='nwes')

scrollbar = ttk.Scrollbar(root, orient='vertical', command=listbox.yview)
scrollbar.grid(column=1, row=0, sticky='ns')

listbox['yscrollcommand'] = scrollbar.set
"""
from turtle import width
from tkinter import scrolledtext
scrolledtxt = scrolledtext.ScrolledText(root, width=50, height=10)
scrolledtxt.pack(fill=BOTH, side=LEFT, expand=True)
root.mainloop()