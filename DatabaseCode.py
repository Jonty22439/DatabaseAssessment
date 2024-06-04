"""This is the code that I will use to access the database information. Made by Jonty Uren"""
# imports
import sqlite3

# variables
DATABASE = "Languages.db"

def printall():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    SQL = "SELECT * FROM Languages ORDER BY million_speakers ASC;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    # prints everything neatly
    for result in results:
        print(result)
    db.close()

while True:
    print("")
    user_input = input("What would you like to do?\n1. print all languages in order of people who speak it\n2. close the program")
    if user_input == "1":
        printall()
    elif user_input == "2":
        break
    else:
        print("Please input a number")