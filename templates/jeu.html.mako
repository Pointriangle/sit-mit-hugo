<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jeu</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div class="logo">
            <img id="logoa" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
        </div>
        <div class="bandeau">
            <a class="btn" href="${url_for('leaderbordpro')}">Les professeurs les plus recherchés</a> 
            <a class="btn" href="${url_for('leaderbordeleve')}">Les plus gros joueurs</a>
            <a class="btn" href="${url_for('acceuil')}">Log out</a>
        </div>
    </header>

    <main>
        <h1 class="h1-barre">Bienvenue dans AkiPlanta</h1>
        <p id="question">Pense à un personnage, je vais essayer de le deviner.</p>
        
        <div class="buttons">
            <a class="btn">Oui</a>
            <a class="btn">Non</a>
        </div>

        <div class="buttons">
            <button class="btn btn-restart">Recommencer</button>
        </div>
    </main>

    <footer>
        <div class="contacts">
            <p>Bug, problème ou curiosité ? <a href="${url_for('contact')}">Contactez-nous</a></p>  
        </div>
    </footer>
</body>
</html>
