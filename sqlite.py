import sqlite3

def createdb(): 
    con = sqlite3.connect("sqlite.db")
    cur = con.cursor()
    cur.execute("CREAT TABLE task()")
