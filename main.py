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
            if option == 1:
                login_instance = Login()
                login_instance.login_student()
            elif option == 2:
                self.signup_student()
            elif option == 3:
                login_instance = Login()
                login_instance.login_admin()
            elif option == 4:
                self.signup_admin()
            elif option == 5:
                self.update_pass_student()
            elif option == 6:
                self.update_pass_admin()
            elif option == 7:
                login_instance = Login()
                login_instance.forgot_pass_student()
            elif option == 8:
                login_instance = Login()
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
        print("Update password as Student functionality here")
        
    def update_pass_admin(self):
        print("Update password as Admin functionality here")
        

class Login:

    def login_student(self):
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
        
    def login_admin(self):
        admin_id = input("Enter Student id: ")
        password= input("Enter PassWord: ")
        if(signup_instance.fetch_id_adm(admin_id)==1):
            if(signup_instance.fetch_pass_adm(admin_id)==password):
                print("ID and Pass is correct\n")
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
        pass
    
    def book_id_generator(self):
        pass
    
    def display_borrowed_books(self):
        pass
    
    def add_book(self):
        pass
    
    def display_existing_books(self):
        pass
    

class Student:
    def student_option(self):
        pass
    
    def display_non_borrowed_book(self):
        pass
    
    def borrow_book(self):
        pass
    
    def return_book(self):
        pass
    
    def update_borrow_date(self):
        pass


if __name__ == "__main__":
    signup_instance = Signup()
    signup_instance.login_signup_option()
    



