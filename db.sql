PRAGMA encoding="UTF-8";

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    pseudo TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    points INTEGER DEFAULT 0,
    admin BOOLEAN DEFAULT 0,
    created_at DATETIME
);

CREATE TABLE teachers (
    id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL UNIQUE,
    genre TEXT NOT NULL,
    couleur_yeux TEXT NOT NULL,
    couleur_cheveux TEXT NOT NULL,
    taille TEXT NOT NULL,
    branche TEXT NOT NULL,
    points INTEGER DEFAULT 0,   
    created_at DATETIME 
);
CREATE TABLE question (
    id INTEGER PRIMARY KEY ,
    type TEXT NOT NULL UNIQUE,
    q TEXT NOT NULL UNIQUE
    
);
