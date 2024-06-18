"""This is a program that can be used to access data in my Languages database. Made by Jonty Uren for an Assessment in Computer Science, BHS 2024."""
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
    print("\033[33mLANGUAGE NAME          SPEAKERS      COUNTRIES THAT SPEAK IT     LANGUAGE FAMILY \033[0m")
    for result in results:
        # this variable is to add the "m" at the end of the second result
        speakers = str(result[2]) + "m"
        print(f"\033[34m{result[1] :<23}\033[36m{speakers:<14}\033[34m{result[3]:<28}\033[36m{result[4]:<11}\033[0m")
    # the following code is to make the printout stay on screen until you press enter
    while True:
        close_confirm = input("\033[30mpress enter to open the menu\033[0m")
        if close_confirm != 1:
            break
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
    print("\033[33mCOUNTRY NAME           LANGUAGE          POPULATION\033[0m")
    for result in results:
        print(f"\033[34m{result[0] :<23}\033[36m{result[1]:<18}\033[34m{result[2]}m\033[0m")
        # the following code is to make the printout stay on screen until you press enter
    while True:
        close_confirm = input("\033[30mpress enter to open the menu\033[0m")
        if close_confirm != 1:
            break
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
    print("\033[33mNATIONALITY            COUNTRY          MILLION PEOPLE\033[0m")
    for result in results:
        print(f"\033[34m{result[0] :<23}\033[36m{result[1]:<17}\033[34m{result[2]}m\033[0m")
    # the following code is to make the printout stay on screen until you press enter
    while True:
        close_confirm = input("\033[30mpress enter to open the menu\033[0m")
        if close_confirm != 1:
            break
    db.close()

# the main loop that recieves input and runs one of the programs depending on the input given by the user
print("\033[33m                 __              __   ___  ___     __        _____      ___      ___  ___")
print("\033[32m|      /| |\  | /    |   |   /| /    |___  \_     |  \    /|   |    /| |__/   /| \_  |___")
print("\033[33m|     /_| | \ | | __ |   |  /_| | __ |       \    |   |  /_|   |   /_| |  \  /_|   \ |   ")
print("\033[32m|___ /  | |  \| \__| \__/  /  | \__| |___  __/    |__/  /  |   |  /  | |__/ /  | __/ |___\033[0m")

print("\033[33mHOW TO USE:   Input one of the numbers to do specific actions")
while True:
    user_input = input("\n\033[33mWhat would you like to do?\033[34m\n1. print all languages in order of people who speak it\n\033[36m2. print all countries in the database\n\033[34m3. print all nationalities in order of people\n\033[36m4. close the program\n\033[0m")
    if user_input == "1":
        printlang()
    elif user_input == "2":
        printcountry()
    elif user_input == "3":
        printnationality()
    elif user_input == "4":
        # the following code is to make the program stay on screen until you press enter
        print("\033[30mprogram closing now...\033[0m")
        close_confirm = input("\033[30mpress enter to close the program\033[0m")
        if close_confirm != 1:
            break
    else:
        print("\033[31m\nPlease input a valid number\033[0m")