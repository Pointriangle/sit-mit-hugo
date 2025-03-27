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
            <h3>Créer un compte</h3>
            <form method="POST">
                <label for="pseudo">Nom d'utilisateur</label>
                <input type="text" id="pseudo" name="pseudo" required/> 
                <label for="password">Mot de passe</label>
                <input type="password" id="password" name="password" required/> 
                <label for="confirm">Confirmer le mot de passe</label>
                <input type="password" id="confirm" name="confirm" required /> 
                <div class="buttons">
                    <input type="submit" class="btn" value="S'inscrire"/>
                    <a class="btn" href="${url_for('login')}">Déjà un compte ?</a>
                </div>
            % if error is not None:
                <p style= "color:red">ERREUR: ${error} </p>
            %endif
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