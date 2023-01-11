#!/usr/bin/python3

# Les imports
from flask import Flask, render_template, request
import sqlite3
from pleine_lune_extractor_data import *
from calendar import monthrange, month_name
from data_index import *
# créer l'app avec le debugger
app = Flask(__name__, template_folder='templates')
app.debug = False

# créer le curseur de la DB
conn = sqlite3.connect('data/p2.sqlite', check_same_thread=False)
cursor = conn.cursor()


# les chemins du site
# acceuil
@app.route("/")
def index():
    # les data pour les graphiques
    voitures = car()
    velos = bike()
    camions = heavy()
    pietons = pedestrian()
    return render_template("index.html", voitures=voitures, velos=velos, camions=camions, pietons=pietons)

@app.route("/pleine_lune", methods=['POST', 'GET'])
def pleine_lune():
    # conditions si une date est donnée
    if request.method == "POST":
        month = request.form.get("month")
        year = request.form.get("year")
        type = request.form.get("type")
        date_passage = date_passages(int(month), int(year), int(type))
        keys = list(date_passage.keys())
        data = list(date_passage.values())
        data2 = list(passage_pleine_lune(int(type)).values())

        date = "{} {}".format(month_name[int(month)], str(year))
        for x in range(1, (monthrange(int(year), int(month))[1]) + 1):
            pos = position(datetime(int(year), int(month), x))
            phasename = phase(pos)

            if phasename == "Full Moon":
                lune = "La pleine lune à eu lieu le {}/{}/{}".format(str(x), str(month), str(year))
                return render_template("pleine_lune.html", keys=keys, data=data, data2=data2,
                                       lune=lune, date=date)

        lune = "Il n'y a pas eu de plein lune a cette date"
        return render_template("pleine_lune.html", keys=keys, data=data, data2=data2, lune=lune,
                               date=date)

    # le site sans données sur les graphes
    return render_template("pleine_lune.html", keys=[], data=[])

# lance le site
if __name__ == '__main__':
    app.run()
