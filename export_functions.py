import sqlite3
import csv

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


class Exports():
    def export_single_user(user_id):

        cursor.execute("SELECT U.user_id, U.first_name, U.last_name, U.email, U.phone, AR.assessment, AR.score, AR.date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id=AR.user_id JOIN Assessments A ON AR.assessment=A.name WHERE U.user_id=?", (user_id,))

        header = [row[0] for row in cursor.description]

        rows = cursor.fetchall()

        f = open('Competency_Assessment.csv', 'w')

        f.write(','.join(header) + '\n')

        for row in rows:
            f.write(','.join(str(r) for r in row) + '\n')
        
        print(str(len(rows)) + ' rows written successfully to ' + f.name)

    # export_single_user('Assessment_Results', 2)



    def export_competencies(competency):
        cursor.execute("SELECT U.user_id, U.first_name, U.last_name, A.competency, A.name, AR.score, AR.date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id = AR.user_id JOIN Assessments A ON AR.assessment = A.name WHERE A.competency LIKE ?", (competency,))

        header = [row[0] for row in cursor.description]

        rows = cursor.fetchall()

        f = open('Competency.csv', 'w')

        f.write(','.join(header) + '\n')

        for row in rows:
            f.write(','.join(str(r) for r in row) + '\n')
        
        print(str(len(rows)) + ' rows written successfully to ' + f.name)

    # export_competencies('Data Structures')
