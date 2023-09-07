# 08 entry
# creare esempio di login

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Il nostro programma')

root.geometry('600x400')
def login():
    print(email_entry.get())
    print(password_entry.get())
    
label_email = Label(root, text="Email")
label_email.pack(padx=5, pady=5)

email = StringVar()
email_entry = ttk.Entry(root, textvariable=email)
email_entry.pack(padx=5, pady=5)
email_entry.focus() # cursore sull'email all'inizio

label_password = Label(root, text="Password")
label_password.pack(padx=5, pady=5)

password = StringVar()
password_entry = ttk.Entry(root, textvariable=password, show="*")
password_entry.pack(padx=5, pady=5)

button = ttk.Button(root, text="Login", command=login)
button.pack(padx=10, pady=10)

root.mainloop()