import sqlite3

db = sqlite3.connect('Users.sqlite')
cursor = db.cursor()

cursor.execute("""CREATE TABLE Users(
                    ID INTEGER PRIMARY KEY,
                    State INTEGER
                    )""")
db.commit()