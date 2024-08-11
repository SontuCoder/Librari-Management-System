# Librari-Management-System
## Author: <b><i>Subhadip Maity</i></b>

## Project Overview

The Library Management System is a Python-based application that provides functionalities to manage a library, including student and admin login, book borrowing, returning, and other operations related to library management. The project uses a MySQL database to store and retrieve information about students, admins, and books.

## Features

### User Roles
- **Student:**
  - **Login/Signup:** Students can sign up or log in to their accounts.
  - **View Available Books:** Students can view the list of books available in the library.
  - **Borrow Books:** Students can borrow books, which updates the book's status in the library.
  - **Return Books:** Students can return borrowed books, which updates the book's status.
  - **Update Borrow Date:** Students can update the date they borrowed a book.

- **Admin:**
  - **Login/Signup:** Admins (Librarians) can sign up or log in to their accounts.
  - **View Borrowed Books:** Admins can view the list of all borrowed books along with the student details.
  - **Add New Books:** Admins can add new books to the library.
  - **View Existing Books:** Admins can view all books available in the library, including their borrow status.

### Password Management
- **Password Update:** Both students and admins can update their passwords after logging in.
- **Forgot Password:** Both students and admins can retrieve forgotten passwords by verifying their identity through personal details.

## Project Structure

- **Signup Class:**
  - Handles signup and login operations for both students and admins.
  - Includes methods for fetching student and admin credentials from the database.
  - Provides options for updating and retrieving passwords.

- **Login Class:**
  - Manages login operations for students and admins.
  - Provides an interface to handle different user options based on their roles.

- **Library Class:**
  - Handles all library-related operations accessible by the admin.
  - Manages the display of borrowed books, adding new books, and displaying existing books in the library.

- **Student Class:**
  - Handles operations accessible by the student.
  - Manages borrowing and returning books and updating the borrow date.

## Database Structure

- **Tables:**
  - **student:** Stores student information, including ID, password, name, and class.
  - **librarian:** Stores admin (librarian) information, including ID, password, and name.
  - **bookList:** Stores book information, including book ID, name, author, date added, and borrow status.
  - **student_borrow_book:** Stores the relationship between students and borrowed books, including the student ID, book ID, and borrow date.

## How to Run

1. **Install MySQL:** Ensure that MySQL is installed and running on your system.
2. **Database Setup:**
   - Create a database named `library`.
   - Create the necessary tables (`student`, `librarian`, `bookList`, `student_borrow_book`) based on the project structure.
3. **Python Setup:**
   - Install the necessary Python libraries using pip:
     ```bash
     pip install mysql-connector-python
     ```
4. **Run the Application:**
   - Execute the script by running the following command:
     ```bash
     python main.py
     ```
   - Follow the on-screen instructions to interact with the system.

## Sample Interaction

- **Main Menu:** 
  - Choose to log in or sign up as a student or admin.
  - Update or retrieve forgotten passwords.

- **Student Dashboard:** 
  - View available books, borrow or return books, and update borrow dates.

- **Admin Dashboard:**
  - View borrowed books, add new books to the library, or view existing books.

## Notes

- The system assumes that the MySQL server is running locally (`127.0.0.1`) and that the MySQL credentials (`user`, `password`) are set to `root` and `Sontu@123` respectively. You can change these settings according to your local MySQL configuration.

- The book IDs are generated randomly for new entries, and the borrow status is tracked to indicate whether a book is currently borrowed or not.


