from sqlite3 import Cursor
from tkinter import *
import time
from tkinter import ttk, messagebox,filedialog
import sqlite3
import pandas


# functions
def clock():
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'    Date: {date}\nTime:{currenttime}')
    datetimeLabel.after(1000, clock)

# Add Employee
def add_employee():
    def add_data():
        if idEntry.get() == '' or nameEntry.get() == '' or departmentEntry.get() == '' or emailAddressEntry.get() == '' or mobileNumberEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:

            try:
                query = "INSERT INTO Employees (id, name, department, emailAddress, mobileNo, dob) VALUES (?, ?, ?, ?, ?, ?)"
                values = (
                    idEntry.get(), nameEntry.get(), departmentEntry.get(), emailAddressEntry.get(),
                    mobileNumberEntry.get(),
                    dobEntry.get())
                cur.execute(query, values)
                db.commit()
                result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?')
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    departmentEntry.delete(0, END)
                    emailAddressEntry.delete(0, END)
                    mobileNumberEntry.delete(0, END)
                    dobEntry.delete(0, END)
                else:
                    pass

                query='SELECT * FROM employees'
                cur.execute(query)
                fetched_data=cur.fetchall()
                employeeTable.delete(*employeeTable.get_children())

                for data in fetched_data:
                    datalist=list(data)
                    employeeTable.insert('',END,values=datalist)
            except:
                messagebox.showerror('Error', 'Id cannot be repeated')
                return

    add_window = Toplevel()
    add_window.title('Add Employee')
    add_window.grab_set()
    add_window.resizable(False, False)

    idLabel = Label(add_window, text='id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(add_window, font=('times new roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(add_window, font=('times new roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    departmentLabel = Label(add_window, text='Department', font=('times new roman', 20, 'bold'))
    departmentLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    departmentEntry = Entry(add_window, font=('times new roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=2, column=1, padx=10, pady=15)

    emailAddressLabel = Label(add_window, text='Email Address', font=('times new roman', 20, 'bold'))
    emailAddressLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailAddressEntry = Entry(add_window, font=('times new roman', 15, 'bold'), width=24)
    emailAddressEntry.grid(row=3, column=1, padx=10, pady=15)

    mobileNumberLabel = Label(add_window, text='Mobile Number', font=('times new roman', 20, 'bold'))
    mobileNumberLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    mobileNumberEntry = Entry(add_window, font=('times new roman', 15, 'bold'), width=24)
    mobileNumberEntry.grid(row=4, column=1, padx=10, pady=15)

    dobLabel = Label(add_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(add_window, font=('times new roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=15)

    add_employee_button = Button(add_window, text='ADD EMPLOYEE', width=25, command=add_data)
    add_employee_button.grid(row=7, columnspan=2, pady=15)


# Search Employee
def search_employee():

    def search_data():
        query = 'SELECT * FROM employees WHERE id=? or name=? or department=? or emailAddress=? or mobileNo=? or dob=?'
        cur.execute(query,(
        idEntry.get(), nameEntry.get(), departmentEntry.get(), emailAddressEntry.get(), mobileNumberEntry.get(),
        dobEntry.get()))
        employeeTable.delete(*employeeTable.get_children())
        fetch_data = cur.fetchall()
        for data in fetch_data:
            employeeTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.title('Search Employee')
    search_window.grab_set()
    search_window.resizable(False, False)

    idLabel = Label(search_window, text='id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    departmentLabel = Label(search_window, text='Department', font=('times new roman', 20, 'bold'))
    departmentLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    departmentEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=2, column=1, padx=10, pady=15)

    emailAddressLabel = Label(search_window, text='Email Address', font=('times new roman', 20, 'bold'))
    emailAddressLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailAddressEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    emailAddressEntry.grid(row=3, column=1, padx=10, pady=15)

    mobileNumberLabel = Label(search_window, text='Mobile Number', font=('times new roman', 20, 'bold'))
    mobileNumberLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    mobileNumberEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    mobileNumberEntry.grid(row=4, column=1, padx=10, pady=15)

    dobLabel = Label(search_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('times new roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=15)

    search_employee_button = Button(search_window, text='SEARCH', width=25, command=search_data)
    search_employee_button.grid(row=7, columnspan=2, pady=15)

    query = 'SELECT * FROM employees'
    cur.execute(query)
    fetch_data = cur.fetchall()
    employeeTable.delete(*employeeTable.get_children())
    for data in fetch_data:
        datalist=list(data)
        employeeTable.insert('', END, values=data)

# Delete Employee
def delete_employee():
    indexing = employeeTable.focus()
    print(indexing)
    content = employeeTable.item(indexing)
    content_id = content['values'][0]
    query = 'DELETE FROM employees WHERE id=?'
    #cur.execute(query, content_id)
    cur.execute(query, (content_id,))
    db.commit()
    messagebox.showinfo('Deleted', f'Id {content_id} is deleted succesfully')
    query='SELECT * FROM employees'
    cur.execute(query)
    fetched_data=cur.fetchall()
    employeeTable.delete(*employeeTable.get_children())
    for data in fetched_data:
        employeeTable.insert('',END,values=data)

#Update Employee
def update_employee():

    def update_data():
        query='UPDATE employees SET name=?,department=?,emailAddress=?,mobileNo=?,dob=? WHERE id=?'
        cur.execute(query,(nameEntry.get(),departmentEntry.get(),emailAddressEntry.get(),mobileNumberEntry.get(),dobEntry.get(),idEntry.get()))
        db.commit()
        messagebox.showinfo('Success', f'id{idEntry.get()} is modified successfully')
        update_window.destroy()
        show_employee()

    update_window = Toplevel()
    update_window.title('Update Employee')
    update_window.grab_set()
    update_window.resizable(False, False)

    idLabel = Label(update_window, text='id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('times new roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    nameLabel = Label(update_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('times new roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    departmentLabel = Label(update_window, text='Department', font=('times new roman', 20, 'bold'))
    departmentLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    departmentEntry = Entry(update_window, font=('times new roman', 15, 'bold'), width=24)
    departmentEntry.grid(row=2, column=1, padx=10, pady=15)

    emailAddressLabel = Label(update_window, text='Email Address', font=('times new roman', 20, 'bold'))
    emailAddressLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailAddressEntry = Entry(update_window, font=('times new roman', 15, 'bold'), width=24)
    emailAddressEntry.grid(row=3, column=1, padx=10, pady=15)

    mobileNumberLabel = Label(update_window, text='Mobile Number', font=('times new roman', 20, 'bold'))
    mobileNumberLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    mobileNumberEntry = Entry(update_window, font=('times new roman', 15, 'bold'), width=24)
    mobileNumberEntry.grid(row=4, column=1, padx=10, pady=15)

    dobLabel = Label(update_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(update_window, font=('times new roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=15)

    update_employee_button = Button(update_window, text='UPDATE', width=25, command=update_data)
    update_employee_button.grid(row=7, columnspan=2, pady=15)

    indexing=employeeTable.focus()
    content=employeeTable.item(indexing)
    listdata=content['values']
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    departmentEntry.insert(0,listdata[2])
    emailAddressEntry.insert(0,listdata[3])
    mobileNumberEntry.insert(0,listdata[4])
    dobEntry.insert(0,listdata[5])

#Show Employee
def show_employee():
    query = 'SELECT * FROM employees'
    cur.execute(query)
    fetched_data = cur.fetchall()
    employeeTable.delete(*employeeTable.get_children())
    for data in fetched_data:
        employeeTable.insert('', END, values=data)

# Export Data
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=employeeTable.get_children()
    newlist=[]
    for index in indexing:
        content=employeeTable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['id','Name','Department','Email Address','Mobile No','DOB'])
    table.to_csv(url,index=False)
    messagebox.showinfo('success','Data is saved successfully')

# Exit
def iexit():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

# connect to database
    global db, cur
db = sqlite3.connect("employees.db")
cur: Cursor = db.cursor()
query = cur.execute("Drop table if exists Employees")
query = cur.execute("CREATE table Employees (id INTEGER PRIMARY KEY, Name TEXT (30), Department TEXT (30), EmailAddress TEXT(30), MobileNo "
                    "INTEGER (11), DOB VARCHAR (30))")

db.commit()

# GUI
root = Tk()

root.geometry('1280x700+0+0')

# root.resizable(0,0)
root.title('Employee Management System')

# Date,Time
datetimeLabel = Label(root, font=('times new roman', 15, 'bold'))
datetimeLabel.place(x=5,y=5)
clock()

# heading
headingLabel = Label(root, text='EMPLOYEE MANAGEMENT SYSTEM', font=('times new roman', 28, 'bold'), width=40)
headingLabel.place(x=200,y=0)

# left frame
leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

# logo image
logo_image = PhotoImage(file='employee.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0)
# add button
addemployeeButton = Button(leftFrame, text='Add Employee', width=25, command=add_employee)
addemployeeButton.grid(row=1, column=0, pady=20)
# search button
searchemployeeButton = Button(leftFrame, text='Search Employee', width=25, command=search_employee)
searchemployeeButton.grid(row=2, column=0, pady=20)
# delete button
deleteemployeeButton = Button(leftFrame, text='Delete Employee', width=25, command=delete_employee)
deleteemployeeButton.grid(row=3, column=0, pady=20)
# update button
updateemployeeButton = Button(leftFrame, text='Update Employee', width=25, command=update_employee)
updateemployeeButton.grid(row=4, column=0, pady=20)
# show button
showemployeeButton = Button(leftFrame, text='Show Employee', width=25, command=show_employee)
showemployeeButton.grid(row=5, column=0, pady=20)
# export button
exportemployeeButton = Button(leftFrame, text='Export Data', width=25, command=export_data)
exportemployeeButton.grid(row=6, column=0, pady=20)
# exit button
exitButton = Button(leftFrame, text='Exit', width=25, command=iexit)
exitButton.grid(row=7, column=0, pady=20)

# right frame
rigtFrame = Frame(root)
rigtFrame.place(x=350, y=80, width=820, height=600)

scrollBarX = Scrollbar(rigtFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rigtFrame, orient=VERTICAL)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

employeeTable = ttk.Treeview(rigtFrame, columns=('Id', 'Name', 'Department', 'Email', 'Mobile No',
                                                 'D.O.B'),
                             xscrollcommand=scrollBarX.set,
                             yscrollcommand=scrollBarY.set)

scrollBarX.config(command=employeeTable.xview)
scrollBarY.config(command=employeeTable.yview)

employeeTable.pack(fill=BOTH, expand=1)

# adding name to the column headings
employeeTable.heading('Id', text='Id')
employeeTable.heading('Name', text='Name')
employeeTable.heading('Department', text='Department')
employeeTable.heading('Email', text='Email Address')
employeeTable.heading('Mobile No', text='Mobile No')
employeeTable.heading('D.O.B', text='D.O.B')

employeeTable.config(show='headings')

root.mainloop()
