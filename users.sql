INSERT INTO users (pseudo, password, points, admin, created_at) 
VALUES ('c', '2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6', 0, 1, datetime('now')),
('b', '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d', 0, 1, datetime('now')),
('a', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 0, 0, datetime('now'));

INSERT INTO question (type,q) 
VALUES ('genre','Est ce un homme?'),
 ('couleur_yeux','A-t-il/elle les yeux clairs ?'),
 ('couleur_cheveux','A-t-il/elle les cheveux clairs ?'),
 ('taille','Est-il/elle grand(e) ?');
