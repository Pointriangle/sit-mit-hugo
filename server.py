
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
import hashlib


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
            hash = hashlib.sha256(request.form["password"].encode())
            hpassword = hash.hexdigest()
            if user and hpassword == user["password"]:
                session["pseudo"] = pseudo
                session["admin"] = bool(user["admin"])
                return redirect(url_for("jeu"), code=303)
            else:
                return render_template("login.html.mako", error="Identifiants incorrects.")
        except ValidationError as e:
            return render_template("login.html.mako", error=str(e))
        finally:
            db.rollback()

@app.route("/jeu", methods=["GET", "POST"])
def jeu():
    if "pseudo" not in session:
        return redirect(url_for("login"), code=303)
    
    is_admin = session.get("admin", False)
    is_logged_in = "pseudo" in session

    db = get_db()
    
    # Initialisation ou récupération de la liste filtrée de professeurs
    if 'filtered_teachers' not in session:
        cursor = db.execute("SELECT id FROM teachers")
        teachers = cursor.fetchall()
        session['filtered_teachers'] = [teacher['id'] for teacher in teachers]

    if request.method == "POST":
        # Récupérer la réponse de l'utilisateur
        response = request.form['response']
        current_question_id = int(request.form['current_question_id'])
        
        # Filtrer les professeurs en fonction de la réponse
        if response == "oui":
            db.execute(f"DELETE FROM filtered_teachers WHERE id NOT IN (SELECT teacher_id FROM teacher_answers WHERE question_id = ? AND answer = 1)", (current_question_id,))
        else:  # "non"
            db.execute(f"DELETE FROM filtered_teachers WHERE id NOT IN (SELECT teacher_id FROM teacher_answers WHERE question_id = ? AND answer = 0)", (current_question_id,))

        db.commit()

        # Choisir la question suivante basée sur les professeurs restants
        cursor = db.execute("SELECT id, type, q FROM question")
        questions = cursor.fetchall()

        best_question = None
        max_ratio = 0
        
        for question in questions:
            q_type = question['type']
            text = question['q']

            # Compter les réponses 0 et 1 pour chaque question
            cursor = db.execute(f"SELECT {q_type} FROM teachers WHERE id IN ({', '.join(map(str, session['filtered_teachers']))})")
            responses = cursor.fetchall()

            c0 = sum(1 for response in responses if response[0] == 0)
            c1 = sum(1 for response in responses if response[0] == 1)

            if c0 > 0 and c1 > 0:
                ratio = min(c0, c1) / max(c0, c1)
                if ratio > max_ratio:
                    max_ratio = ratio
                    best_question = question

        # Si une question a été trouvée, elle est envoyée, sinon, le jeu est terminé
        if best_question:
            session['current_question_id'] = best_question['id']
            return render_template("jeu.html.mako", question=best_question['q'], current_question_id=best_question['id'], is_logged_in=is_logged_in, pseudo=session.get("pseudo"))
        else:
            # Si aucune question n'est disponible, cela signifie que nous avons deviné un professeur
            return render_template("jeu.html.mako", question="Je pense avoir trouvé un professeur. Qui est-ce ?", is_logged_in=is_logged_in, pseudo=session.get("pseudo"))

    # Si on accède à la page sans avoir répondu, on commence une nouvelle partie
    cursor = db.execute("SELECT id, type, q FROM question")
    questions = cursor.fetchall()

    # Choisir la meilleure question de départ en fonction de la base de professeurs
    best_question = None
    max_ratio = 0
    for question in questions:
        q_type = question['type']
        text = question['q']
        
        cursor = db.execute(f"SELECT {q_type} FROM teachers WHERE id IN ({', '.join(map(str, session['filtered_teachers']))})")
        responses = cursor.fetchall()

        c0 = sum(1 for response in responses if response[0] == 0)
        c1 = sum(1 for response in responses if response[0] == 1)

        if c0 > 0 and c1 > 0:
            ratio = min(c0, c1) / max(c0, c1)
            if ratio > max_ratio:
                max_ratio = ratio
                best_question = question

    # Si une question est trouvée, on la pose, sinon le jeu est terminé
    if best_question:
        session['current_question_id'] = best_question['id']
        return render_template("jeu.html.mako", question=best_question['q'], current_question_id=best_question['id'], is_logged_in=is_logged_in, pseudo=session.get("pseudo"))
    else:
        return render_template("jeu.html.mako", question="Je pense avoir trouvé un professeur. Qui est-ce ?", is_logged_in=is_logged_in, pseudo=session.get("pseudo"))

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
            hash = hashlib.sha256(request.form["password"].encode())
            password = hash.hexdigest()
            db.execute(
                "INSERT INTO users (pseudo, password, created_at) VALUES (?, ?, ?)",
                (request.form["pseudo"], password, datetime.now()),
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

@app.route("/profil/<pseudo>",methods=["GET", "POST"])
def profil(pseudo):
    error=None
    if request.method=='GET':
        if "pseudo" not in session:
            return redirect(url_for("login"), code=303)
        if session.get("pseudo") != pseudo:
            return redirect(url_for("profil", pseudo=session.get("pseudo")), code=303,error=error)
        db = get_db()
        cursor = db.execute("SELECT * FROM users WHERE pseudo = ?", (pseudo,))
        user = cursor.fetchone() 
        return render_template('profil.html.mako', pseudo=user["pseudo"], points=user["points"], created_at=user["created_at"],error=error)
    elif request.method == "POST": 
        db = get_db()
        cursor = db.execute("SELECT * FROM users WHERE pseudo = ?", (pseudo,))
        user = cursor.fetchone()
        password = user["password"]
        hash = hashlib.sha256(request.form["mdp"].encode())
        hpassword = hash.hexdigest()
        try:
            if hpassword!=password:
                raise ValidationError("Mot de passe incorrect")
            if request.form["nmdp"] != request.form["confirm"]:
                raise ValidationError("Les mots de passe ne correspondent pas.")
            hash = hashlib.sha256(request.form["nmdp"].encode())
            password = hash.hexdigest()
            db.execute(
                "UPDATE users SET password=? WHERE pseudo=?",
                (password,session.get("pseudo"),))
            db.commit()
        except ValidationError as e:
            return render_template("profil.html.mako",pseudo=user["pseudo"], points=user["points"], created_at=user["created_at"],error=str(e))
        
        finally:
            db.rollback()
    return redirect(url_for("profil",pseudo=session.get("pseudo")), points=user["points"], created_at=user["created_at"], code=303,error=error))




    



app.run(debug=True)