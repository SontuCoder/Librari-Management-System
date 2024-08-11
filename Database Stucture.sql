create database library;
use library;

create table bookList(
book_id bigint(10) primary key,
book_name varchar(100) not null,
book_author varchar(50) not null,
add_date date not null,
borrow_status boolean not null
);

create table student_borrow_book(
student_id int(5) not null,
book_id bigint(10) not null,
borrow_date date not null,
foreign key(book_id) references bookList(book_id) on delete cascade
on update cascade,
foreign key(student_id) references student(std_id)
on delete cascade
on update cascade
);

create table student(
std_id int(5) primary key,
pass char(10) not null,
std_name varchar(20) not null,
class int(2) not null
);

create table librarian(
admin_id int(5) primary key,
pass char(10) not null,
admin_name varchar(20) not null
);




