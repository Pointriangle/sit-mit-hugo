
"""
Server Web d'exemple écrit en Python avec Flask.
"""
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
import random
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
            if request.form['lunettes']=="oui":
                lunettes=0
            else:
                lunettes=1
            db.execute(
                "INSERT INTO teachers (name, genre, couleur_yeux,couleur_cheveux,taille,branche,created_at,lunettes) VALUES (?, ?, ?,?,?,?,?,?)",
                (request.form['name'], genre,couleur_yeux,couleur_cheveux,taille,request.form["branche"],datetime.now(),lunettes)
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
    global pj
    global nom
    if "pseudo" not in session:
        return redirect(url_for("login"))

    
    db = get_db()
    pseudo = session["pseudo"]
    is_admin = session.get("admin", False)  
    is_logged_in = True  

    
    if "rep" not in session:
        session["rep"] ={}

    
    if request.method =="POST":

        if request.form.get("restart"):
            session["rep"]= {}  
            return redirect(url_for('jeu'))  
        
        if request.form.get("ok"):
            if request.form.get("ok")=="true":
                nom=session["fp"]
                        
        
                cursor=db.execute(
                        "SELECT points FROM users WHERE pseudo=?",
                        (session.get("pseudo"),))
                user = cursor.fetchone()
                points= int(user['points'])
                points+= 1
                db.execute(
                        "UPDATE users SET points=? WHERE pseudo=?",
                        (points,session.get("pseudo"),))
                
                curseur=db.execute(
                        "SELECT points FROM teachers WHERE name=?",
                        (nom,))
                teacher = curseur.fetchone()
                points= int(teacher['points'])
                points+= 1
                db.execute(
                        "UPDATE teachers SET points=? WHERE name=?",
                        (points,nom,))

                db.commit()
                session["rep"]= {} 
                session["fp"]={}

                return redirect(url_for('jeu')) 
            else:
                
                if len(pj)>0:
                    session["fp"]={}
                    x=len(pj)
                    x=randint(0,x-1)
                    nom = pj[x]["name"]
                    del pj[x]
                    
                    j=True  
                    session["fp"]=nom
                    return render_template("jeu.html.mako", pseudo=pseudo, is_admin=is_admin, is_logged_in=is_logged_in, final_prof=nom,correct=j)
                else :
                    return render_template("jeu.html.mako", pseudo=pseudo, is_admin=is_admin, is_logged_in=is_logged_in, final_prof="Je ne sais pas encore. Essaie de recommencer.")
        if request.form.get("question_type") and request.form.get("reponse"):
            question = request.form["question_type"]
            repu = request.form["reponse"]


            curseur = db.execute("SELECT oui FROM question WHERE type = ?", (question,))
            ligne = curseur.fetchone()


            if ligne:

                vatt = ligne[0]


                if repu =="oui":
                    vg = str(vatt)
                else:

                    if vatt== 1:
                        vg ="0"
                    else:
                        vg ="1"


                session["rep"][question] = vg
                session.modified = True  
       
    curseur =db.execute("SELECT type, q FROM question")
    qall= curseur.fetchall()
    qres =[]  

  
    for q in qall:
        
        if q[0] not in session["rep"]:
            qres.append(q) 

    curseur = db.execute("SELECT * FROM teachers")
    nomc = [] 

    
    for desc in curseur.description:
        nom= desc[0] 
        nomc.append(nom) 
    profs_lignes =curseur.fetchall()  

    
    profs = []
    for ligne in profs_lignes:
        prof ={}
        for i in range(len(nomc)):
            prof[nomc[i]]=ligne[i]
        profs.append(prof)

 
    pres=[]
    
    for prof in profs:
        garder=True
        for question, valeur in session["rep"].items():
            if prof[question] !=valeur:
                garder = False  
                break
        if garder:
            pres.append(prof)

    
    if len(pres)==1:
        nom=pres[0]["name"]
        
        cursor=db.execute(
                "SELECT points FROM users WHERE pseudo=?",
                (session.get("pseudo"),))
        user = cursor.fetchone()
        points= int(user['points'])
        points+= 1
        db.execute(
                "UPDATE users SET points=? WHERE pseudo=?",
                (points,session.get("pseudo"),))
        
        curseur=db.execute(
                "SELECT points FROM teachers WHERE name=?",
                (nom,))
        teacher = curseur.fetchone()
        points= int(teacher['points'])
        points+= 1
        db.execute(
                "UPDATE teachers SET points=? WHERE name=?",
                (points,nom,))
        
        db.commit()
        session["rep"]= {} 
        return render_template("jeu.html.mako", pseudo=pseudo, is_admin=is_admin, is_logged_in=is_logged_in, final_prof=nom)

    
    
    bq = None
    if session["rep"] =={}:
    
        if qres:
            questionc = random.choice(qres)
            qtype = questionc[0]
            question_text = questionc[1]
            bq = (qtype, question_text)
    
    else:
        brat = 0

        for qtype, texte  in qres:
            c0 = 0
            c1 = 0
            for prof in pres:
                if prof[qtype] == "0":
                    c0 += 1
                elif prof[qtype] == "1":
                    c1 += 1

            if c0 > 0 and c1 > 0:
                score = min(c0, c1) / max(c0, c1)
                if score > brat:
                    brat = score
                    bq = (qtype, texte)
                elif score==brat:
                    r=randint(0,1)
                    if r==0:
                        brat = score
                        bq = (qtype, texte)


    if bq:
        return render_template("jeu.html.mako", pseudo=pseudo, is_admin=is_admin, is_logged_in=is_logged_in, question_type=bq[0], question=bq[1])
    
    elif bq is None and  len(pres) != 1 :
        session["fp"]={}
        x=len(pres)
        x=randint(0,x-1)
        nom = pres[x]["name"]
        
        del pres[x]
        
        pj=pres
        pres=[]
        j=True    
        session["rep"]= {}
        session["fp"]=nom
        return render_template("jeu.html.mako", pseudo=pseudo, is_admin=is_admin, is_logged_in=is_logged_in, final_prof=nom,correct=j)


    cursor=db.execute(
            "SELECT points FROM users WHERE pseudo=?",
            (session.get("pseudo"),))
    user = cursor.fetchone()
    points= int(user['points'])
    points+= 1
    db.execute(
            "UPDATE users SET points=? WHERE pseudo=?",
            (points,session.get("pseudo"),))
    db.commit()
    session["rep"]= {}
    return render_template("jeu.html.mako", pseudo=pseudo, is_admin=is_admin, is_logged_in=is_logged_in, final_prof="Je ne sais pas encore. Essaie de recommencer.")


@app.route("/leaderboardeleve")
def leaderboardeleve():
    session["rep"]= {} 
    db = get_db()
    cursor = db.execute("SELECT pseudo, points FROM users ORDER BY points DESC limit 3")
    users = cursor.fetchall() 
    is_logged_in = "pseudo" in session  
    return render_template('leaderboardeleve.html.mako', users=users, is_logged_in=is_logged_in)

@app.route("/leaderboardpro")
def leaderboardpro():
    session["rep"]= {} 
    db = get_db()
    cursor = db.execute("SELECT name, points FROM teachers ORDER BY points DESC limit 3")
    teachers = cursor.fetchall() 
    is_logged_in = "pseudo" in session  
    return render_template('leaderboardpro.html.mako', teachers=teachers, is_logged_in=is_logged_in)

@app.route("/signup", methods=["GET", "POST"])
def signup():
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
    session["rep"]= {} 
    error=None
    if request.method=='GET':
        if "pseudo" not in session:
            return redirect(url_for("login"), code=303)
        if session.get("pseudo") != pseudo:
            return redirect(url_for("profil", pseudo=session.get("pseudo")), code=303,error=error,validation=False)
        db = get_db()
        cursor = db.execute("SELECT * FROM users WHERE pseudo = ?", (pseudo,))
        user = cursor.fetchone() 
        cursor=db.execute("SELECT pseudo from users WHERE points < ?", (user["points"],))
        count= db.execute("SELECT COUNT(*) FROM users")
        percentile= (len(cursor.fetchall())/count.fetchone()[0])*100
        return render_template('profil.html.mako', pseudo=user["pseudo"], points=user["points"], created_at=user["created_at"],error=error, validation =False, percentile=percentile)
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
            return render_template("profil.html.mako",pseudo=user["pseudo"], points=user["points"], created_at=user["created_at"],error=str(e),validation=False)
        
    return render_template('profil.html.mako', pseudo=user["pseudo"], points=user["points"], created_at=user["created_at"],error=error,validation=True) 

    



app.run(debug=True)