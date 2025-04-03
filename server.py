
"""
Server Web d'exemple écrit en Python avec Flask.
"""
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))

from flask import abort,request, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename
from datetime import datetime
from flask_mako import render_template,MakoTemplates
from flask_sqlite import SQLiteExtension
from flask_sqlite import get_db
import sqlite3
from random import randint
from flask import Flask ,session 
app = Flask("Akiplanta")  
MakoTemplates(app)
SQLiteExtension(app)
app.secret_key = os.urandom(24)  


class ValidationError(ValueError):
    """Error in users provided values."""
    pass


    
@app.route("/")
def index():
    return redirect(url_for("accueil"), code=303)

@app.route("/accueil")
def accueil():
    is_logged_in = "pseudo" in session  
    return render_template("accueil.html.mako",is_logged_in=is_logged_in)

@app.route("/contacts")
def contacts():
    return render_template("contacts.html.mako")
@app.route("/ajoutprof", methods=["GET", "POST"])
def ajoutprof():
    if "pseudo" not in session:
        return redirect(url_for("login"), code=303)

    if not session.get("admin", False):
        abort(403) 
    if request.method == "GET":
        return render_template('ajoutprof.html.mako',error=None,validation=False) 
    
    elif request.method == "POST": 
        db = get_db()
        try:
            if request.form['genre']=="Homme":
                genre=0
            else:
                genre=1
            if request.form['couleur_yeux']=="Clairs":
                couleur_yeux=0
            else:
                couleur_yeux=1
            if request.form['couleur_cheveux']=="Clairs":
                couleur_cheveux=0
            else:
                couleur_cheveux=1
            if request.form['taille']=="Petit":
                taille=0
            else:
                taille=1
            db.execute(
                "INSERT INTO teachers (name, genre, couleur_yeux,couleur_cheveux,taille,branche,created_at) VALUES (?, ?, ?,?,?,?,?)",
                (request.form['name'], genre,couleur_yeux,couleur_cheveux,taille,request.form["branche"],datetime.now())
            )
            db.commit()
            is_logged_in = "pseudo" in session  
            return render_template("ajoutprof.html.mako", validation=True,error=None,is_logged_in=is_logged_in)
        
        except sqlite3.IntegrityError as ie:
            return render_template("ajoutprof.html.mako", error="Ce professeur est déja enregistré.",validation=False)
        
        finally:
            db.rollback()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html.mako")
    elif request.method == "POST":
        pseudo = request.form.get("pseudo")
        password = request.form.get("password")

        if not pseudo or not password:
            return render_template("login.html.mako", error="Remplissez tous les champs.")

        db = get_db()
        try:
            cursor = db.execute("SELECT pseudo, password, id, admin FROM users WHERE pseudo = ?", (pseudo,))
            user = cursor.fetchone()

            if user and user["password"] == password:
                session["pseudo"] = pseudo
                session["admin"] = bool(user["admin"])
                return redirect(url_for("jeu"), code=303)
            else:
                return render_template("login.html.mako", error="Identifiants incorrects.")
        except ValidationError as e:
            return render_template("login.html.mako", error=str(e))
        finally:
            db.rollback()

@app.route("/jeu")
def jeu():
    if "pseudo" not in session:
        return redirect(url_for("login"), code=303)
    is_admin = session.get("admin", False)
    is_logged_in = "pseudo" in session    
    return render_template("jeu.html.mako", is_admin=is_admin,is_logged_in=is_logged_in,pseudo=session.get("pseudo"))

@app.route("/leaderboardeleve")
def leaderboardeleve():
    db = get_db()
    cursor = db.execute("SELECT pseudo, points FROM users ORDER BY points DESC limit 3")
    users = cursor.fetchall() 
    is_logged_in = "pseudo" in session  
    return render_template('leaderboardeleve.html.mako', users=users, is_logged_in=is_logged_in)

@app.route("/leaderboardpro")
def leaderboardpro():
    db = get_db()
    cursor = db.execute("SELECT name, points FROM teachers ORDER BY points DESC limit 3")
    teachers = cursor.fetchall() 
    is_logged_in = "pseudo" in session  
    return render_template('leaderboardpro.html.mako', teachers=teachers, is_logged_in=is_logged_in)

@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        return render_template('signin.html.mako', error=None)  
    
    elif request.method == "POST": 
        db = get_db()
        try:
            if request.form["password"] != request.form["confirm"]:
                raise ValidationError("Les mots de passe ne correspondent pas.")

            db.execute(
                "INSERT INTO users (pseudo, password, created_at) VALUES (?, ?, ?)",
                (request.form["pseudo"], request.form["password"], datetime.now()),
            )
            db.commit()
            pseudo=request.form["pseudo"]
            session["pseudo"] = pseudo
            return redirect(url_for("jeu"), code=303)
        
        except ValidationError as e:
            return render_template("signin.html.mako", error=str(e))
        
        except sqlite3.IntegrityError as ie:
            return render_template("signin.html.mako", error="Ce nom d'utilisateur est déjà pris.")
        
        finally:
            db.rollback()

@app.route("/logout")
def logout():
    session.clear()
    return render_template("logout.html.mako")

@app.route("/profil/<pseudo>")
def profil(pseudo):
    if "pseudo" not in session:
        return redirect(url_for("login"), code=303)
    db = get_db()
    cursor = db.execute("SELECT * FROM users WHERE pseudo = ?", (pseudo,))
    user = cursor.fetchone() 
    return render_template('profil.html.mako', pseudo=user["pseudo"], points=user["points"], created_at=user["created_at"])



def algo ():
    db = get_db()
    questions = db.execute("SELECT id, type FROM question")
    best_question = None
    best_balance = 0
    
    for question in questions:
        q_id = question[0]
        q_type = question[1]
        
        cursor = db.execute(f"SELECT {q_type} FROM teachers")
        responses = []
        for q_type in cursor:
            responses.append(q_type)
        
        c0 = 0
        c1 = 0
        for response in responses:
            if response == "0":
                c0 =c0+ 1
            elif response == "1":
                c1 = c1+ 1
        
        if c0 > 0 and c1 > 0:
            b = min(c0, c1) / max(c0, c1)
            if b > brat:
                brat = b
                bq = (q_id, q_type)
    print(best_question)

    return best_question

algo()
    



app.run(debug=True)






































app.run(debug=True)
