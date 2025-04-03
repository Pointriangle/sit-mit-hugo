<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Ajout de Professeurs</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div class="logo">
            <img id="logob" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
        </div>
        <div class="bandeau">
            <a class="btn" href="${url_for('jeu')}">Jeu</a>
            <a class="btn" href="${url_for('leaderboardpro')}">Les professeurs les plus recherchés</a> 
            <a class="btn" href="${url_for('leaderboardeleve')}">Les plus gros joueurs</a>
            % if is_logged_in: 
                <a class="btn" href="${url_for('logout')}">Log out</a>
            % endif
            
        </div>
    </header>
    
    <main>
        <h1 class="h1-barre">Ajout de Professeurs à deviner</h1>
        <form id="ajoutProfesseurForm" method="POST">
            <label for="name">Nom</label>
            <input type="text" id="name" name="name" required>

            <label for="branche">Branche</label>
            <input type="text" id="branche" name="branche" required>

            <label for="couleur_cheveux">Couleur des Cheveux</label>
            <select id="couleur_cheveux" name="couleur_cheveux" required>
                <option>Sombre</option>
                <option>Clair</option>
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
            <div class="buttons-ajout">
                <input  type="submit" class="btn"value="Ajouter professeur"> 
            </div>
        </form>
        %if error is not None:
        <p style="color:red">${error}</p>
        %endif
        %if validation:
        <p style="color:green">Professeur enregistré</p>
        %endif
    </main>

    <footer>
        
    </footer>

</body>
</html>
