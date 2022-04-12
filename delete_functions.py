import sqlite3

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


def delete_result(assessment, date_taken):
    results = 'DELETE FROM Assessment_Results WHERE assessment=? AND date_taken=?'
    cursor.execute(results, (assessment, date_taken))