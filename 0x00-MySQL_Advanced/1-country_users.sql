-- Creating table in holberton db
DROP TABLE IF EXISTS users;
CREATE TABLE users(id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
                                email VARCHAR(255) NOT NULL UNIQUE,
                                name VARCHAR(255),
                                country CHAR(2) DEFAULT 'US' NOT NULL CHECK (country IN ('US', 'CO', 'TN')));
