"""This is a program that can be used to access data in my Languages database. Made by Jonty Uren"""
# imports
import sqlite3

# variables
DATABASE = "Languages.db"

# funtions
# prints all languages in order of how many people speak it
def printlang():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # SQL query
    SQL = "SELECT * FROM Languages ORDER BY million_speakers DESC;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    # prints everything neatly
    print("\033[31mLANGUAGE NAME          SPEAKERS      COUNTRIES THAT SPEAK IT     LANGUAGE FAMILY \033[0m")
    for result in results:
        # this variable is to add the "m" at the end of the second result
        speakers = str(result[2]) + "m"
        print(f"{result[1] :<23}{speakers:<14}{result[3]:<28}{result[4]:<11}")
    db.close()

# prints all countries in order of population
def printcountry():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # SQL query
    SQL = "SELECT country_name, language_name, population_million FROM Countries INNER JOIN Languages ON Countries.language_id = Languages.language_id ORDER BY population_million DESC;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    # prints everything neatly 
    print("\033[31mCOUNTRY NAME           LANGUAGE          POPULATION\033[0m")
    for result in results:
        print(f"{result[0] :<23}{result[1]:<18}{result[2]}m")
    db.close()

# prints all nationalities in the database
def printnationality():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # SQL query
    SQL = "SELECT nationality_name, country_name, people_million FROM Nationalities INNER JOIN Countries ON Nationalities.country_id = Countries.country_id ORDER BY people_million DESC;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    # prints everything neatly 
    print("\033[31mNATIONALITY            COUNTRY          MILLION PEOPLE\033[0m")
    for result in results:
        print(f"{result[0] :<23}{result[1]:<17}{result[2]}m")
    db.close()

# the main loop that recieves input and runs one of the programs depending on the input given by the user
print("                 __              __   ___  ___     __        _____      ___      ___  ___")
print("|      /| |\  | /    |   |   /| /    |___  \_     |  \    /|   |    /| |__/   /| \_  |___")
print("|     /_| | \ | | __ |   |  /_| | __ |       \    |   |  /_|   |   /_| |  \  /_|   \ |   ")
print("|___ /  | |  \| \__| \__/  /  | \__| |___  __/    |__/  /  |   |  /  | |__/ /  | __/ |___")

print("HOW TO USE:\nInput one of the numbers to print data")
print("\033[31mRed text\033[0m")
while True:
    user_input = input("\n\033[31mWhat would you like to do?\033[0m\n1. print all languages in order of people who speak it\n2. print all countries in the database\n3. print all nationalities in order of people\n4. close the program\n")
    if user_input == "1":
        printlang()
    elif user_input == "2":
        printcountry()
    elif user_input == "3":
        printnationality()
    elif user_input == "4":
        break
    else:
        print("\nPlease input a valid number\n")