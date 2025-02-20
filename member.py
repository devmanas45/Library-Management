import mysql.connector as sqlt
import book
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con=sqlt.connect(host="localhost",user="root", passwd="manas1234", database="library")
cursor=con.cursor()
def member_input():
    try:
        memberid=int(input("Enter Member ID"))
        mname=input("Enter Member Name")
        madd=input("Enter Member Address")
        phone=input("Enter Phone")
        qry="insert into member values({},'{}','{}','{}');".format(memberid,mname,madd,phone)
        cursor.execute(qry)
        con.commit()
        print("Added Succesfully")
    except:
        print("Invalid Input")
def member_edit():
    try:
        x=int(input("Enter Member Id"))
        qry="select * from member where memberid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            y=input("Enter New Address")
            qry="update member set madd='{}' where memberid={};".format(y,x)
            cursor.execute(qry)
            con.commit()
            print("Edited Successfully")
        else:
            print("Doesn't Exist! Enter valid Book ID")
    except:
        print("Invalid Input")
def member_delete():
    try:

        x=int(input("Enter Member ID"))
        qry="select * from member where memberid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            qry="delete from member where memberid={};".format(x)
            cursor.execute(qry)
            con.commit()
            print("Deleted Successfully")
        else:
            print("Doesn't Exist! Enter valid Book ID")
    except:
        print("Invalid Input")
def member_search():
    try:
        x=int(input("Enter Member ID"))
        qry="select * from member where memberid={};".format(x)
        cursor.execute(qry)
        r=cursor.fetchone()
        if r:
            df=pd.read_sql(qry,con)
            print(tabulate(df,headers='keys',tablefmt='psql' ,showindex=False))
        else:
            print("Doesn't Exist! Enter valid Member ID")
    except:
        print("Invalid Input")