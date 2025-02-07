**Overview**

This Student Management System is a Python-based desktop application built using Tkinter and MySQL. It allows users to add, update, delete, search, and export student records efficiently. The application also provides a graphical user interface (GUI) for easy interaction.

**Features**

Add Student: Add new student records with details such as ID, Name, Phone, Email, Address, Gender, and Date of Birth.

Update Student: Modify student records.

Delete Student: Remove a student entry.

Search Student: Find student records based on multiple criteria.

Show All Students: Display all student records in a tabular format.

Export Data: Save student records as a CSV file.

Database Connectivity: Connect to a MySQL database to store student information.

GUI Interface: Uses Tkinter and TTK themes for an interactive experience.

Technologies Used

Python

Tkinter (GUI Development)

ttkthemes (Themed Widgets)

pymysql (Database Connectivity)

pandas (Data Exporting to CSV)

**Installation**

Prerequisites

Ensure you have Python 3.x installed on your system along with the following dependencies:

pip install pymysql pandas ttkthemes

Setting Up MySQL Database

Open MySQL Workbench or Command Line.

Run the following SQL commands to create the database and table:

CREATE DATABASE studentmanagementsystem;
USE studentmanagementsystem;
CREATE TABLE student (
    id INT NOT NULL PRIMARY KEY,
    name VARCHAR(30),
    mobile VARCHAR(10),
    email VARCHAR(30),
    address VARCHAR(100),
    gen VARCHAR(20),
    dob VARCHAR(20),
    date VARCHAR(50),
    time VARCHAR(50)
);

Running the Application

Clone this repository:

git clone https://github.com/yourusername/Student-Management-System.git
cd Student-Management-System

Run the main script:

python student_management.py

**Usage**

Click "Connect Database" and enter MySQL credentials.

Use the buttons on the left panel to Add, Search, Update, Delete, Show, or Export student data.

The data will be displayed in the right-side table.

Developed By: Aniket Sonawane
