#Init db
import sqlite3
import csv
import sys
from datetime import datetime

print("DB Tables Init")

conn = sqlite3.connect('data/p2.sqlite')
cursor = conn.cursor()

try:
  cursor.execute("""CREATE TABLE IF NOT EXISTS segment_list(
    id               INT    NOT NULL,
    semgment_id      INT    NOT NULL
  );""")
  conn.commit()
  conn.close()
except:
  print("Error: Creating tables")
  sys.exit(1)


print("done")

print("DB Fill")
try:
  conn = sqlite3.connect('data/p2.sqlite')
  cursor = conn.cursor()
except:
  print("Error: Unable to connect to db")
with open("data/data.csv", 'r') as csvfile:
  csvreader = csv.reader(csvfile)
  next(csvreader)
  for row in csvreader:
    if int(row[1]) not in cursor.execute("SELECT semgment_id FROM segment_list"):
      id = int(row[1])
      cursor.execute("""CREATE TABLE IF NOT EXISTS test(
        date            STRING(100),
        interval        STRING(100),
        uptime          REAL,
        heavy           REAL,
        car             REAL,
        bike            REAL,
        pedestrian      REAL,
        heavy_lft       REAL,
        heavy_rgt       REAL,
        car_lft         REAL,
        car_rgt         REAL,
        bike_lft        REAL,
        bike_rgt        REAL,
        pedestrian_lft  REAL,
        pedestrian_rgt  REAL,
        direction       REAL

      );""".format(id))
      i = cursor.execute("SELECT MAX(id) FROM segment_list").fetchall()[0][0]
      if str(i) == "None":
        i = 0
      else:
        i = int(i) + 1
      cursor.execute("INSERT INTO segment_list VALUES({}, {})".format(i, int(row[1])))
    tmp =row[2].split('T')
    tmp2 = tmp[0] + " " + tmp[1].split('Z')[0].split('.')[0]
    date = datetime.strptime(tmp2, '%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO test VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (date,row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17]))

conn.commit()
conn.close()

print("done")