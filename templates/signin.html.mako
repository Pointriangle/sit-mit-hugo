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
        <div class="signup">
            <form>
                <label>
                    <h3>Créer un compte</h3>
                </label>
                <label>
                    <p>Nom d'utilisateur</p>
                    <input type="text" > 
                </label>
                <label>
                    <p>Mot de passe</p>
                    <input type="password" > 
                </label>
                
                <label>
                    <p>Confirmer le mot de passe</p>
                    <input type="password" > 
                </label>
                
                <div class="buttons">
                    <a class="btn" href="${url_for('jeu')}">S'inscrire</a>
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