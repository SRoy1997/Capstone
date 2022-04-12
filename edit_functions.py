import sqlite3
import bcrypt

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


def update_user(user_id):
    user_update = ''
    update_values = ''
    update_menu = input("\nTo update a field, enter the name of the field.\nTo return to the main menu, press 'Enter'.\n>>> ")

    if update_menu == '':
        pass
    if update_menu == 'first name'.lower():
        update_values = input('Please enter the updated First Name:  ')
        user_update = "UPDATE Users SET first_name=? WHERE user_id=?"
        cursor.execute(user_update, (update_values, user_id))
    if update_menu == 'last name'.lower():
        update_values = input('Please enter the updated Last Name:  ')
        user_update = "UPDATE Users SET last_name=? WHERE user_id=?"
        cursor.execute(user_update, (update_values, user_id))
    if update_menu == 'email'.lower():
        update_values = input('Please enter the updated Email:  ')
        user_update = "UPDATE Users SET email=? WHERE user_id=?"
        cursor.execute(user_update, (update_values, user_id))
    if update_menu == 'phone'.lower():
        update_values = input('Please enter the updated Phone Number:  ')
        user_update = "UPDATE Users SET phone=? WHERE user_id=?"
        cursor.execute(user_update, (update_values, user_id))
    if update_menu == 'password'.lower():
        update_values = input('Please enter the updated Password:  ')
        user_update = "UPDATE Users SET password=? WHERE user_id=?"
        password_encoded = update_values.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password_encoded, salt)
        cursor.execute(user_update, (hashed, user_id))
    if update_menu == 'hire date'.lower():
        update_values = input('Please enter the updated Hire Date:  ')
        user_update = "UPDATE Users SET hire_date=? WHERE user_id=?;"
        cursor.execute(user_update, (update_values, user_id))
    if update_menu == 'user type'.lower():
        update_values = input('Manager (Yes or No):  ')
        user_update = "UPDATE Users SET user_type=? WHERE user_id=?"
        cursor.execute(user_update, (update_values, user_id))

    connection.commit()


def update_competency(name):
    competency_update = ''
    update_values = ''
    update_menu = input("\nTo update a field, enter the name of the field.\nTo return to the main menu, press 'Enter'.\n>>> ")

    if update_menu == '':
        pass
    elif update_menu == 'name'.lower():
        update_values = input('Please enter the updated Competency Name:  ')
        competency_update = "UPDATE Competencies SET name=? WHERE name=?"
        cursor.execute(competency_update, (update_values, name))
    else:
        print('Invalid entry')
        pass

    connection.commit()


def update_assessment(name):
    assessment_update = ''
    update_values = ''
    update_menu = input("\nTo update a field, enter the name of the field.\nTo return to the main menu, press 'Enter'.\n>>> ")

    if update_menu == '':
        pass
    if update_menu == 'name'.lower():
        update_values = input('Please enter the updated Assessment Name:  ')
        assessment_update = "UPDATE Assessments SET name=? WHERE name=?"
        cursor.execute(assessment_update, (update_values, name))
    if update_menu == 'competency'.lower():
        update_values = input('Please enter the updated Competency:  ')
        assessment_update = "UPDATE Assessments SET competency=? WHERE name=?"
        cursor.execute(assessment_update, (update_values, name))
    else:
        print('Invalid entry')
        pass

    connection.commit()


def update_results(user_id):
    results_update = ''
    update_values = ''
    update_menu = input("\nTo update a field, enter the name of the field.\nTo return to the main menu, press 'Enter'.\n>>> ")

    if update_menu == '':
        pass
    if update_menu == 'assessment'.lower():
        update_values = input('Please enter the updated Assessment Name:  ')
        results_update = "UPDATE Assessment_Results SET assessment=? WHERE user_id=?"
        cursor.execute(results_update, (update_values, user_id))
    if update_menu == 'score'.lower():
        update_values = input('Please enter the updated Score:  ')
        results_update = "UPDATE Assessment_Results SET score=? WHERE user_id=?"
        cursor.execute(results_update, (update_values, user_id))
    if update_menu == 'date taken'.lower():
        update_values = input('Please enter the updated Date the Assessment was Taken (YYYY-MM-DD):  ')
        results_update = "UPDATE Assessment_Results SET date_taken =? WHERE user_id=?"
        cursor.execute(results_update, (update_values, user_id))
    if update_menu == 'time taken'.lower():
        update_values = input('Please enter the updated Time the Assessment was Taken (YYYY-MM-DD):  ')
        results_update = "UPDATE Assessment_Results SET time_taken =? WHERE user_id=?"
        cursor.execute(results_update, (update_values, user_id))
    if update_menu == 'manager'.lower():
        update_values = input('Please enter the updated Manager ID:  ')
        results_update = "UPDATE Assessment_Results SET manager=? WHERE user_id=?"
        cursor.execute(results_update, (update_values, user_id))
    else:
        print('Invalid Entry')
        pass 

    connection.commit()