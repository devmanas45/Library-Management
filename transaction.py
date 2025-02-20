import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con=sqlt.connect(host="localhost",user="root", passwd="manas1234", database="library")
cursor=con.cursor()
def book_issue():
    try:
        q="select max(issueid) from issue;"
        cursor.execute(q)
        r=cursor.fetchone()[0]
        if r:
            issueid=r+1
        else:
            issueid=1
        x=int(input("Enter Member Id"))
        q1="select * from member where memberid={};".format(x)
        cursor.execute(q1)
        r=cursor.fetchone()
        if r:
            y=int(input("Enter Book Id"))
            q2="select bookid,rem_copies from book where bookid={};".format(y)
            cursor.execute(q2)
            r=cursor.fetchone()
            if r:
                if r[1]>0:
                    issuedate=input("Enter issue Date")
                    copies=int(input("Enter Number of copies"))
                    remcopies=r[1]-copies
                    q3="insert into issue values({},'{}',{},{},{});".format(issueid,issuedate,x,y,copies)
                    cursor.execute(q3)
                    q4="update book set rem_copies={} where bookid={};".format(remcopies,y)
                    cursor.execute(q4)
                    con.commit()
                    print("Book Issued Successfully")
                else:
                    print("No Copies Available")
            else:
                print("Book Doesn't Exist")
        else:
            print("Member Doesn't Exist")
    except:
        con.rollback()
def book_return():
    try:

        q="select max(returnid) from returns;"
        cursor.execute(q)
        r=cursor.fetchone()[0]
        if r:
            returnid=r+1
        else:
            returnid=1
        x=int(input("Enter member Id"))
        q1="select * from member  where memberid={};".format(x)
        cursor.execute(q1)
        r=cursor.fetchone()
        if r:
            y=int(input("Enter book Id"))
            q2="select bookid,rem_copies from book where bookid={};".format(y)
            cursor.execute(q2)
            r=cursor.fetchone()
            if r:
                returndate=input("Enter return Date")
                copies=int(input("Enter Number of copies"))
                remcopies=r[1]+copies
                q3="insert into returns values({},'{}',{},{},{});".format(returnid,returndate,x,y,copies)
                cursor.execute(q3)
                q4="update book set rem_copies={} where bookid={};".format(remcopies,y)
                cursor.execute(q4)
                con.commit()
                print("Book Returned Successfully")
            else:
                print("Book Doesn't Exist")
        else:
            print("Member Doesn't Exist")
    except:
        con.rollback()

