
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accueil</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div class="logo">
            <img id="logoa" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
        </div>
        <div class="bandeau">
            <a class="btn " href="${url_for('leaderboardpro')}">Les professeurs les plus recherchés</a> 
            <a class="btn " href="${url_for('leaderboardeleve')}">Les plus gros joueurs</a>
            % if is_logged_in: 
                <a class="btn" href="${url_for('logout')}">Log out</a>
            % endif
        </div>
    </header>

    <main>
        <h1>Profil de ${pseudo} </h1>
        <p id="questions">Pseudo: ${pseudo} </p> 
        <p id="questions">Nombre de parties: ${points} </p> 
        <p id="questions">Actif depuis le: ${created_at} </p>  
        <form method="POST">
                <label>
                    <h3>Changer de mot de passe</h3>
                </label>
                <label for="mdp">
                    <p>Ancien mot de passe</p>
                    <input class="field" type="text" id="mdp" name="mdp" required> 
                </label>
                
                <label for="password">
                    <p>Nouveau mot de passe</p>
                    <input class="field" type="password" id="nmdp" name="nmdp" required> 
                </label>

                <label for="confirm">
                    <p>Confirmer le nouveau mot de passe</p>
                    <input class="field" type="password" id="confirm" name="confirm" required> 
                </label>
                
                <div class="buttons">
                    <input class="btn" type="submit" value="Changer de mot de passe" />
                </div>
            </form> 
         <div class="buttons">
            <a class="btn" href="${url_for('accueil')}"> Retour à l'accueuil </a>
            <a class="btn" href="${url_for('jeu')}"> Retour au jeu </a>  
        </div>    
    </main>

    <footer>
        <div class="contacts">
            <p>Bug, problème ou curiosité? <a href="${url_for('contacts')}">Contactez-nous</a></p>  
        </div>
    </footer>
</body>
</html>