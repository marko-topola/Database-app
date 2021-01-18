from tkinter import *
import sqlite3

root= Tk()
root.title("Database app")
root.geometry("400x400")


''' 
c.execute("""CREATE TABLE address_book (
        f_name text,
        l_name text,
        adress text,
        city text,
        zipcode integer   
)""")

'''
def update():
    conn = sqlite3.connect("address_book.db")

    c = conn.cursor()

    record_id = delete_box.get()

    c.execute("""UPDATE addresses  SET 
     first_name = :first,
     last_name = :last,
     adress = :address,
     city = :city,
     zipcode = zipcode
     
     WHERE oid = :oid""",
    {"first":f_name_editor.get(),
     "last":l_name_editor.get(),
     "address":adress_editor.get(),
     "city":city_editor.get(),
     "zipcode":zipcode_editor.get(),
     "oid":record_id
     })

    conn.commit()

    conn.close()




def edit():
    editor = Tk()
    editor.title("Update record app")
    editor.geometry("400x400")

    conn = sqlite3.connect("address_book.db")

    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()

    global  f_name_editor
    global l_name_editor
    global adress_editor
    global city_editor
    global zipcode_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20)

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)

    adress_editor = Entry(editor, width=30)
    adress_editor.grid(row=2, column=1)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)

    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=4, column=1)


    f_name_label = Label(editor, text="First name")
    f_name_label.grid(row=0, column=0)

    l_name_label = Label(editor, text="Last name")
    l_name_label.grid(row=1, column=0)

    adress_label = Label(editor, text="Adress")
    adress_label.grid(row=2, column=0)

    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)

    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=4, column=0)

    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        adress_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        zipcode_editor.insert(0,record[4])


    edit_btn = Button(editor, text="Save Record ", command=update)
    edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=144)

def delete():
    conn = sqlite3.connect("address_book.db")

    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid= "+ delete_box.get())
    delete_box.delete(0, END)

    conn.commit()

    conn.close()


def sumbit():
    conn = sqlite3.connect("address_book.db")

    c = conn.cursor()

    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :adress, :city, :zipcode)",
              {
                  "f_name":f_name.get(),
                  "l_name":l_name.get(),
                  "adress":adress.get(),
                  "city":city.get(),
                  "zipcode":zipcode.get()
              }

              )

    conn.commit()

    conn.close()



    f_name.delete(0,END)
    l_name.delete(0,END)
    adress.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)

def query():
    conn = sqlite3.connect("address_book.db")

    c = conn.cursor()

    c.execute("SELECT *,oid FROM addresses")
    records = c.fetchall()
    print(records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[5]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)
    conn.commit()

    conn.close()


f_name = Entry(root,width =30)
f_name.grid(row=0,column=1,padx=20)

l_name = Entry(root,width =30)
l_name.grid(row=1,column=1)

adress = Entry(root,width=30)
adress.grid(row=2,column=1)

city = Entry(root,width=30)
city.grid(row=3,column=1)

zipcode = Entry(root,width=30)
zipcode.grid(row=4,column=1)

delete_box = Entry(root,width=30)
delete_box.grid(row=8,column=1,pady=5)

f_name_label= Label(root, text="First name")
f_name_label.grid(row=0,column=0)

l_name_label = Label(root,text="Last name")
l_name_label.grid(row=1,column=0)

adress_label = Label(root,text="Adress")
adress_label.grid(row=2,column=0)

city_label = Label(root,text="City")
city_label .grid(row=3, column=0)

zipcode_label = Label(root,text="Zipcode")
zipcode_label.grid(row=4,column=0)

delete_label = Label(root,text="Select ID")
delete_label.grid(row=8,column=0)



sumbit_btn = Button(root,text="Add Record to Database" , command=sumbit)
sumbit_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10 ,ipadx=10)

query_btn=Button(root,text="Show Records", command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

delete_btn = Button(root,text="Delete record",command=delete)
delete_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

edit_btn = Button(root,text="Edit record ", command=edit)
edit_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=144)


mainloop()