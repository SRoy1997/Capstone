import sqlite3
import bcrypt
from activate_functions import activate_user
from add_functions import add_user, add_assessments, add_assessment_reuslts, add_competency
from deactivate_functions import deactivate_user
from delete_functions import delete_result
from details_functions import user_details, comptency_details, assessment_details
from edit_functions import update_assessment, update_competency, update_results, update_user
from export_functions import Exports
from import_functions import import_csv
from login import login, is_manager
from search_functions import search_users
from view_functions import view_competencies, view_user_assessment, view_user_assessment_scores, view_user_competencies, view_users


connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()


print('----- Competency Assessment Database -----')

while True:
    main_menu = input('\nPlease choose from the following options\n\n[1] Login\n[2] Create Account\n[3] Quit\n\n>>>')
    if main_menu == '1':
        login()
        user_type = is_manager()
        while user_type == '1':
            menu = input('\nPlease select from the following options:\n[1] Users\n[2] Competencies\n[3] Assessments\n[4] Assessment Results\n[5] Reports\n[6] Logout\n\n>>>')
            while menu == '1':
                user_menu = input('\nPlease select from the following options:\n[1] View a User\n[2] Search Users\n[3] Add a User\n[4] Deactivat a User\n[5] Activate a User\n[6] Quit\n\n>>>')
                if user_menu == '1':
                    view_users()
                    user_id = input('\nPlease enter a User ID:  ')
                    user_details(user_id)
                    edit = input('\nWould you like to edit the User? Y or N:  ')
                    if edit == 'Y':
                        update_user(user_id)
                        print('\nUser has been Updated')
                    if edit == 'N':
                        pass     
                if user_menu == '2':
                    search_users()
                    user_id = input('\nPlease enter a User ID:  ')
                    user_details(user_id)
                    edit = input('\nWould you like to edit the User? Y or N:  ')
                    if edit == 'Y':
                        update_user(user_id)
                        print('\nUser has been Updated')
                    if edit == 'N':
                        pass
                if user_menu == '3':
                    add_user()
                    print('\nUser has been Added')
                if user_menu == '4':
                    user_id = input('\nPlease enter a User ID:  ')
                    deactivate_user(user_id)
                    print('\nUser has been Deactivated')
                if user_menu == '5':
                    user_id = input('\nPlease enter a User ID:  ')
                    activate_user(user_id)
                    print('\nUser has been Activated')
                if user_menu == '6':
                    break
            while menu == '2':
                user_menu = input('\nPlease select from the following options:\n[1] View Competencies\n[2] Add a Competency\n[3] Quit\n\n>>>')
                if user_menu == '1':
                    name = input('\nPlease enter a Competency:  ')
                    view_competencies(name)
                    edit = input('\nWould you like to edit the Competency? Y or N:  ')
                    if edit == 'Y':
                        comptency_details(name)
                        update_competency(name)
                        print('\nCompetency has been Updated')
                    if edit == 'N':
                        pass
                if user_menu == '2':
                    add_competency()
                    print('\nCompetency has been Added')
                if user_menu == '3':
                    break
            while menu == '3':
                user_menu = input('\nPlease select from the following options:\n[1] View Assessments\n[2] Add an Assessment\n[3] Quit\n\n>>>')
                if user_menu == '1':
                    name = input('\nPlease enter an Assessment:  ')
                    assessment_details(name)
                    edit = input('\nWould you like to edit the Assessment? Y or N:  ')
                    if edit == 'Y':
                        update_assessment(name)
                        print('\nAssessment has been Updated')
                    if edit == 'N':
                        pass
                if user_menu == '2':
                    add_assessments()
                    print('\nAssessment has been Added')
                if user_menu == '3':
                    break
            while menu == '4':
                user_menu = input('\nPlease select from the following options:\n[1] View Assessment Results\n[2] Add an Assessment Result\n[3] Edit Results\n[4] Delete Results by User\n[5] Quit\n\n>>>')
                while user_menu == '1':
                    assessment_menu = input('\nPlease select one of the following: \n[1] Results by Competency\n[2] Results by Assessment\n[3] Results by User\n[4] Quit\n\n>>>')
                    if assessment_menu == '1':
                        name = input('\nPlease enter a Competency:  ')
                        view_user_competencies(name)
                    if assessment_menu == '2':
                        name = input('\nPlease enter an Assessment:  ')
                        view_user_assessment_scores(name)
                    if assessment_menu == '3':
                        user_id = input('\nPlease enter a User ID:  ')
                        view_user_assessment(user_id)
                    if assessment_menu == '4':
                        break
                if user_menu == '2':
                    add_assessment_reuslts()
                    print('\nResult has been Added')
                if user_menu == '3':
                    user_id = input('\nPlease enter a User ID:  ')
                    view_user_assessment(user_id)
                    update_results(user_id)
                    print('\nResult has been Updated')
                if user_menu == '4':
                    user_id = input('\nPlease enter a User ID:  ')
                    view_user_assessment(user_id)
                    assessment = input('\nPlease enter an Assessment Name:  ')
                    date_taken = input('\nPlease enter the Date the Assessment was Taken (YYYY-MM-DD):  ')
                    delete_result(assessment, date_taken)
                if user_menu == '5':
                    break
            while menu == '5':
                report_menu = input('\nPlease choose from the following options:\n[1] Import Reports\n[2] Export Reports\n[3] Quit\n\n>>>')
                if report_menu == '1':
                    import_csv()
                    print('\nReport has been imported')
                while report_menu == '2':
                    export_menu = input('\nPlease choose from the following options:\n[1] Assessment Results by User\n[2] Assessment Results by Competency\n[3] Quit\n\n>>>')
                    if export_menu == '1':
                        user_id = input('Please enter a User ID:  ')
                        Exports.export_single_user(user_id)
                    if export_menu == '2':
                        competency = input('\nPlease enter a Competency:  ')
                        Exports.export_competencies(competency)
                    if export_menu == '3':
                        break
                if report_menu == '3':
                    break
            if menu == '6':
                print('\nGoodbye!')
                break
        while user_type == '0':
            menu = input('\nPlease select from the following options:\n[1] View Information\n[2] Edit Information\n[3] View Assessment Results\n[4] Logout\n\n>>>')
            if menu == '1':
                user_id = input('\nPlease enter your User ID:  ')
                user_details(user_id)
            if menu == '2':
                user_id = input('\nPlease enter your User ID:  ')
                user_details(user_id)
                update_user(user_id)
            if menu == '3':
                user_id = input('\nPlease enter your User ID:  ')
                view_user_assessment(user_id)
            if menu == '4':
                print('\nGoodbye!')
                break
    if main_menu == '2':
        add_user()
        print('User has been added')
    if main_menu == '3':
        break
            
