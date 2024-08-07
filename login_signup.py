import mysql.connector as myConn
myDb = myConn.connect(host="127.0.0.1",user="root",password="Sontu@123",database="college")
db_cursor = myDb.cursor()

#function for fetch student_id 
def fetch_id(id):
    db_cursor.execute("select student_id from login_signup")
    ids=[]
    for id_data in db_cursor.fetchall():
        ids.append(id_data[0])
    if id in ids:
        return 1
    return 0

#function for fetch pass for id
def fetch_pass(id):
    db_cursor.execute("select * from login_signup")
    for id_data in db_cursor.fetchall():
        if(id_data[0]==id):
            return id_data[1]

#function for log in...
def login():
    stu_id = input("Enter Student id: ")
    password= input("Enter PassWord: ")
    if(fetch_id(stu_id)==1):
        if(fetch_pass(stu_id)==password):
            print("ID and Pass is correct\n")
        else:
            print("Pass is Wrong\n")
    else:
        print("Student ID is not found.\n")
        print("sign up first.\n")

#function for signup...
def signup():
    stu_id = input("Enter Student id: ")
    password= input("Enter PassWord: ")
    if(fetch_id(stu_id)==1):
        print("Student ID already exist in Data")
    else:
        insert_query = "insert into login_signup(student_id,pass) values (%s,%s)"
        insert_value = (stu_id,password)
        db_cursor.execute(insert_query,insert_value)
        myDb.commit()
        print("Data stored successfully.\n")

def option():
    print("Choose any one:")
    print("Enter (1) for Log in :")
    print("Enter (2) for Sign up: ")
    print("Enter (3) for Exit: ")

option()
opp=int(input(":-"))
while(opp!=3):
    if(opp==1):
        login()
    elif(opp==2):
        signup()
    else:
        print("Enter correct opption\n")
    option()
    opp=int(input(":-"))
if(opp==3):
    print("Thank You..")
