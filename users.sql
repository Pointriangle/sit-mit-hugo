INSERT INTO users (pseudo, password, points, admin, created_at) 
VALUES ('c', 'c', 0, 1, datetime('now')),
('b', 'b', 0, 1, datetime('now')),
('a', 'a', 0, 0, datetime('now'));

INSERT INTO question (type,q) 
VALUES ('genre','Est ce un homme?'),
 ('couleur_yeux','A-t-il/elle les yeux clairs ?'),
 ('couleur_cheveux','A-t-il/elle les cheveux clairs ?'),
 ('taille','Est-il/elle grand(e) ?');
