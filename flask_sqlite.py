# -*- encoding: utf-8 -*-
"""Extension flask minimaliste pour sqlite3.

Peut être exécuter depuis la ligne de commande pour initialiser la base de données.

Options:

    SQLITE_DB_FILENAME
        Nom du fichier de base de données (par défaut: 'data.db')

        AVERTISSEMENT: si la valeur de cette option est changé le script 'reset_db.py'
        ne fonctionnera plus.

    SQLITE_DB_ATTR
        Nom de l'attribut utilisé pour stocker la connexion dans le context global.
        Normalement cette option n'a pas besoin d'être modifiée.
        (valeur par défaut: '_sqlite_db')

Copyright (c) Nicolas Desprès <nicolas.despres@gmail.com>
"""


import sqlite3

from flask import g as GLOBAL
from flask import current_app


# ------------------------
# Fonctions de l'extension
# ------------------------


def connect_db(filename):
    """Établie une nouvelle connexion.
    """
    db = sqlite3.connect(filename, detect_types=sqlite3.PARSE_DECLTYPES)
    # Demande que les tables de résultat des requêtes soient des listes
    # de dictionnaires plutôt que des listes de listes.
    db.row_factory = sqlite3.Row
    # L'utilisation de db.commit et db.rollback est nécessaire.
    if hasattr(db, "autocommit"):  # Pas disponible avant Python 3.12
        db.autocommit = current_app.config['SQLITE_AUTOCOMMIT']
    return db


def get_db():
    """Obtiens une connexion à la base de données.

    Se connecte à la base de données et enregistre la connexion
    dans le contexte global.
    """
    # Tente de récupérer une connexion existante.
    attr_name = current_app.config['SQLITE_DB_ATTR']
    db = GLOBAL.get(attr_name)
    if db is None:  # Si auncune connextion existante
        # Établie une nouvelle connexion.
        db = connect_db(current_app.config['SQLITE_DB_FILENAME'])
        # Enregistre la connexion dans le contexte global pour éviter d'avoir
        # à se reconnecter à chaque requête.
        setattr(GLOBAL, attr_name, db)
    return db


def close_db(exception=None):
    """Ferme la connexion à la base de données lorsque l'application Web se termine.
    """
    # Essaie de récupérer la connexion active à la base de données dans
    # l'attribut 'db' du contexte global.
    # La variable 'db' recevra la valeur None si aucune connexion n'est
    # active.
    db = GLOBAL.pop('db', None)
    # Ferme la connexion à la base de données s'il y en avait une d'établie.
    if db is not None:
        db.close()


# ---------------
# Extension Flask
# ---------------

class SQLiteExtension:
    """Interface de l'extension Flask."""

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Enregistre l'extension dans la liste des extensions.
        app.extensions['sqlite'] = self

        # Définie la valeur par défaut des options de l'extension.
        app.config.setdefault('SQLITE_DB_FILENAME', 'data.db')
        app.config.setdefault('SQLITE_DB_ATTR', '_sqlite_db')
        app.config.setdefault('SQLITE_AUTOCOMMIT', False)

        # Inscrit la fonction close_db pour qu'elle soit déclenchée lorsque
        # l'application se termine.
        app.teardown_appcontext(close_db)
