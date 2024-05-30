"""This is the code that I will use to access the database information. Made by Jonty Uren"""
# imports
import sqlite3

# variables
DATABASE = "Languagess.db"

def printall():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    SQL = "SELECT * FROM Languages ORDER BY million_speakers ASC;"
    cursor.execute(SQL)
    results = cursor.fetchall()
    # prints everything neatly
    print("lsdkfjasldfjalsdkfjaksdflasdkfjlskfj")
    for fighter in results:
        print(f"{fighter[1] :<30}{fighter[2]:<8}")
    db.close()
printall()

# apparently there is no table "Languages" so I will need to do some trouble-shooting"