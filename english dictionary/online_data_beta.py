'''
program copied by the teacher of the course throught video

'''

import mysql.connector

# create con object
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# create cursor object
cursor = con.cursor()
word = input("enter the word: ")

query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = \"{word}\"")
# from the query we get a list of tuples
# were every tuple has the name (Expression) as [0] 
# and its meaning as [1]
results = cursor.fetchall()

for result in results:
    print(result[1])