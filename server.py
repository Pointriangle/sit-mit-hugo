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

@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "GET":
        return render_template("login.html.mako", error=None)
    elif request.method == "POST":
        pseudo = request.form.get("pseudo")
        password = request.form.get("password")
   
        if not pseudo or not password:
            return render_template("login.html.mako", error="Tous les champs sont requis.")
        db = get_db()
        try:
            cursor = db.execute("SELECT pseudo, password,id  FROM users WHERE pseudo = ?",(pseudo,))
            user = cursor.fetchone()
            try:
            
                if user["password"] == password:
                    session.clear()
                    session["user_id"]=user["id"]
                    return redirect(url_for("profile", pseudo=pseudo), code=303)
                else:
                    return render_template("login.html.mako", error="Mot de passe incorrect.")
                
            except TypeError:
                return render_template("login.html.mako", error="Utilisateur non trouvé.")
    
           
        
        except ValidationError as e:
            return render_template("login.html.mako", error=str(e))
        except sqlite3.IntegrityError as ie:
            return render_template("login.html.mako", error=str(ie))
        finally:
            db.rollback() 

@app.route("/jeu")
def jeu():
    return render_template('jeu.html.mako')
@app.route("/leaderboardpro")
def leaderboardpro():
    return render_template('leaderboardpro.html.mako')
@app.route("/signin")
def signin():
    if request.method== "GET":
        return render_template('signin.html.mako')
    elif request.method=="POST":
       db=get_db()
       db.execute("INSERT INTO users (pseudo,password,created_at) VALUES (?,?,?)",request.form["pseudo"],request.form["password"],datetime.now())
       db.commit()
       return redirect(url_for("jeu"), code=303)
app.run(debug=True)






































app.run(debug=True)
