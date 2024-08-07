import mysql.connector as myConn

class Signup:
    def login_signup_option(self):
        print("Enter (1) for Login as a Student:")
        print("Enter (2) for Signup as a Student:")
        print("Enter (3) for Login as an Admin:")
        print("Enter (4) for Signup as an Admin:")
        print("Enter (5) for Update password as a Student:")
        print("Enter (6) for Update password as an Admin:")
        print("Enter (7) for forgot password as a Student:")
        print("Enter (8) for forgot password as an Admin:")
        print("Enter (9) for Exit:--:\n\n")
        
        option = int(input("Enter: "))
        
        # Placeholder for functionality
        while(True):
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
        print("Signup as Student functionality here")
        
    def signup_admin(self):
        print("Signup as Admin functionality here")
        
    def update_pass_student(self):
        print("Update password as Student functionality here")
        
    def update_pass_admin(self):
        print("Update password as Admin functionality here")
        

class Login:
    def login_student(self):
        print("Login as Student functionality here")
        
    def login_admin(self):
        print("Login as Admin functionality here")
        
    def forgot_pass_student(self):
        print("Forgot password as Student functionality here")
        
    def forgot_pass_admin(self):
        print("Forgot password as Admin functionality here")
        

# class Library:
#     def admin_login_option(self):
#         pass
    
#     def admin_option(self):
#         pass
    
#     def book_id_generator(self):
#         pass
    
#     def display_borrowed_books(self):
#         pass
    
#     def add_book(self):
#         pass
    
#     def display_existing_books(self):
#         pass
    

# class Student:
#     def student_login_option(self):
#         pass
    
#     def student_option(self):
#         pass
    
#     def display_non_borrowed_book(self):
#         pass
    
#     def borrow_book(self):
#         pass
    
#     def return_book(self):
#         pass
    
#     def update_borrow_date(self):
#         pass


if __name__ == "__main__":
    signup_instance = Signup()
    signup_instance.login_signup_option()
    

myDb = myConn.connect(host="127.0.0.1",user="root",password="Sontu@123",database="college")
db_cursor = myDb.cursor()

