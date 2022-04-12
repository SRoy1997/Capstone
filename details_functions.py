import sqlite3

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


def user_details(user_id):
    query = "SELECT user_id, first_name, last_name, phone, email, password, date_created, hire_date, user_type, active FROM Users WHERE user_id=?"
    details = cursor.execute(query, [user_id]).fetchone()
    ('\n--- Details ---\n')
    print(f"ID:                    {details[0]}")
    print(f"First Name:            {details[1]}")
    print(f"Last Name:             {details[2]}")
    print(f"Phone:                 {details[3]}")
    print(f"Email:                 {details[4]}")
    print(f"Password:              {details[5]}")
    print(f"Date Created:          {details[6]}")
    print(f"Date Hired:            {details[7]}")
    print(f"User Type:             {details[8]}")
    print(f"Active User (1=Y 0=N): {details[9]}")


def comptency_details(name):
    query = "SELECT name, date_created FROM Competencies WHERE name=?"
    details = cursor.execute(query, [name]).fetchone()
    ('\n--- Details ---\n')
    print(f"Name:         {details[0]}")
    print(f"Date Created: {details[1]}")


def assessment_details(name):
    query = "SELECT name, competency, date_created FROM Assessments WHERE name=?"
    details = cursor.execute(query, [name]).fetchone()
    ('\n--- Details ---\n')
    print(f"Name:         {details[0]}")
    print(f"Competency:   {details[1]}")
    print(f"Date Created: {details[2]}")