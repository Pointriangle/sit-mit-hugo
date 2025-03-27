PRAGMA encoding="UTF-8";

CREATE TABLE users (
    id INTEGER PRIMARY KEY ,
    pseudo TEXT NOT NULL, 
    password TEXT NOT NULL,  
    created_at DATETIME 
);
