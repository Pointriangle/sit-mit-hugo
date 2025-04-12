<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Déconnexion</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div class="logo">
            <img id="logoc" src="${url_for('static',filename='LOGO.png')}" alt="Logo"> 
        </div>
    </header>

        <main>
        <h1 class="h1-barre">Au revoir!!!</h1>
        <br><br>
        <div class="buttons">
            <a class="btn" href="${url_for('accueil')}">Accueil</a>
        </div>

    </main>


    <footer>
        <div class="contacts">
            <p>Bug, problème ou curiosité? <a href="${url_for('contacts')}">Contactez-nous</a></p>  
        </div>
    </footer>
</body>
</html>