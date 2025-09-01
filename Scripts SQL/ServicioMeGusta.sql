CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30),
    last_name VARCHAR(30),
    email VARCHAR(60) NOT NULL UNIQUE,
);

-- Tabla intermedia para registrar los "Me gusta"
CREATE TABLE user_likes (
    user_id INT,
    property_id INT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, property_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (property_id) REFERENCES property(property_id)
);