import sqlite3

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


def search_users():
    search_term = input("Please enter a Last Name\n>>>")

    query = "SELECT user_id, first_name, last_name, phone, email FROM Users WHERE last_name LIKE ?"
    rows = cursor.execute(query, (f'%{search_term}%',)).fetchall()

    print('\n--- Users ---')
    print('ID  First Name           Last Name            Phone           Email')

    for user in rows:
        user = [str(x) for x in user]
            
        print(f'{user[0]:<3} {user[1]:<20} {user[2]:20} {user[3]:15} {user[4]:30}')