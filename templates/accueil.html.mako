
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
        <div>
            % if is_logged_in:
                <a href="${url_for('profil',pseudo = session.get("pseudo"))}" >
                    <img src="${url_for('avatar', filename=avatar)}" width="160" height="160" class="r">
                </a>
            % endif
        
            <div class="logo">
                <img id="logoa" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
            </div>
        </div>
        <div class="bandeau">
            <a class="btn " href="${url_for('leaderboardpro')}">Les professeurs les plus recherchés</a> 
            <a class="btn " href="${url_for('leaderboardeleve')}">Les plus gros joueurs</a>
            % if is_logged_in: 
                <a class="btn" href="${url_for('logout')}">Log out</a>
                <a class="btn" href="${url_for('jeu')}">Jeu</a>
            
                
            % endif
        </div>
    </header>

    <main>
        <h1>Bienvenue sur AkiPlanta, le qui-est-ce <br> des professeurs!</h1>
        <p id="questions">Le concept du jeu est de faire deviner à la machine, en répondant à des questions fermées, l'identité d'un professeur du Lycée-Collège de la Planta</p> 
        <div class="buttons">
            <a class="btn" href="${url_for('login')}"> Se connecter </a>
            <a class="btn" href="${url_for('signup')}"> Créer un compte </a>  
        </div>
        <div class="buttons">
            <a  class="btn" id="boutonFuyant">Jouer sans se connecter</a>
        </div>
        
        <script>
            const bouton = document.getElementById('boutonFuyant');
            
            document.addEventListener('mousemove', (souris) => {
                const rect = bouton.getBoundingClientRect();
                const distance = Math.sqrt(
                    Math.pow(souris.clientX - (rect.left + rect.width / 2), 2) +
                    Math.pow(souris.clientY - (rect.top + rect.height / 2), 2)
                );
                
                if (distance < 100) {
                    const newTop = Math.random() * (window.innerHeight - rect.height);
                    const newLeft = Math.random() * (window.innerWidth - rect.width);
                    
                    bouton.style.top = newTop + 'px';
                    bouton.style.left = newLeft + 'px';
                }
            });
        </script>
    </main>

    <footer>
        <div class="contacts">
            <p>Bug, problème ou curiosité? <a href="${url_for('contacts')}">Contactez-nous</a></p>  
        </div>
    </footer>
</body>
</html>