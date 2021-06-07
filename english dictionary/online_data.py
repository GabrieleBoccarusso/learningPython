'''

'''
# libraries
from mysql import connector


# create the con(nnector) with the database object
con = connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# create cursor object
cursor = con.cursor()

def fetch(word):
    statement = "SELECT * FROM Dictionary WHERE Expression = \"" + word + "\""
    query = cursor.execute(statement)
    return cursor.fetchall()

def main() -> int:
    loop: str = 'y'
    word: str = ''

    # entering the main loop
    while(loop[0] == 'y'):
        word = input("enter a word: ")

        results = fetch(word)
        if results == []:
            print("this word isn't in the dictionary") 
        else:
            for i,result in enumerate(results):
                print("definition", i+1, ":", result[1])
        
        # repeting the loop or exiting the program
        loop = input("do you want to enter another word? ")

    return 0
# end main

main()