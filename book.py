import pandas as pd
import mysql.connector as sqlt
from tabulate import tabulate
import matplotlib.pyplot as plt
con=sqlt.connect(host="localhost",user="root", passwd="manas1234", database="library")
cursor=con.cursor()

def book_input():
    try:
        bookid=input("Enter Book ID")
        bname=input("Enter Book Name")
        author=input("Enter Author Name")
        price=float(input("Enter Price"))
        copies=int(input("Enter No of Copies"))
        qry="insert into book values({},'{}','{}',{},{},{});".format(bookid,bname,author,price,copies,copies)
        cursor.execute(qry)   
        con.commit()
        print("Added Succesfully")
    except:
        print("Error Occured")
def book_edit():
    try:
        x=int(input("Enter Book Id"))
        qry="select * from book where bookid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            y=float(input("Enter New Price"))
            qry="update book set price={} where bookid={};".format(y,x)
            cursor.execute(qry)
            con.commit()
            print("Edited Successfully")
        else:
            print("Doesn't Exist! Enter valid Book ID")
    except:
        print("Error Occured")
def book_delete():
    try:
        x=int(input("Enter Book ID"))
        qry="select * from book where bookid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            qry="delete from book where bookid={};".format(x)
            cursor.execute(qry)
            con.commit()
            print("Deleted Successfully")
        else:
            print("Doesn't Exist! Enter valid Book ID")
    except:
        print("Error Occured")
        
def book_search():
    try:
        x=int(input("Enter Book ID"))
        qry="select * from book where bookid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            df=pd.read_sql(qry,con)
            print(tabulate(df,headers='keys',tablefmt='psql' ,showindex=False,))
        else:
            print("Doesn't Exist! Enter valid Book ID")
    except:
        print("Error Occured")