CREATE SCHEMA `habi_db` ;
USE habi_db;

DROP TABLE IF EXISTS status_history;
DROP TABLE IF EXISTS property;
DROP TABLE IF EXISTS status;

CREATE TABLE status (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE property (
    id INT PRIMARY KEY AUTO_INCREMENT,
    address VARCHAR(255),
    city VARCHAR(100),
    price DECIMAL(12, 2),
    description TEXT,
    year INT
);

CREATE TABLE status_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    property_id INT,
    status_id INT,
    update_date DATETIME,
    FOREIGN KEY (property_id) REFERENCES property(id),
    FOREIGN KEY (status_id) REFERENCES status(id)
);