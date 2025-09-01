DROP TABLE IF EXISTS user_likes;
DROP TABLE IF EXISTS status_property;
DROP TABLE IF EXISTS property;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS ubication;
DROP TABLE IF EXISTS status;

CREATE TABLE status (
    status_id INT PRIMARY KEY AUTO_INCREMENT, 
    name VARCHAR(50) NOT NULL UNIQUE 
);

CREATE TABLE ubication (
    id_ubication INT PRIMARY KEY AUTO_INCREMENT, 
    ubi_id_ubication INT, 
    name VARCHAR(50) NOT NULL, 
    ubication_type VARCHAR(50), 
    FOREIGN KEY (ubi_id_ubication) REFERENCES ubication(id_ubication) 
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT, 
    id_ubication INT, 
    name VARCHAR(30), 
    last_name VARCHAR(30), 
    email VARCHAR(60) NOT NULL UNIQUE, 
    FOREIGN KEY (id_ubication) REFERENCES ubication(id_ubication) 
);

CREATE TABLE property (
    property_id INT PRIMARY KEY AUTO_INCREMENT, 
    id_ubication INT, 
    address VARCHAR(120), 
    price DECIMAL(12, 2), 
    description VARCHAR(250), 
    year INT, 
    FOREIGN KEY (id_ubication) REFERENCES ubication(id_ubication) 
);

CREATE TABLE status_property (
    id INT PRIMARY KEY AUTO_INCREMENT, 
    property_id INT NOT NULL, 
    status_id INT NOT NULL, 
    update_date DATETIME NOT NULL, 
    FOREIGN KEY (property_id) REFERENCES property(property_id), 
    FOREIGN KEY (status_id) REFERENCES status(status_id) 
);

CREATE TABLE user_likes (
    user_id INT, 
    property_id INT, 
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, 
    PRIMARY KEY (user_id, property_id), 
    FOREIGN KEY (user_id) REFERENCES users(user_id), 
    FOREIGN KEY (property_id) REFERENCES property(property_id) 
);