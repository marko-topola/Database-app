from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry("400x400")

conn= sqlite3.connect("address_book.db")

c= conn.cursor()

c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        adress text,
        city text,
        zipcode integer   
)""")


conn.commit()

conn.close()

root.mainloop()