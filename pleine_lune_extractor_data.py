#!/usr/bin/python3

# Les imports
import decimal
import math
import sqlite3
from datetime import date, datetime
from calendar import monthrange
from math import floor
# créé le curseur et la connexion a la DB
conn = sqlite3.connect('data/p2.sqlite', check_same_thread=False)
cursor = conn.cursor()

# graphique 1
def date_passages(month=None, year=None, type=None):
    """
    :param month: le mois désiré
    :param year: l'année désiré
    :return: une dictionnaire avec le nombre de passage pour chaque jour du mois
    """
    if int(month) < 1 or int(month) > 12 or int(year) < 1990:
        raise ValueError("pas bonne date")
    d = {}
    for x in range(1, monthrange(year, month)[1] + 1):
        d[x] = 0

    for x in cursor.execute("SELECT * FROM test"):
        if int(x[0].split("-")[1]) == int(month) and int(x[0].split("-")[0]) == int(year):
            if type == 1:
                d[int(x[0].split("-")[2].split(" ")[0])] += floor(x[3]) + floor(x[4]) + floor(x[5]) + floor(x[6])
            else:
                d[int(x[0].split("-")[2].split(" ")[0])] += floor(x[type])

    return d


# graphique 2
def passage_pleine_lune(type=None):
    """
    :return: un dictionnaire avec le rapport de passages durant une pleine lune et hors d'une plaine lune
    """
    d = {"passages hors pleine lune": 0, 'passages à la pleine lune': 0}
    for x in cursor.execute("SELECT * FROM test"):
        pos = position(datetime(int(x[0].split("-")[0]), int(x[0].split("-")[1]), int(x[0].split("-")[2].split(" ")[0])))
        phasename = phase(pos)
        if phasename == "Full Moon":
            if type == 1:
                d["passages à la pleine lune"] += floor(x[3]) + floor(x[4]) + floor(x[5]) + floor(x[6])

            else:
                d["passages à la pleine lune"] += floor(x[type])
        else:
            if type == 1:
                d["passages hors pleine lune"] += floor(x[3]) + floor(x[4]) + floor(x[5]) + floor(x[6])
            else:
                d["passages hors pleine lune"] += floor(x[type])

    d["passages à la pleine lune"] = round((d["passages à la pleine lune"] /(d["passages à la pleine lune"]+d["passages hors pleine lune"])) * 100, 2)
    d["passages hors pleine lune"] = round((d["passages hors pleine lune"] /(d["passages à la pleine lune"]+d["passages hors pleine lune"])) * 100, 2)
    print(d["passages hors pleine lune"])
    print(d["passages à la pleine lune"])
    return d


dec = decimal.Decimal


# calcule la position de la lune en fonction de la date
def position(now=None):
    if now is None:
        now = datetime.now()

    diff = now - datetime(2001, 1, 1)
    days = dec(diff.days) + (dec(diff.seconds) / dec(86400))
    lunations = dec("0.20439731") + (days * dec("0.03386319269"))
    return lunations


# donne quelle type de lune il s'agit en fonction de ça position
def phase(pos):
    index = (pos * dec(8)) + dec("0.5")
    index = math.floor(index)
    return {
        0: "New Moon",
        1: "Waxing Crescent",
        2: "First Quarter",
        3: "Waxing Gibbous",
        4: "Full Moon",
        5: "Waning Gibbous",
        6: "Last Quarter",
        7: "Waning Crescent"
    }[int(index) & 7]
