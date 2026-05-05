/*3.  Crear una función que calcule el valor de la casa teniendo en cuenta que recibe tres parámetros el largo, el ancho y el valor del metro cuadrado. 
El valor es el área por el valor del metro cuadrado.*/

DROP FUNCTION IF EXISTS valor;

DELIMITER //

CREATE FUNCTION valor(p_largo int,p_ancho int, p_valor int)
RETURNS int
DETERMINISTIC

BEGIN

	RETURN (p_largo*p_ancho*p_valor);

END //

DELIMITER ;