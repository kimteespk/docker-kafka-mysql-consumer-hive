create database if not EXISTS testdb;

USE testdb;

CREATE TABLE IF NOT EXISTS testdb2 (
    id INT(10),
    name VARCHAR(50),
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX modified_index (modified)
);

GRANT ALL PRIVILEGES ON testdb.* TO 'confluent'@'%';

use testdb;
INSERT INTO testdb2 (id, name) VALUES (1, 'kimtee');
INSERT INTO testdb2 (id, name) VALUES (1, 'kimtee2'),(2, 'rambo2');