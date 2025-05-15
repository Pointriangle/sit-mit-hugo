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
        <div>
            % if is_logged_in:
                <a href="${url_for('profil',pseudo = session.get("pseudo"))}" >
                    <img src="${url_for('avatar', filename=avatar)}" width="160" height="160"   class="r">
                </a>
            % endif
        
            <div class="logo">
                <img id="logoa" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
            </div>
        </div>
        <div class="bandeau">
            <a class="btn" href="${url_for('accueil')}"> Retour à l'accueuil </a>
            % if is_logged_in:
                <a class="btn" href="${url_for('jeu')}">Jeu</a>
                <a class="btn" href="${url_for('logout')}">log out</a>
            % endif
                
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
