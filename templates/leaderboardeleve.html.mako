<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leaderboard des élèves</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div class="logo">
            <img id="logob" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
            <div class="bandeau">
              <a class="btn" href="${url_for('accueil')}">Retour à l'accueuil</a>
            </div>
            
            
        </div>
    </header>

    <main>
        <h1 class="h1-barre">Leaderboard des joueurs</h1>
        <table>
            <tr>
                <th>Classement</th>
                <th>Pseudo</th>
                <th>Nombre de parties</th>
            </tr>
            <tr>
                <td>1</td>
                <td>${users[0]["pseudo"]}</td>
                <td>${users[0]["points"]}</td>
            </tr>
            <tr>
                <td>2</td>
                <td>${users[1]["pseudo"]}</td>
                <td>${users[1]["points"]}</td>
            </tr>
            <tr>
                <td>3</td>
                <td>${users[2]["pseudo"]}</td>
                <td>${users[2]["points"]}</td>
            </tr>
        </table>
    </main>

    <footer>
        <div class="contacts">
            <p>Bug, problème ou curiosité ? <a href="${url_for('contacts')}">Contactez-nous</a></p>  
        </div>
    </footer>
</body>
</html>
