-- Create new database and add table to it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities
(id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
state_id INT NOT NULL,
name VARCHAR(256) NOT NULL,
INDEX state_id (state_id),
FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id));
