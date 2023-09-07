# 20 creare un file exe
# installare pyinstaller, controllare programma, generare exe, testare
from tkinter import *
from tkinter import ttk
import time
import threading 
root = Tk()
root.title('il nostro programma')
root.geometry('600x400')

def dormi():
    time.sleep(5) # 5s
    print("stavo dormendo...")
def mangia():
    print("sto mangiando...")

button1 = Button(root, text="dormi", command=lambda: threading.Thread(target=dormi).start() ).pack(expand=True, fill=X)
button2 = Button(root, text="mangia", command=mangia).pack(expand=True, fill=X)

root.mainloop()