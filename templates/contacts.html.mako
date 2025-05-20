<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
    <title>Contacts</title>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
</head>
<body>
    <header>
        <div class="logo">
            <img id="logoa" src="${url_for('static',filename='LOGO.png')}" alt="Logo">
        </div>
    </header>

    <main>
        <h3>Zêta&Corp : qui sommes-nous ?</h3>
        <img src="${url_for('static',filename='Pointbendo.png')}" id="photo">
        <p id="presentation">Le collectif Zêta&Corp rassemble deux codeurs du nom de Pointriangle et Bendospeed9. Les deux créateurs de ce jeu se sont rencontrés et ont développé leur amitié grâce aux jeux vidéo, et ont donc voulu en créer un petit pour un projet scolaire. Ce site en est le résultat.</p>
        
        <h3 classe="h1-barre">Nous contacter</h3>
        <p id="question" class="contact-info">
            Nous sommes joignables à l'adresse 
            <a href="mailto:zetancorp@gmail.com" class="instagram-link">
                <img src="${url_for('static',filename='mail.png')}" alt="Email" class="icon">
            </a>
        
            ou sur notre compte Instagram 
            <a href="https://www.instagram.com/zetancorp/" class="instagram-link">
                <img src="${url_for('static',filename='insta.png')}" alt="Instagram" class="icon">
            </a>
        </p>
    </main>

    <footer>
        <div class="contacts">
            <p><a href="${url_for('accueil')}">Accueuil</a></p>
        </div> 
    </footer>
</body>
</html>
