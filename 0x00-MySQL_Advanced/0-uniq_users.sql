-- script that creates a table users
CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL PRIMARY KEY IDENTITY,
    email VARCHAR(255),
    name VARCHAR(255)
);
