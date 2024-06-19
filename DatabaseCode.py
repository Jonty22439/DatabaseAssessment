"""This is a program that can be used to access data in my Languages database. Made by Jonty Uren for an Assessment in Computer Science, BHS 2024."""
# imports
import sqlite3

# variables
DATABASE = "Languages.db"
YELLOW = "\033[33m"
GREEN = "\033[32m"
BLUE = "\033[34m"
CYAN = "\033[36m"
GREY = "\033[30m"
RED = "\033[31m"
WHITE = "\033[0m"
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
    print(f"{YELLOW}LANGUAGE NAME          SPEAKERS      COUNTRIES THAT SPEAK IT     LANGUAGE FAMILY {WHITE}")
    for result in results:
        # this variable is to add the "m" at the end of the second result
        speakers = str(result[2]) + "m"
        print(f"{BLUE}{result[1] :<23}{CYAN}{speakers:<14}{BLUE}{result[3]:<28}{CYAN}{result[4]:<11}{WHITE}")
    # the following code is to make the printout stay on screen until you press enter
    while True:
        close_confirm = input(f"\n{GREY}press enter to open the menu{WHITE}")
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
    print(f"{YELLOW}COUNTRY NAME           LANGUAGE          POPULATION{WHITE}")
    for result in results:
        print(f"{BLUE}{result[0] :<23}{CYAN}{result[1]:<18}{BLUE}{result[2]}m{WHITE}")
        # the following code is to make the printout stay on screen until you press enter
    while True:
        close_confirm = input(f"\n{GREY}press enter to open the menu{WHITE}")
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
    print(f"{YELLOW}NATIONALITY            COUNTRY          MILLION PEOPLE{WHITE}")
    for result in results:
        print(f"{BLUE}{result[0] :<23}{CYAN}{result[1]:<17}{BLUE}{result[2]}m{WHITE}")
    # the following code is to make the printout stay on screen until you press enter
    while True:
        close_confirm = input(f"\n{GREY}press enter to open the menu{WHITE}")
        if close_confirm != 1:
            break
    db.close()

# signing in process
while True:
    colour = input("Would you like to have colour enabled? (y/n)")
    colour = colour.lower()
    if colour == "y" or "n":
        break
    else:
        print("ERROR: please only input 'y' or 'n'")
if colour == "y":
    print(f"{YELLOW}Colour has been turned on!")
else:
    print("Colour has been turned off")
    YELLOW = ""
    GREEN = ""
    BLUE = ""
    CYAN = ""
    GREY = ""
    RED = ""
    WHITE = ""
# the main loop that recieves input and runs one of the programs depending on the input given by the user
print(f"{YELLOW}                 __              __   ___  ___     __        _____      ___      ___  ___")
print(f"{GREEN}|      /| |\  | /    |   |   /| /    |___  \_     |  \    /|   |    /| |__/   /| \_  |___")
print(f"{YELLOW}|     /_| | \ | | __ |   |  /_| | __ |       \    |   |  /_|   |   /_| |  \  /_|   \ |   ")
print(f"{GREEN}|___ /  | |  \| \__| \__/  /  | \__| |___  __/    |__/  /  |   |  /  | |__/ /  | __/ |___{WHITE}")

print(f"{YELLOW}HOW TO USE:   Input one of the numbers to do specific actions")
while True:
    user_input = input(f"\n{YELLOW}What would you like to do?{BLUE}\n1. print all languages in order of people who speak it\n{CYAN}2. print all countries in the database\n{BLUE}3. print all nationalities in order of people\n{CYAN}4. close the program\n{WHITE}")
    if user_input == "1":
        printlang()
    elif user_input == "2":
        printcountry()
    elif user_input == "3":
        printnationality()
    elif user_input == "4":
        # the following code is to make the program stay on screen until you press enter
        print(f"{GREY}program closing now...{WHITE}")
        close_confirm = input(f"{GREY}press enter to close the program{WHITE}")
        if close_confirm != 1:
            break
    else:
        print(f"{RED}\nPlease input a valid number{WHITE}")