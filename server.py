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
app = Flask("SuperSite")  # Crée une application Flask nommée "SuperSite".
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