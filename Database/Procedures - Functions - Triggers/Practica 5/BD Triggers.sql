CREATE DATABASE ejemplo;

CREATE TABLE persona(
codigo int primary key,
nombre varchar(100),
edad int);

CREATE TABLE nuevosdatos(
codigo int primary key,
cuando date,
tipo varchar(50));