# 19 lavorare con database mysql
# impostare db, installare mysql-connector-python, inserire dati di prova
# select, insert, update, delete


from tkinter import *
from tkinter import ttk
import mysql.connector
root = Tk()
root.title('il nostro programma')

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tutorial_mysql"
)

cursore = db.cursor()
cursore.execute("SELECT * FROM utenti")
risultato = cursore.fetchall()
colonne = ('id', 'email', 'username', 'password')
tabella = ttk.Treeview(root, columns=colonne, show='headings')
tabella.heading('id', text='ID')
tabella.heading('email', text='email')
tabella.heading('username', text="Username")
tabella.heading('password', text="Password")

for riga in risultato:
    tabella.insert('', END, values=riga)
tabella.grid(row=0, column=0, sticky="nswe")

def inserisci():
    insert_sql="INSERT INTO utenti (id, email, username, password) VALUES (%s,%s, %s, %s)"
    inserisci_valori = (3,"johnny@gmeil.it", "johnnygianni", "wiyuiiwer")
    
    cursore.execute(insert_sql, inserisci_valori)
    db.commit()
def modifica():
    modifica_sql="UPDATE utenti SET email=%s, username=%s, password=%s WHERE id=3"
    valori = ("bibbo@bibbo.it","bibbo2023","ciao123")
    cursore.execute(modifica_sql,valori)
    db.commit()
def elimina():
    elimina_sql = "DELETE FROM utenti WHERE id=3"
    cursore.execute(elimina_sql)
    db.commit()
def refresh():
    visualizza_sql = "SELECT * FROM utenti";
    cursore.execute(visualizza_sql)
    
    risultato = cursore.fetchall()
    colonne = ('id', 'email', 'username', 'password')
    tabella = ttk.Treeview(root, columns=colonne, show='headings')
    tabella.heading('id', text='ID')
    tabella.heading('email', text='email')
    tabella.heading('username', text="Username")
    tabella.heading('password', text="Password")
    for riga in risultato:
        tabella.insert('', END, values=riga)
    tabella.grid(row=0, column=0, sticky="nswe")
    
inserisci_btn = Button(root, text="inserisci", command=inserisci)
modifica_btn = Button(root,text="modifica", command=modifica)
elimina_btn = Button(root, text="elimina", command=elimina)
refresh_btn = Button(root, text="visualizza", command=refresh)

inserisci_btn.grid(row=1, column=0, sticky="we")
modifica_btn.grid(row=2, column=0, sticky="we")
elimina_btn.grid(row=3, column=0, sticky="we")
refresh_btn.grid(row=4,column=0, sticky="we")

root.mainloop()
