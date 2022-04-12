import sqlite3
import bcrypt

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


def add_user():
    first_name = input('Please enter a first name: ')
    last_name = input('Please enter a last name: ')
    email = input('Please enter a email: ')
    phone = input('Please enter a phone: ')
    password = input('Please enter a password: ')
    password_encoded = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_encoded, salt)
    password = hashed
    user_type = input('Manager or User: ')
    date_created = input("Please enter today's date (YYYY-MM-DD):  ")
    hire_date = input('Please enter a hire date:  ')

    query = "INSERT INTO Users (first_name, last_name, email, phone, password, date_created, hire_date, user_type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    values = [first_name, last_name, email, phone, password, date_created, hire_date, user_type]
    cursor.execute(query, values)

    connection.commit()


def add_competency():
    name = input('Please enter the Competency Name:  ')
    date_created = input("Please enter today's date (YYYY-MM-DD):  ")
    
    query = "INSERT INTO Competencies (name, date_created) VALUES (?, ?)"
    values = [name, date_created]
    cursor.execute(query, values)

    connection.commit()


def add_assessments():
    name = input('Please enter the Assessment Name:  ')
    competency = input('Please enter the Competency related to this Assessment:  ')
    date_created = input("Please enter today's date (YYYY-MM-DD):  ")
    
    query = "INSERT INTO Assessments (name, competency, date_created) VALUES (?, ?, ?)"
    values = [name, competency, date_created]
    cursor.execute(query, values)

    connection.commit()


def add_assessment_reuslts():
    user_id = input('Please enter the User ID:  ')
    assessment = input('Please enter the Assessment Name:  ')
    score = input('Please enter a Score between 0 and 4:  ')
    date_taken = input('Please enter the Date the Assessment was taken (YYYY-MM-DD):  ')
    manager = input("Please enter the Administrating Manager's ID:  ")
    
    query = "INSERT INTO Assessment_Results (user_id, assessment, score, date_taken, manager) VALUES (?, ?, ?, ?, ?)"
    values = [user_id, assessment, score, date_taken, manager]
    cursor.execute(query, values)

    connection.commit()