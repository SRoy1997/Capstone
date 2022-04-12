import sqlite3

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


def view_users():
    print('\n--- Users ---\n')
    print('ID  First Name           Last Name            Phone           Email')

    rows = cursor.execute("SELECT user_id, first_name, last_name, phone, email FROM Users").fetchall()

    for user in rows:
        user = [str(x) for x in user]
            
        print(f'{user[0]:<3} {user[1]:<20} {user[2]:20} {user[3]:15} {user[4]:30}')


def view_competencies(name):
    print('\n--- Users by Competency ---\n')
    print('ID  First Name           Last Name            Competency')

    rows = cursor.execute("SELECT U.user_id, U.first_name, U.last_name, C.name FROM Users U JOIN Assessment_Results AR ON U.user_id=AR.user_id JOIN Assessments A ON AR.assessment=A.name JOIN Competencies C ON A.competency=C.name WHERE C.name=?", (name,)).fetchall()

    for user in rows:
        user = [str(x) for x in user]
            
        print(f'{user[0]:<3} {user[1]:<20} {user[2]:20} {user[3]:30}')


def view_user_competencies(name):
    print('\n--- Competency Scores ---\n')
    print('ID  First Name           Last Name            Assessment                     Score')

    rows = cursor.execute("SELECT U.user_id, U.first_name, U.last_name, AR.assessment, AR.score FROM Users U JOIN Assessment_Results AR ON U.user_id=AR.user_id JOIN Assessments A ON AR.assessment=A.name JOIN Competencies C ON A.competency=C.name WHERE C.name=?", (name,)).fetchall()

    for user in rows:
        user = [str(x) for x in user]
            
        print(f'{user[0]:<3} {user[1]:<20} {user[2]:20} {user[3]:30} {user[4]:6}')


def view_user_assessment_scores(name):
    print('\n--- Assessment Scores ---\n')
    print('ID  First Name           Last Name            Assessment                     Score  Competency')

    query = "SELECT U.user_id, U.first_name, U.last_name, A.name, AR.score, A.competency FROM Users U JOIN Assessment_Results AR ON U.user_id=AR.user_id JOIN Assessments A ON AR.assessment=A.name WHERE A.name=?"
    rows = cursor.execute(query, (name,)).fetchall()

    for user in rows:
        user = [str(x) for x in user]
            
        print(f'{user[0]:<3} {user[1]:<20} {user[2]:20} {user[3]:30} {user[4]:6} {user[5]:30}')


def view_user_assessment(user_id):
    print('\n--- Assessment Scores ---\n')
    print('ID  First Name           Last Name            Assessment                     Score      Date Taken')

    rows = cursor.execute(f"SELECT U.user_id, U.first_name, U.last_name, AR.assessment, AR.score, AR.date_taken FROM Users U JOIN Assessment_Results AR ON U.user_id=AR.user_id WHERE U.user_id={user_id}").fetchall()

    for user in rows:
        user = [str(x) for x in user]
            
        print(f'{user[0]:<3} {user[1]:<20} {user[2]:20} {user[3]:30} {user[4]:10} {user[5]:15}')
