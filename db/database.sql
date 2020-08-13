CREATE DATABASE contacts;

CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT,
    nom_usuario VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50)NOT NULL,
    PRIMARY KEY(id_usuario)
);

CREATE TABLE contactos(
    id_contact INT AUTO_INCREMENT,
    nombre VARCHAR(50) NOT NULL,
    appellido VARCHAR(50),
    numero int NOT NULL,
    PRIMARY KEY(id_contact)
);

CREATE TABLE user_contac(
    id_usuario int,
    id_contact int,
    CONSTRAINT fk_usuario FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
    CONSTRAINT fk_contact FOREIGN KEY(id_contact) REFERENCES contactos(id_contact)
);

ALTER TABLE contactos
CHANGE COLUMN appellido apellido VARCHAR(50);

LOAD DATA LOCAL INFILE '/home/vidm/Documents/Projects/2020/list-contact/lista.csv' INTO TABLE contactos FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS; 

INSERT INTO contactos(nombre, apellido, numero)
VALUES ('Juan','Mora',63781122),
('Pedro','Perez',66785681),
('Lucas','Pargo',67481235),
('Alberto','Cierra',67845235);