import sqlite3
import csv

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE statistics 
                  (reg_code,reg_name,road_code,road_name,road_type,oktmo,address,crash_type_name,
                  crash_date,crash_time,crash_reason,fatalities_amount,victims_amount,vehicles_amount,
                  participants_amount,latitude,longitude)
               """)

file = "data-20190220T1309-structure-20180314T1826.csv"
data = []
with open(file, "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        a = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
             row[11], row[12], row[13], row[14], row[15], row[16])
        data.append(a)

cursor.executemany("INSERT INTO statistics VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
conn.commit()

cursor.execute('select * from statistics order by reg_code')  # В качестве примера отсортируем по коду региона
for row in cursor:
    print(row)


