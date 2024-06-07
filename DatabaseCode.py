"""This is a program that can be used to access data in my Languages database. Made by Jonty Uren"""
# imports
import sqlite3

# variables
DATABASE = "Languages.db"

# Prints all languages in order of how many people speak it
def printlang():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    SQL = "SELECT * FROM Languages ORDER BY million_speakers DESC;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    # prints everything neatly
    print("LANGUAGE NAME          SPEAKERS      COUNTRIES THAT SPEAK IT     LANGUAGE FAMILY ")
    for result in results:
        print(f"{result[1] :<23}{result[2]:<14}{result[3]:<28}{result[4]:<11}")
    db.close()

# Prints all countries in order of population
def printcountry():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    SQL = "SELECT * FROM Countries ORDER BY population_million DESC;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    # prints everything neatly 
    print("COUNTRY NAME           LANGUAGE      POPULATION")
    for result in results:
        print(f"{result[1] :<23}{result[2]:<14}{result[3]:<28}")
    db.close()

# The main loop that recieves input and runs one of the programs depending on input
while True:
    print("                 __              __   ___  ___     __        _____      ___      ___  ___   ")
    print("|      /| |\  | /    |   |   /| /    |___  \_     |  \    /|   |    /| |__/   /| \_  |___   ")
    print("|     /_| | \ | | __ |   |  /_| | __ |       \    |   |  /_|   |   /_| |  \  /_|   \ |      ")
    print("|___ /  | |  \| \__| \__/  /  | \__| |___  __/    |__/  /  |   |  /  | |__/ /  | __/ |___   ")
    user_input = input("What would you like to do?\n1. print all languages in order of people who speak it\n2. print all countries in the database \n3. close the program\n")
    if user_input == "1":
        printlang()
    elif user_input == "2":
        printcountry()
    elif user_input == "3":
        break
    else:
        print("\nPlease input a valid number")