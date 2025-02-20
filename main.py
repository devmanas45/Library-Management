import mysql.connector as sqlt
import book
import member
import transaction
import report
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt
con=sqlt.connect(host="localhost",user="root", passwd="manas1234", database="library")
cursor=con.cursor()
while(True):
    print("="*100)
    print("\t\t\t--------Library Management System----------\n")
    print("\t\t\t\tEnter Your Choice: \n\t\t\t\t 1.Book Details\n\t\t\t\t 2. Member Details\n\t\t\t\t 3.Transaction\n\t\t\t\t4. Report\n\t\t\t\t 5.Exit")
    choice = int(input())
    if choice == 1:
        while(True):
            print("Book Details: \n 1.Add Book Details\n 2.Edit Book Details\n 3.Delete Book\n 4.Search A Book\n 5. Back to Main Menu")
            ch=int(input())
            if ch==1:
               book.book_input()
            elif ch==2:
                book.book_edit()
            elif ch==3:
                book.book_delete()
            elif ch==4:
                book.book_search()
            elif ch==5:
                break
    elif choice==2:
        while(True):
            print("Member Details: \n 1.Add Member Details\n 2.Edit Member Details\n 3.Delete Member\n 4.Search A Member\n 5. Back to Main Menu")
            ch=int(input())
            if ch==1:
                member.member_input()
            elif ch==2:
                member.member_edit()
            elif ch==3:
                member.member_delete()
            elif ch==4:
                member.member_search()
            elif ch==5:
                break
    elif choice==3:
         while(True):
            print("Enter Your choice: \n 1.Issue A Book\n 2.Return Book\n 3. Back to Main Menu")
            ch=int(input())
            if ch==1:
                transaction.book_issue()
            elif ch==2:
                transaction.book_return()
            elif ch==3:
                print("Back to main menu")
                break              
    elif choice==4:
         while(True):
            print("Enter your choice: \n 1.Book Details\n 2. Member\n 3.Issue Details\n 4.Return Details\n 5. Best Reading Book(Chart)\n6. Back to Main Menu")
            ch=int(input())
            if ch==1:
                report.book_output()
            elif ch==2:
                report.member_output()
            elif ch==3:
                report.issue_output()
            elif ch==4:
                report.return_output()
            elif ch==5:
                report.col_chart()
            elif ch==6:
                break
    elif choice==5:
        print("Thank You For Using Our Library Management System")
        break