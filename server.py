# -*- encoding: utf-8 -*-
"""
Server Web d'exemple écrit en Python avec Flask.
"""
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# S'assure de pouvoir démarrer le serveur depuis n'importe quel dossier.
from flask import abort,request, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_mako import render_template,MakoTemplates
from flask_sqlite import SQLiteExtension
from flask_sqlite import get_db
import sqlite3
from random import randint
from flask import Flask ,session # Importe le type Flask.
app = Flask("Akiplanta")  # Crée une application Flask nommée "SuperSite".
MakoTemplates(app)
SQLiteExtension(app)
class ValidationError(ValueError):
    """Error in users provided values."""
    pass


    
@app.route("/")
def index():
    return redirect(url_for("accueil"), code=303)

@app.route("/accueil")
def accueil():
    return render_template("accueil.html.mako")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html.mako")
@app.route("/ajoutprof")
def ajoutprof():
    return render_template('ajoutprof.html.mako')
@app.route("/leaderboardeleve")
def leaderboardeleve():
    return render_template('leaderboardeleve.html.mako')

@app.route("/login")
def login():
    return render_template('login.html.mako')

@app.route("/jeu")
def jeu():
    return render_template('jeu.html.mako')
@app.route("/leaderboardpro")
def leaderboardpro():
    return render_template('leaderboardpro.html.mako')
@app.route("/signin")
def signin():
    return render_template('signin.html.mako')
7.03






































app.run(debug=True)
