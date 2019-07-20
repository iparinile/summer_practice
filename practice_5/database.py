import sqlite3

db = sqlite3.connect("Mydatabase.db")
cursor = db.cursor()

cursor.execute("""CREATE TABLE users (ID, Name) """)
db.commit()
