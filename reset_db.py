
# -*- encoding: utf-8 -*-
""""Réinitialise la base de donnée.

AVERTISSEMENT:
    1) Toutes les données présente dans la base de données seront effacées.
    2) Seules les données insérées par le fichier test.sql seront présentes.

Copyright (c) Nicolas Desprès <nicolas.despres@gmail.com>
"""


import sys
from pathlib import Path
import sqlite3
from traceback import print_exception


ME_DIR = Path(__file__).parent
DB_FILE = ME_DIR / "users.db"
INIT_SCRIPT = ME_DIR / "db.sql"
DATA_SCRIPT = ME_DIR / "users.sql"


def execute_sql_script(db, path):
    with path.open(encoding="utf-8") as f:
        content = f.read()
        try:
            db.executescript(content)
        except sqlite3.Error as e:
            print(f"Erreur pendant l'exécution du script SQL: {path}")
            print(f"   ({type(e).__name__}): {e}")
            sys.exit(1)


try:
    # Delete DB file.
    if DB_FILE.exists():
        DB_FILE.unlink()
        print(f"Base de données supprimée: {DB_FILE}")
    # Initialize database.
    with sqlite3.connect(DB_FILE) as db:
        # Create structure.
        execute_sql_script(db, INIT_SCRIPT)
        print("Structure de la base de données initialisée.")
        # Insert test data.
        if DATA_SCRIPT.exists():
            execute_sql_script(db, DATA_SCRIPT)
            print("Données de test insérées dans la base de données.")
        else:
            print("Script d'insertion de données de test non trouvé "
                f"({DATA_SCRIPT})")
except FileNotFoundError as e:
    print(f"Fichier introuvable: {e.filename}")
except Exception as e:
    print("Une erreur inattendue s'est produite !!!")
    print_exception(*sys.exc_info())
finally:
    input("Appuyer sur ENTREE pour terminer le programme...")

