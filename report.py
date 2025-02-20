import mysql.connector as sqlt
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con=sqlt.connect(host="localhost",user="root", passwd="manas1234", database="library")
cursor=con.cursor()
def book_output():
    try:

        df=pd.read_sql("select * from book",con)
        print(tabulate(df,headers='keys',tablefmt='psql' ,showindex=False))
    except:
        print("Error in fetching data")
def member_output():
    try:
        df=pd.read_sql("select * from member",con)
        print(tabulate(df,headers='keys',tablefmt='psql' ,showindex=False))
    except:
        print("Error in fetching data")
def return_output():
    try:
        df=pd.read_sql("select * from returns",con)
        print(tabulate(df,headers='keys',tablefmt='psql' ,showindex=False))
    except:
        print("Error in fetching data")
def issue_output():
    try:
        df=pd.read_sql("select * from issue",con)
        print(tabulate(df,headers='keys',tablefmt='psql' ,showindex=False))
    except:
        print("Error in fetching data")
def col_chart():
    try:
        q="select bookid,count(copies) as total from issue group by bookid;"
        df=pd.read_sql(q,con)
        plt.figure(figsize=(10,6))
        plt.bar(df.bookid,df.total)
        plt.xlabel('Book Id')
        plt.ylabel('Total Copies Issued')
        plt.title('Best Reading Book')
        plt.xticks(df.bookid)
        plt.show()
    except:
        print("Error in fetching data")