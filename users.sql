INSERT INTO users (pseudo, password, points, admin, created_at) 
VALUES ('c', '2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6', 0, 1, datetime('now')),
('b', '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d', 0, 1, datetime('now')),
('a', 'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb', 0, 0, datetime('now'));

INSERT INTO question (type,q,oui) 
VALUES ('genre','Est ce un homme?',0),
 ('couleur_yeux','A-t-il/elle les yeux clairs ?',0),
 ('couleur_cheveux','A-t-il/elle les cheveux clairs ?',0),
 ('lunettes','porte-il/elle des lunettes ?',1),
 ('taille','Est-il/elle grand(e) ?',1);


INSERT INTO teachers (name, genre, couleur_yeux, couleur_cheveux, taille, branche, points, created_at, lunettes)
VALUES('Mr. Posse', 0, 0, 1, 1, 'Français, Latin', 0, '2025-04-03 17:55:55.230838', 1),
('Mme. Gillioz', 1, 0, 1, 0, 'Anglais', 0, '2025-04-03 17:56:28.117501', 0),
('Mr. Mivelaz', 0, 1, 1, 1, 'Mathématiques', 0, '2025-04-03 17:56:43.151456', 1),
('Mr. Bridel', 0, 1, 1, 1, 'Mathématiques', 0, '2025-04-03 17:57:15.821326', 0),
('Mr. Troillet', 0, 1, 1, 0, 'Sport', 0, '2025-04-03 17:57:42.984857', 0),
('Mr. Després', 0, 1, 1, 1, 'Informatique', 0, '2025-04-03 17:58:04.309376', 1),
('Mme. Rittiner', 1, 1, 1, 1, 'Allemand', 0, '2025-04-03 17:58:27.793754', 1),
('Mme Crettenand-Sierro', 1, 1, 1, 0, 'Rectorat', 0, '2025-04-03 17:59:21.489065', 1),
('Mr. Gaillard', 0, 1, 1, 1, 'Histoire', 0, '2025-04-03 18:00:22.431923', 0),
('Mr. Emery', 0, 1, 1, 1, 'Musique', 0, '2025-04-03 18:00:54.423307', 0),
('Mme. Dupont', 1, 0, 0, 1, 'Biologie', 0, '2025-04-10 09:10:00', 1),
('Mr. Lambert', 0, 0, 0, 0, 'Chimie', 0, '2025-04-10 09:10:01', 0),
('Mme. Schneider', 1, 1, 0, 1, 'Physique', 0, '2025-04-10 09:10:02', 1),
('Mr. Robert', 0, 1, 0, 1, 'Histoire', 0, '2025-04-10 09:10:03', 0),
('Mme. Reymond', 1, 0, 1, 0, 'Géographie', 0, '2025-04-10 09:10:04', 1),
('Mr. Muller', 0, 1, 0, 0, 'Informatique', 0, '2025-04-10 09:10:05', 1),
('Mme. Blanc', 1, 1, 1, 1, 'Français', 0, '2025-04-10 09:10:06', 0),
('Mr. Jordan', 0, 0, 1, 1, 'Latin', 0, '2025-04-10 09:10:07', 1),
('Mme. Zufferey', 1, 0, 1, 1, 'Anglais', 0, '2025-04-10 09:10:08', 0),
('Mr. Vocat', 0, 0, 0, 0, 'Sport', 0, '2025-04-10 09:10:09', 0),
('Mme. Monnet', 1, 1, 0, 1, 'Musique', 0, '2025-04-10 09:10:10', 1),
('Mr. Nicolet', 0, 1, 0, 1, 'Mathématiques', 0, '2025-04-10 09:10:11', 1),
('Mme. Vannay', 1, 0, 0, 0, 'Allemand', 0, '2025-04-10 09:10:12', 0),
('Mr. Bétrisey', 0, 0, 1, 0, 'Chimie', 0, '2025-04-10 09:10:13', 1),
('Mme. Fumeaux', 1, 1, 1, 0, 'Biologie', 0, '2025-04-10 09:10:14', 1),
('Mr. Delaloye', 0, 0, 0, 1, 'Physique', 0, '2025-04-10 09:10:15', 0),
('Mme. Genoud', 1, 0, 0, 1, 'Latin', 0, '2025-04-10 09:10:16', 1),
('Mr. Fournier', 0, 1, 1, 0, 'Informatique', 0, '2025-04-10 09:10:17', 1),
('Mme. Maye', 1, 1, 0, 0, 'Philosophie', 0, '2025-04-10 09:10:18', 1),
('Mr. Barras', 0, 0, 1, 0, 'Philosophie', 0, '2025-04-10 09:10:19', 0);
