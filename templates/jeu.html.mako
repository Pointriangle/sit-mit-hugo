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
            % if is_admin: 
                <a class="btn" href="${url_for('ajoutprof')}">Ajouter un professeur</a>
            % endif 
            <a class="btn" href="${url_for('leaderboardpro')}">Les professeurs les plus recherchés</a> 
            <a class="btn" href="${url_for('leaderboardeleve')}">Les plus gros joueurs</a>
            % if is_logged_in: 
                <a class="btn" href="${url_for('accueil')}"> Accueuil </a>
                <p><a class="btn" href="${url_for('logout')}">Log out</a></p><br><br>
            % endif
        </div>
    </header>

    <main>
        <h1 class="h1-barre">Bienvenue ${pseudo} dans AkiPlanta</h1>
        <p id="question">Pense à un personnage, je vais essayer de le deviner.</p>

        % if question:
            <form method="post">
                <input type="hidden" name="question_type" value="${question_type}">
                <p id="question">${question}</p>
                <div class="buttons">
                    <button class="btn" type="submit" name="reponse" value="oui">Oui</button>
                    <button class="btn" type="submit" name="reponse" value="non">Non</button>
                </div>
            </form>
        % elif final_prof:
            <p id="question">Je pense que tu penses à <strong>${final_prof}</strong> !</p>
        % else:
            <p id="question">Je ne peux pas deviner... Il me manque des infos.</p>
        % endif

        
        <form method="post">
            
            %if correct==True:
                <div class="buttons">
                    <button class="btn" type="submit" name="ok" value="true">Juste</button>
                    <button class="btn" type="submit" name="ok" value="false">Faux</button>
                </div>
            %else:
                <button class="btn" type="submit" name="restart" value="true">Restart</button>
            % endif
        </form>
    </main>

    <footer>
        <div class="contacts">
            <p>Bug, problème ou curiosité ? <a href="${url_for('contacts')}">Contactez-nous</a></p>  
        </div>
    </footer>
</body>
</html>
