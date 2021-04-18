import tkinter as tk
from tkinter import *
import tkinter.font as tkFont
import mysql.connector
import datetime
from tkinter import messagebox

t = datetime.datetime.now()

#declare the db connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "cyborg13",
    database = "dbgui_ems_beta",
    port = 3307
    
    )
#declare the db cursor
mycursor = mydb.cursor()

#declare function for updating inventory

#update inventory second phase
def update_inv2():
    
        cust = str(up1.get())
        meat_ = str(up2.get())
        dim = int(up3.get())
        '''
        dim2 = int(dim)
        cust2 = str(cust)
        meat_2 = str(meat_)
        '''
        sql = "select * from frozen_meat where meats = %s"
        
        mycursor.execute(sql, (meat_,))
        res = mycursor.fetchall()
        t1 = dim * 60
        for y in res:
            print(y[0])
            print(y[1] - dim)
            print(y[2])
            print(y[4])
        sql = "insert into frozen_meat (meats, stocks, price, total, total_omit, time_update, customer) values (%s, %s, %s, %s, %s, %s, %s) "
        val = (meat_, y[1]-dim, y[2],t1, dim, t, cust)
        mycursor.execute(sql, val)
        mydb.commit()
        #top4.destroy()

    
#update inventory first stage
def update_inventory():
    global up1
    global up2
    global up3
    top.destroy()
    top4 = tk.Tk()
    top4.title("EMS")
    top4.geometry("250x150")
    #declare stringvars for update
    up1 = StringVar()
    up2 = StringVar()
    up3 = StringVar()
    #gui for update inv
    lb5 = Label(top4, text = 'name of customer').grid(column = 0)
    e23 = Entry(top4,bd = 5, textvariable = up1 ).grid(row = 0, column = 1)
    lb6 = Label(top4, text = 'kind of meat').grid(row = 1, column = 0)
    e24 = Entry(top4, bd = 5, textvariable = up2).grid(row = 1, column = 1)
    lb7 = Label(top4, text = "qty").grid(row = 2, column = 0)
    e25 = Entry(top4, bd = 5, textvariable = up3).grid(row = 2, column = 1)
    b6 = tk.Button(top4, text = 'update', command = update_inv2).grid(row = 5, column = 0)
    

#combine functions
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

#declare second stage for restock

def restock():
    top3.destroy()
    pr1 = p1.get()
    pr2 = p2.get()
    pr3 = p3.get()
    pr4 = p4.get()
    pr5 = p5.get()
    pr6 = p6.get()
    pr7 = p7.get()
    pr8 = p8.get()
    pr9 = p9.get()
    pr10 = p10.get()
    pr11 = p11.get()
    #restock get entry
    restock1 = s1.get()
    restock2 = s2.get()
    restock3 = s3.get()
    restock4 = s4.get()
    restock5 = s5.get()
    restock6 = s6.get()
    restock7 = s7.get()
    restock8 = s8.get()
    restock9 = s9.get()
    restock10 = s10.get()
    restock11 = s11.get()
    
    mycursor = mydb.cursor()
    sql = "insert into frozen_meat (meats, stocks, price, time_update) values (%s, %s, %s, %s)"
    val =[
    (str(pr1), int(restock1), 60, t),
    (str(pr2), int(restock2), 60, t),
    (str(pr3), int(restock3), 60, t),
    (str(pr4), int(restock4), 60, t),
    (str(pr5), int(restock5), 60, t),
    (str(pr6), int(restock6), 60, t),
    (str(pr7), int(restock7), 60, t),
    (str(pr8), int(restock8), 60, t),
    
    (str(pr9), int(restock9), 60, t),
    (str(pr10), int(restock10), 60, t),
    (str(pr11), int(restock11), 60, t)
    ]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

#declare restock first stage
def restock2():
    top.destroy()
    top3 = tk.Tk()
    top3.title("EMS")
    #declare into string var of meat name
    p1 = StringVar()
    p2 = StringVar()
    p3 = StringVar()
    p4 = StringVar()
    p5 = StringVar()
    p6 = StringVar()
    p7 = StringVar()
    p8 = StringVar()
    p9 = StringVar()
    p10 = StringVar()
    p11 = StringVar()

    #declare stringvar of stocks
    s1 = StringVar()
    s2 = StringVar()
    s3 = StringVar()
    s4 = StringVar()
    s5 = StringVar()
    s6 = StringVar()
    s7 = StringVar()
    s8 = StringVar()
    s9 = StringVar()
    s10 = StringVar()
    s11 = StringVar()


    
    #declare into entries
    #declare label text
    lb3 = Label(top3, text='meats').grid(row = 0)
    lb4 = Label(top3, text = 'no. stocks').grid(row=0,column=1)
    #stocks1
    e12 = Entry(top3, bd = 5, textvariable = s1).grid(column=1)
    e1 = Entry(top3, bd = 5, textvariable = p1).grid(row=1)
    #stocks2
    e13 = Entry(top3, bd = 5, textvariable = s2).grid(column=1)
    e2 = Entry(top3, bd = 5, textvariable = p2).grid(row=2)
    #stocks3
    e14 = Entry(top3, bd = 5, textvariable = s3).grid(column=1)
    e3 = Entry(top3, bd = 5, textvariable = p3).grid(row=3)
    #stocks4
    e15 = Entry(top3, bd = 5, textvariable = s4).grid(column=1)
    e4 = Entry(top3, bd = 5, textvariable = p4).grid(row=4)
    #stocks5
    e16 = Entry(top3, bd = 5, textvariable = s5).grid(column=1)
    e5 = Entry(top3, bd = 5, textvariable = p5).grid(row=5)
    #stocks6
    e17 = Entry(top3, bd = 5, textvariable = s6).grid(column=1)
    e6 = Entry(top3, bd = 5, textvariable = p6).grid(row=6)
    #stocks7
    e18 = Entry(top3, bd = 5, textvariable = s7).grid(column=1)
    e7 = Entry(top3, bd = 5, textvariable = p8).grid(row=7)
    #stocks8
    e19 = Entry(top3, bd = 5, textvariable = s8).grid(column=1)
    e8 = Entry(top3, bd = 5, textvariable = p8).grid(row=8)
    #stocks9
    e20 = Entry(top3, bd = 5, textvariable = s9).grid(column=1)
    e9 = Entry(top3, bd = 5, textvariable = p9).grid(row=9)
    #stocks10
    e21 = Entry(top3, bd = 5, textvariable = s10).grid(column=1)
    e10 = Entry(top3, bd = 5, textvariable = p10).grid(row=10)
    #stocks11
    e22 = Entry(top3, bd = 5, textvariable = s11).grid(column=1)
    e11 = Entry(top3, bd = 5, textvariable = p11).grid(row=11)
    
    b5 = tk.Button(top3, text = "restock", command = restock).grid(row=12)
    #declare stocks entry
   
    
    
                                   
    

#second stage fetch    
def fetch2():
     global top2
     v = product_.get()
     top1.destroy()
     sql = "select * from frozen_meat where meats = %s"
     val = (str(v))

     mycursor.execute(sql, (val,))
     res = mycursor.fetchall()
     for x in res:
         re = ("product:",x[0],"|", "stocks:",str(x[1]),"|", "price:",str(x[2]),"|", "total:", str(x[3]), "|","omitted:", str(x[4]),"|","time updated:",str(x[5]),"|","customer:",str(x[6]))
     top2 = tk.Tk()
     top2.title("EMS")
     top2.geometry("700x120")
     lb1 = Label(top2, text = re ).pack()
    
     b4 = tk.Button(top2, text = "main window", command = combine_funcs(mainwindow(), closet2())).pack()
     
     top2.mainloop()
     #fetch()


#first stage fetch
def fetch():
     #top2.destroy()
     global product_
     global top1
     top.destroy()
     top1 = tk.Tk()
     top1.title("EMS")
     top1.geometry("200x200")
     lb = Label(top1, text = "enter meat name").pack()

     product_ = StringVar()

     e = Entry(top1, bd = 5, textvariable=product_).pack()
     b3 = tk.Button(top1, text='search', command = fetch2).pack()
     top1.mainloop()
    #while True:

#function for closing the top2 window
def closet2():
    top2.destroy()

#declare the main window
def mainwindow():
    global top
    top = tk.Tk()
    top.title("EMS")
    top.geometry("200x200")

    b = tk.Button(top, text='update inventory', command = update_inventory).pack()
    b1 = tk.Button(top, text='restock', command = restock2).pack()
    b2 = tk.Button(top, text='show inventory', command = fetch).pack()

    top.mainloop()
mainwindow()
