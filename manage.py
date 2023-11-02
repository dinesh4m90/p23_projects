from tkinter import *
from tkinter import ttk
import mysql.connector
window = Tk()
window.geometry('1500x500')
window.title('Apply')
font = ('DM Sans', 20)

connection = mysql.connector.connect(host='localhost', user='dinesh4m90', password='Dinesh4Mysql@1990',
                                     port='3306', database='tenant_management')
c = connection.cursor()

Main_F = Frame(master=window, bg='white')
Main_F.pack(side=LEFT)
Main_F.configure(width=1500, height=500)

Menu_F = Frame(master=window, bg='black')
Menu_F.pack(side=LEFT)
Menu_F.configure(width=100, height=500)

Appl_F = Frame(master=Main_F)
Appl_F.pack(side=LEFT, pady=40)
Appl_F.configure(width=600, height=500)

View_F = Frame(master=Main_F,relief=RAISED)
View_F.pack(side=LEFT,pady=40)
View_F.configure(width=800, height=500)

def insertdata():
    connection = mysql.connector.connect(host='localhost', user='dinesh4m90', password='Dinesh4Mysql@1990',
                                             port='3306', database='tenant_management')
    c = connection.cursor()

    Name = Aent_1.get()
    Age = Aent_2.get()
    Sex = combo.get()
    Address = Aent_3.get("1.0",'end-1c')
    Contact_No = Aent_4.get()

    insert_query = "INSERT INTO `tenant_details`(`Name`, `Age`, `Sex`, `Address`,`Contact_No`)VALUES (%s,%s,%s,%s,%s)"

    vals = (Name, Age, Sex, Address, Contact_No)
    c.execute(insert_query, vals)
    connection.commit()
    # connection.close()

Alab_1=Label(master=Appl_F, text="Name:", font=font)
Alab_2 = Label(master=Appl_F, text="Age:", font=font)
Alab_3 = Label(master=Appl_F, text="Address:", font=font)
Alab_4 = Label(master=Appl_F, text="Contact No:", font=font)
Alab_5 = Label(master=Appl_F, text="Sex:", font=font)
Aent_1 = Entry(master=Appl_F, font=font)
Aent_2 = Entry(master=Appl_F, font=font)
Aent_3 = Text(master=Appl_F, font=font)
Aent_4 = Entry(master=Appl_F, font=font)

combo = ttk.Combobox(master=Appl_F, values=["Male", "Female", "Transgender"], font=font)
Abtn = Button(master=Appl_F, text="Update", font=font,bg='orange', command=insertdata)

Alab_1.pack()
Alab_1.place(x=20, y=50)
Alab_2.pack()
Alab_2.place(x=20, y=100)
Alab_3.pack()
Alab_3.place(x=20, y=150)
Alab_4.pack()
Alab_4.place(x=20, y=275)
Alab_5.pack()
Alab_5.place(x=300, y=100)

Aent_1.pack()
Aent_1.place(x=200, y=50, width=355)
Aent_2.pack()
Aent_2.place(x=200, y=100, width=100)
Aent_3.pack()
Aent_3.place(x=200, y=150, width=355, height= 100)
Aent_4.pack()
Aent_4.place(x=200, y=275, width=355)

combo.pack()
combo.place(x=375, y=100, width=180)

Abtn.pack()
Abtn.place(x=20, y=325, width=150)

def menu_b():
    # connection = mysql.connector.connect(host='localhost', user='dinesh4m90', password='Dinesh4Mysql@1990',
    #                                      port='3306', database='tenant_management')
    # c = connection.cursor()

    query = "SELECT * FROM tenant_details"
    c.execute(query)


    i = 0
    for tenant_details in c:
        for j in range(len(tenant_details)):
            e = Entry(View_F, width=25, fg='black')
            e.grid(row=i, column=j)
            e.insert(END, tenant_details[j])
        i = i + 1

    connection.commit()

def H_blink():
    # lab_1.config(bg='black')
    lab_2.config(bg='black')
    # lab_4.config(bg='black')
def blink(b, func):
    H_blink()
    b.config(bg='Green')
    func()

# btn_1 = Button(master=Menu_F, text="Apply Now", command= lambda : blink(lab_1,insertdata))
# btn_1.place(x=15, y=50)

# lab_1 = Label(master=Menu_F, text=" ",bg='black')
# lab_1.place(x=5, y=52)

btn_2 = Button(master=Menu_F, text="Check Status", command= lambda:blink(lab_2,menu_b))
btn_2.place(x=15, y=100)

lab_2 = Label(master=Menu_F, text=" ",bg='black')
lab_2.place(x=5, y=102)
#
# btn_4 = Button(master=Menu_F, text="About", command= lambda:blink(lab_4))
# btn_4.place(x=15, y=450)
#
# lab_4 = Label(master=Menu_F, text=" ",bg='black')
# lab_4.place(x=5, y=452)

# data_text = Text(view_frame, height=10, width=40)
# data_text.pack()

window.mainloop()