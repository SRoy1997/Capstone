import sqlite3
import csv 

connection = sqlite3.connect('Capstone_Database.db')

cursor = connection.cursor()

def import_csv():
  data_list = []

  with open('Capstone_CSV.csv', 'r') as csvfile:
    data = csv.reader(csvfile)
    header = next(data)

    query = "INSERT INTO Assessment_Results (user_id, assessment, score, date_taken, manager) VALUES(?, ?, ?, ?, ?)"
    
    if header != None:
      for row in data:
        data_list.append(row)
        
    cursor.executemany(query, data_list)
    
    connection.commit()

import_csv()
