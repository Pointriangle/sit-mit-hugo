<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Ajout de professeurs</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div>
            % if is_logged_in:
                <a href="${url_for('profil',pseudo = session.get("pseudo"))}" >
                    <img src="${url_for('avatar', filename=avatar)}" width="160" height="160"  class="r">
                </a>
            % endif
        
            <div class="logo">
                <img id="logoa" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
            </div>
        </div>
        <div class="bandeau">
            <a class="btn" href="${url_for('jeu')}">Jeu</a>
            <a class="btn" href="${url_for('leaderboardpro')}">Les professeurs les plus recherchés</a> 
            <a class="btn" href="${url_for('leaderboardeleve')}">Les plus gros joueurs</a>
            % if is_logged_in: 
                <a class="btn" href="${url_for('logout')}">Log out</a>
                <a class="btn" href="${url_for('accueil')}"> Accueuil </a>
            % endif
            
        </div>
    </header>
    
    <main>
        <h1 class="h1-barre">Ajout de professeurs à deviner</h1>
        <form id="ajoutProfesseurForm" method="POST">
            <label for="name">Nom</label>
            <input type="text" id="name" name="name" required>

            <label for="couleur_cheveux">Couleur des Cheveux</label>
            <select id="couleur_cheveux" name="couleur_cheveux" required>
                <option>Sombres</option>
                <option>Clairs</option>
            </select>
            <label for="couleur_yeux">Couleur des Yeux</label>
            <select type="text" id="couleur_yeux" name="couleur_yeux"required>
                <option>Clairs</option>
                <option>Sombres</option>
            </select>
            <label for="taille">Taille </label>
            <select type="text" id="taille" name="taille" required>
                <option>Grand</option>
                <option>Petit</option>
            </select>

            <label for="genre">Genre</label>
            <select type="text" id="genre" name="genre" required>
                <option>Homme</option>
                <option>Femme</option>
            </select>

            <label for="lunettes">lunettes</label>
            <select type="text" id="lunettes" name="lunettes" required>
                <option>oui</option>
                <option>non</option>
            </select>
            %if error is not None:
        <p style="color:red">${error}</p>
        %endif
        %if validation:
        <p style="color:green">Professeur enregistré</p>
        %endif
            <div class="buttons-ajout">
                <input  type="submit" class="btn"value="Ajouter professeur"> 
            </div>
        </form>
    </main>

    <footer>
        
    </footer>

</body>
</html>
