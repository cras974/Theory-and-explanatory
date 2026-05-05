/*2.  Crear una función que calcule el perímetro de la casa.*/

DROP FUNCTION IF EXISTS perimetro;

DELIMITER //

CREATE FUNCTION perimetro (p_largo int,p_ancho int)
RETURNS int
DETERMINISTIC

BEGIN

	RETURN (p_largo+p_ancho * 2);

END //

DELIMITER ;