<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Leaderboard des professeurs</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div class="logo">
            <img id="logoa" src="${url_for('static', filename='LOGO.png')}" alt="Logo">
            <div class="bandeau">
                % if is_logged_in:
                    <a class="btn" href="${url_for('jeu')}">Jeu</a>
                % endif
                <a class="btn" href="${url_for('accueil')}">Retour à l'accueil</a>
            </div>
        </div>
    </header>

    <main>
        <h1 class="h1-barre">Leaderboard des professeurs</h1>
        <table>
            <tr>
                <td>1</td>
                <td>${teachers[0]["name"]}</td>
                <td>${teachers[0]["points"]}</td>
            </tr>
            <tr>
                <td>2</td>
                <td>${teachers[1]["name"]}</td>
                <td>${teachers[1]["points"]}</td>
            </tr>
            <tr>
                <td>3</td>
                <td>${teachers[2]["name"]}</td>
                <td>${teachers[2]["points"]}</td>
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

