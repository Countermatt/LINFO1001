import sqlite3
from datetime import date, datetime
from math import floor
# créé le curseur et la connexion a la DB
conn = sqlite3.connect('data/p2.sqlite', check_same_thread=False)
cursor = conn.cursor()


def car():
    count = 0
    for x in cursor.execute("SELECT car FROM test"):
        count += x[0]
    return floor(count)


def bike():
    count = 0
    for x in cursor.execute("SELECT bike FROM test"):
        print(x)
        count += x[0]
    return floor(count)


def heavy():
    count = 0
    for x in cursor.execute("SELECT heavy FROM test"):
        count += x[0]
    return floor(count)


def pedestrian():
    count = 0
    for x in cursor.execute("SELECT pedestrian FROM test"):
        count += x[0]
    return floor(count)
