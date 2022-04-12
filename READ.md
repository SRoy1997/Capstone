Users Types:

Managers:
Sarah Roy - user_name = sarah@devpipeline.com - password = Manager - user_id = 1
Ryan Curtis - user_name = ryancurtis@devpipeline.com - password = Manager - user_id = 7
Jason Fletcher - user_name = jason@devpipeline.com - password = Manager - user_id = 13
Shayne Roy - user_name = shayne@devpipeline.com - password = Manager - user_id = 29

Users:
Bugs Bunny - user_name = Bugs@gmail.com - password = 1234 - user_id = 5
Daffy Duck - user_name = Daffy@gmail.com - password = 1234 - user_id = 6
Pepe Le Pew - user_name = Pepe@gmail.com - password = 1234 - user_id = 22
Wile E. Coyote Bunny - user_name = Wile@gmail.com - password = 1234 - user_id = 25
Road Runner - user_name = Road@gmail.com - password = 1234 - user_id = 24
Marvin The Martian - user_name = MArvin@gmail.com - password = 1234 - user_id = 23

Assessment Names
For Loops
While Loops
CSV Files
.join()
.split()
Debugging
Computer Parts
Variable Types

Competency Names
Data Types
Functions
Loops
Boolean Logic
Conditionals
Lists
Working with Files
Quality Assurance (QA)
Databases
Variables


1st Menu:
You have three options - Login, Create User, Quit
To login you need to enter a user_name and a password - provided above for different users
To create a new user, you will just need to enter the information according to the prompts

If you are a manager:

2nd Menu:
You have 5 options - Users, Competencies, Assessments, Assessment Results, Reports

Users - You can view, search, edit, deactivate, reactivate - You will need user ID's to do anything that has to do with changing something in the database for the user
Competencies - You can view or add a competency - You will need competency names (provided above)
Assessments - You can view or add an assessment - You will need assessment names (provided above)
Assessment Results - You can view, add, edit, or delete results by user
    View Results - You can view by competency, assessment, or user - you will need competency name, assessment name, or user_id
    Add Results - You will need to provide user_id, assessment name, score, the date_taken, and the administrating manager ID 
    Edit Results - You will need to provide a user_id and then follow the prompts
    Delete Results - You will need to provide a user_id, assessment name, and date_taken
Reports - Importing and Exporting
    Importing - It will import the provided CSV file Capstone_CSV into the Assessment_Results table of the Capstone_Database
    Exporting - You can export by a single user or by a competency
        Single User - It will export to a CSV the following information: user_id, first_name, last_name, email, phone, assessment, score, date_taken
        Competency - It will export to a CSV the following information: user_id, first_name, last_name, competency, assessment name, score, date_taken

If you are a User:

2nd Menu:
You have 3 options - View Information, Edit Information, View Assessment Results

View Information - Will provide your user details - will need to provide the user_id
Edit Information - Will need to provide the user_id and then will display the user details and will give you prompts to edit the information
View Assessment Results - Will need to provide the user_id and then will display the assessments that the individual has taken.