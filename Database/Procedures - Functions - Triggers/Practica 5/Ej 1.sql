/*FUNCIONES

Crea dos tablas:

·       CASA (código, descripción, largo, ancho, área, valor, perímetro)

·       VALORMETRO (valor)

1.  Crear una función que calcule el área de la casa.*/

CREATE TABLE IF NOT EXISTS CASA(
codigo int primary key,
descripcion varchar(200),
largo int,
ancho int,
area int,
valor int,
perimetro int);

CREATE TABLE IF NOT EXISTS VALORMETRO(
valor int);

DROP FUNCTION IF EXISTS calcular_area;

DELIMITER //

CREATE FUNCTION calcular_area(p_largo int,p_ancho int)
returns int
deterministic

BEGIN

	RETURN (p_largo * p_ancho);
    
END //

DELIMITER ;