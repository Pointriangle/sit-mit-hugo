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
            <img src="/Logo/LOGO.png" alt="Logo">
        </div>
        <div class="bandeau">
            <a class="btn" href="leaderboardpro.html">Les professeurs les plus recherchés</a> 
            <a class="btn" href="leaderboardeleve.html">Les plus gros joueurs</a>
            <a class="btn" href="accueil.html">Log out</a>
        </div>
    </header>
    
    <main>
        <h1 class="h1-barre">Ajout de Professeurs à deviner</h1>
        <form id="ajoutProfesseurForm">
            <label for="etablissement">Nom</label>
            <input type="text" id="etablissement" required>

            <label for="branche">Branche</label>
            <input type="text" id="branche" required>

            <label for="couleurCheveux">Couleur des Cheveux</label>
            <input type="text" id="couleurCheveux" required>

            <label for="couleurYeux">Couleur des Yeux</label>
            <input type="text" id="couleurYeux" required>

            <label for="taille">Taille (grand, petit, moyen)</label>
            <input type="text" id="taille" required>

            <label for="genre">Genre</label>
            <input type="text" id="genre" required>
            
            <div class="buttons-ajout">
                <button  class="btn">Ajouter professeur</button> 
            </div>
        </form>
    </main>

    <footer>
        
    </footer>

</body>
</html>
