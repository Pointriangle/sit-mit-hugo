<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Créer un compte</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div class="logo">
            <img id="logoa" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
        </div>
    </header>
    
    <main>
        <h1 class="h1-barre">Bienvenue dans l'équipe !</h1>
        <div class="login">
            <form method="POST">
                <label>
                    <h3>Créer un compte</h3>
                </label>
                <label for="pseudo">
                    <p>Nom d'utilisateur</p>
                    <input class="field" type="text" id="pseudo" name="pseudo" required> 
                </label>
                
                <label for="password">
                    <p>Mot de passe</p>
                    <input class="field" type="password" id="password" name="password" required> 
                </label>

                <label for="confirm">
                    <p>Confirmer le mot de passe</p>
                    <input class="field" type="password" id="confirm" name="confirm" required> 
                </label>
                 % if error is not None:
            <p style="color: red">ERREUR: ${error}</p>
                % endif
                <div class="buttons">
                    <input class="btn" type="submit" value="S'inscrire" />
                    <a class="btn" href="${url_for('login')}">Déjà un compte ?</a>
                </div>
            </form>
        </div>
    </main>

    <footer>
        <div class="contacts">
            <p>Bug, problème ou curiosité ? <a href="${url_for('contacts')}">Contactez-nous</a></p>  
        </div>
    </footer>
</body>
</html>
