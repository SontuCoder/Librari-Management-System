# from dbm.ndbm import library
import random 
import mysql.connector as myConn
myDb = myConn.connect(host="127.0.0.1",user="root",password="Sontu@123",database="library")
db_cursor = myDb.cursor()

class Signup:

#fetch data for student
    def fetch_id_std(self,id):
        db_cursor.execute("SELECT std_id FROM student WHERE std_id = %s", (id,))
        return db_cursor.fetchone() is not None

    #function for fetch pass for id
    def fetch_pass_std(self, id):
        db_cursor.execute("select pass from student where std_id = %s", (id,))
        result = db_cursor.fetchone()
        if result:
            return result[0]
        return None
    
#fetch data for Admin
    def fetch_id_adm(self,id):
        db_cursor.execute("SELECT admin_id FROM librarian WHERE admin_id = %s", (id,))
        return db_cursor.fetchone() is not None

    #function for fetch pass for id
    def fetch_pass_adm(self, id):
        db_cursor.execute("select pass from librarian where admin_id = %s", (id,))
        result = db_cursor.fetchone()
        if result:
            return result[0]
        return None

    def login_signup_option(self):
        while(True):
            print("\n\n===========================")
            print("Enter (1) for Login as a Student:")
            print("Enter (2) for Signup as a Student:")
            print("Enter (3) for Login as an Admin:")
            print("Enter (4) for Signup as an Admin:")
            print("Enter (5) for Update password as a Student:")
            print("Enter (6) for Update password as an Admin:")
            print("Enter (7) for forgot password as a Student:")
            print("Enter (8) for forgot password as an Admin:")
            print("Enter (9) for Exit:--:")
            print("===========================\n")

            option = int(input("Enter: "))
            login_instance = Login()
            if option == 1:
                login_instance.login_student()
            elif option == 2:
                self.signup_student()
            elif option == 3:
                login_instance.login_admin()
            elif option == 4:
                self.signup_admin()
            elif option == 5:
                self.update_pass_student()
            elif option == 6:
                self.update_pass_admin()
            elif option == 7:
                login_instance.forgot_pass_student()
            elif option == 8:
                login_instance.forgot_pass_admin()
            elif option == 9:
                print("Exiting...")
                break
            else:
                print("Invalid option, please try again.")

    def signup_student(self):
        stu_id = input("\nEnter Student id: ")
        password= input("Enter PassWord: ")
        std_name=input("Enter name: ")
        std_class=input("Enter class:")
        if(self.fetch_id_std(stu_id)==1):
            print("\nStudent ID already exist in Data")
        else:
            insert_query = "insert into student(std_id,pass,std_name,class) values (%s,%s,%s,%s)"
            insert_value = (stu_id,password,std_name,std_class)
            db_cursor.execute(insert_query,insert_value)
            myDb.commit()
            print("\nData stored successfully.\n")
        
    def signup_admin(self):
        admin_id = input("\nEnter Admin id: ")
        password= input("Enter PassWord: ")
        admin_name=input("Enter name: ")
        if(self.fetch_id_adm(admin_id)==1):
            print("\nAdmin ID already exist in Data")
        else:
            insert_query = "insert into librarian(admin_id,pass,admin_name) values (%s,%s,%s)"
            insert_value = (admin_id,password,admin_name)
            db_cursor.execute(insert_query,insert_value)
            myDb.commit()
            print("\nData stored successfully.\n")
        
    def update_pass_student(self):
        signup_instance=Signup()
        print("\n\n===========================")
        stu_id=input("Enter Id:-")
        old_pass=input("Enter old Password:-")
        new_pass=input("Enter New Password:-")
        print("===========================\n")
        if(signup_instance.fetch_id_std(stu_id)==1):
            if(signup_instance.fetch_pass_std(stu_id)==old_pass):
                query = "UPDATE student SET pass = %s WHERE std_id = %s"
                db_cursor.execute(query, (new_pass, stu_id))
                myDb.commit()  
                print("Password Updated successfully.\n")
            else:
                print("Pass is Wrong\n")
                return
        else:
            print("Student ID is not found.\n")
            return
        
    def update_pass_admin(self):
        signup_instance=Signup()
        print("\n\n===========================")
        adm_id=input("Enter Id:-")
        old_pass=input("Enter old Password:-")
        new_pass=input("Enter New Password:-")
        print("===========================\n")
        if(signup_instance.fetch_id_adm(adm_id)==1):
            if(signup_instance.fetch_pass_adm(adm_id)==old_pass):
                query = "UPDATE librarian SET pass = %s WHERE admin_id = %s"
                db_cursor.execute(query, (new_pass, adm_id))
                myDb.commit()  
                print("Password Updated successfully.\n")
            else:
                print("Pass is Wrong\n")
        else:
            print("Admin ID is not found.\n")
        

class Login:
    signup_instance=Signup()
    def login_student(self,signup_instance):
        stu_id = input("Enter Student id: ")
        password= input("Enter PassWord: ")
        if(signup_instance.fetch_id_std(stu_id)==1):
            if(signup_instance.fetch_pass_std(stu_id)==password):
                print("ID and Pass is correct\n")
            else:
                print("Pass is Wrong\n")
        else:
            print("Student ID is not found.\n")
            print("sign up first.\n")
        
    def login_admin(self,signup_instance):
        library_instance=Library()
        admin_id = input("Enter Student id: ")
        password= input("Enter PassWord: ")
        if(signup_instance.fetch_id_adm(admin_id)==1):
            if(signup_instance.fetch_pass_adm(admin_id)==password):
                library_instance.admin_option()
            else:
                print("Pass is Wrong\n")
        else:
            print("Student ID is not found.\n")
            print("sign up first.\n")
        
    def forgot_pass_student(self):
        print("Forgot password as Student functionality here")
        
    def forgot_pass_admin(self):
        print("Forgot password as Admin functionality here")
        

class Library:
    def admin_option(self):
        while(True):
            print("\n\n===========================")
            print("Enter (1) for Display Borrowed Books and Name of Students:")
            print("Enter (2) for Add New Book in Library:")
            print("Enter (3) for Display Existing books in Library:")
            print("Enter (4) for Exit:--:")
            print("===========================\n")
            option=int(input("Enter:-"))
            if option == 1:
                self.display_borrowed_books()
            elif option == 2:
                self.add_book()
            elif option == 3:
                self.display_existing_books()
            elif option == 4:
                print("Exiting...")
                return
            else:
                print("Invalid option, please try again.")

    def book_id_generator(self):
        a=list("1234567890")
        c=[]
        for i in range(10):
            c.append(random.choice(a))
        b=''.join(c)
        db_cursor.execute("SELECT book_id FROM bookList WHERE book_id = %s", (b))
        if(db_cursor.fetchone()):
            self.book_id_generator()
        return ''.join(c)
    
    def display_borrowed_books(self):
        query = "SELECT student_borrow_book.student_id, student.std_name, student.class, student_borrow_book.book_id, bookList.book_name, student_borrow_book.borrow_date FROM student_borrow_book INNER JOIN student ON student_borrow_book.student_id = student.std_id INNER JOIN bookList ON student_borrow_book.book_id = bookList.book_id;"
        db_cursor.execute(query)
        borrowed_books = db_cursor.fetchall()
        print("\n\n===========================")
        print("The All books are:-\n")
        for record in borrowed_books:
            print(f"Student ID: {record[0]}, Name: {record[1]}, Class: {record[2]}, Book ID: {record[3]}, Book Name: {record[4]}, Borrow Date: {record[5]}")
        print("===========================\n")

    
    def add_book(self):
        print("\n\n===========================")
        name=input("Enter the name of book:- ")
        author=input("Enter the name of Author:- ")
        date=input("Enter the date of addition (in form dd/mm/yyyy):- ")
        print("===========================\n")
        a=self.book_id_generator()
        try:
            date_parts = date.split('/')
            formatted_date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
        except IndexError:
            print("Error: Incorrect date format. Please use dd/mm/yyyy.")
            return
        insert_query = "insert into bookList(book_id,book_name,book_author,add_date,borrow_status) values (%s,%s,%s,%s)"
        insert_value = (a,name,author,formatted_date,0)
        db_cursor.execute(insert_query,insert_value)
        myDb.commit()
        print("\n New book added to the Library successfully.\n")
    
    def display_existing_books(self):
        query="SELECT * FROM bookList"
        listOfBook = db_cursor.fetchall(query)
        for book in listOfBook:
            if(book[4]):
                print(f"{book[0]}-{book[1]}-By, {book[2]}, add on: {book[3]}, Borrow status- Yes")
            else:
                print(f"{book[0]}-{book[1]}-By, {book[2]}, add on: {book[3]}, Borrow status- No")

class Student:
    def student_option(self):
        while(True):
            print("\n\n===========================")
            print("Enter (1) for Display Books in Library:")
            print("Enter (2) for Borrow Book from Library:")
            print("Enter (3) for Return Book in Library:")
            print("Enter (4) for Update borrow date:")
            print("Enter (5) for Exit:--:")
            print("===========================\n")
            option=int(input("Enter:-"))
            if option == 1:
                self.display_non_borrowed_books()
            elif option == 2:
                self.borrow_book()
            elif option == 3:
                self.return_book()
            elif option == 4:
                self.update_borrow_date()
            elif option == 5:
                print("Exiting...")
                return
            else:
                print("Invalid option, please try again.")
    
    def display_non_borrowed_book(self):
        query = "SELECT * FROM bookList WHERE borrow_status=0;"
        db_cursor.execute(query)
        non_borrow_books = db_cursor.fetchall()
        print("\n\n===========================")
        print("The avalable books are:-\n")
        for record in non_borrow_books:
            print(f"Book ID: {record[0]}, Book Name: {record[1]}, Book Author: {record[2]}")
        print("===========================\n")
    
    def borrow_book(self):
        self.display_non_borrowed_book()
        stu_id=input("Enter Student Id:-")
        book_id=input("Enter Book Id:-")
        date=input("Enter the date of addition (in form dd/mm/yyyy):- ")
        print("===========================\n")
        try:
            date_parts = date.split('/')
            formatted_date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
        except IndexError:
            print("Error: Incorrect date format. Please use dd/mm/yyyy.")
            return
        insert_query = "insert into student_borrow_book (student_id,book_id,borrow_date) values (%s,%s,%s)"
        insert_value = (stu_id,book_id,formatted_date)
        db_cursor.execute(insert_query,insert_value)
        update_query="UPDATE bookList SET borrow_status = %s WHERE book_id = %s"
        db_cursor.execute(update_query,(1,book_id))
        myDb.commit()
        print("\n Book borrow from the Library successfully.\n")
    
    def return_book(self):
        print("\n\n===========================")
        stu_id=input("Enter Student Id:-")
        book_id=input("Enter Book Id:-")
        print("===========================\n")
        db_cursor.execute("SELECT student_id FROM student_borrow_book WHERE student_id = %s", (stu_id,))
        if(db_cursor.fetchone()):
            db_cursor.execute("SELECT book_id FROM student_borrow_book WHERE student_id = %s", (stu_id,))
            a=db_cursor.fetchall()
            if any(book_id == str(book[0]) for book in a):
                query="delete from student_borrow_book where student_id=%s and book_id= %s;"
                db_cursor(query,(stu_id,book_id))
                myDb.commit()
            else:
                print("Book id isn't matched.")
                return
        else:
            print("Student id isn't matched.")
            return


    def update_borrow_date(self):
        print("\n\n===========================")
        stu_id=input("Enter Student Id:-")
        book_id=input("Enter Book Id:-")
        date=input("Enter the date of addition (in form dd/mm/yyyy):- ")
        print("===========================\n")
        try:
            date_parts = date.split('/')
            formatted_date = f"{date_parts[2]}-{date_parts[1]}-{date_parts[0]}"
        except IndexError:
            print("Error: Incorrect date format. Please use dd/mm/yyyy.")
            return
        db_cursor.execute("SELECT student_id FROM student_borrow_book WHERE student_id = %s", (stu_id,))
        if(db_cursor.fetchone()):
            db_cursor.execute("SELECT book_id FROM student_borrow_book WHERE student_id = %s", (stu_id,))
            a=db_cursor.fetchall()
            if any(book_id == str(book[0]) for book in a):
                update_query="UPDATE student_borrow_book SET borrow_date = %s WHERE book_id = %s AND student_id=%s"
                db_cursor.execute(update_query,(formatted_date,book_id,stu_id))
                myDb.commit()
                print("\n Borrow date updated successfully.\n")
            else:
                print("Book id doesn't match.")
        else:
            print("Student id doesn't match.")



if __name__ == "__main__":
    signup_instance = Signup()
    signup_instance.login_signup_option()


