# Library Management System

<img src="./public/logo.jpg" width="50px" />

## Author: *Subhadip Maity*

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Project Screenshots](#project-screenshots)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Database Structure](#database-structure)
- [How to Run](#how-to-run)
- [Notes](#notes)
- [Contact](#contact)

---

## Overview
The Library Management System is a Python-based application that provides functionalities to manage a library, including student and admin login, book borrowing, returning, and other operations related to library management. The project uses a MySQL database to store and retrieve information about students, admins, and books.

---

## Features

### User Roles
- **Student**:
  - **Login/Signup**: Students can sign up or log in to their accounts.
  - **View Available Books**: Students can view the list of books available in the library.
  - **Borrow Books**: Students can borrow books, updating the book's status in the library.
  - **Return Books**: Students can return borrowed books, updating the book's status.
  - **Update Borrow Date**: Students can update the date they borrowed a book.

- **Admin**:
  - **Login/Signup**: Admins (Librarians) can sign up or log in to their accounts.
  - **View Borrowed Books**: Admins can view all borrowed books along with student details.
  - **Add New Books**: Admins can add new books to the library.
  - **View Existing Books**: Admins can view all books available in the library, including their borrow status.

### Password Management
- **Password Update**: Both students and admins can update their passwords after logging in.
- **Forgot Password**: Students and admins can retrieve forgotten passwords by verifying their identity.

---

## Project Screenshots
- **Main Menu**  
  <img src="./public/Screenshot 2025-01-12 150343.png" width="500px" />

- **Student Menu**  
  <img src="./public/Screenshot 2025-01-12 150809.png" width="500px" />

- **Book List**  
  <img src="./public/Screenshot 2025-01-12 150825.png" width="500px" />

---

## Technologies
- 1. Python;
- 2. MySQL;

---

## Project Structure
- **Signup Class**: Handles signup and login operations for both students and admins, including password management.
- **Login Class**: Manages login operations and provides user options based on roles.
- **Library Class**: Manages library operations accessible by the admin, including viewing borrowed books and adding new books.
- **Student Class**: Handles student operations such as borrowing, returning books, and updating borrow dates.

---

## Database Structure
- **Tables**:
  - **student**: Stores student information (ID, password, name, class).
  - **librarian**: Stores admin (librarian) information (ID, password, name).
  - **bookList**: Stores book details (book ID, name, author, date added, borrow status).
  - **student_borrow_book**: Tracks borrowed books (student ID, book ID, borrow date).

---

## How to Run

1. **Install MySQL**: Ensure MySQL is installed and running.
2. **Database Setup**:
   - Create a database named `library`.
   - Create necessary tables as per the project structure.
3. **Python Setup**:
   ```bash
   pip install mysql-connector-python

---

## Notes

- The system assumes that the MySQL server is running locally (`127.0.0.1`) and that the MySQL credentials (`user`, `password`) are set to `user_root` and `pass_word` respectively. You can change these settings according to your local MySQL configuration.

- The book IDs are generated randomly for new entries, and the borrow status is tracked to indicate whether a book is currently borrowed or not.

---

## Contact
- Email: [subhadipmaity211@gmail.com](mailto:subhadipmaity211@gmail.com)
- GitHub: [SontuCoder](https://github.com/SontuCoder)
