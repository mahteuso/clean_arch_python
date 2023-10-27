CREATE DATABASE IF NOT EXISTS arch_clean;

CREATE TABLE IF NOT EXISTS `arch_clean`.`users`(
    id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    PRIMARY KEY (id)
);