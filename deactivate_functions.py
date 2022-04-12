import sqlite3

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


def deactivate_user(user_id):
    user_update = 'UPDATE Users SET active=0 WHERE user_id=?'
    cursor.execute(user_update, (user_id,))
    connection.commit()