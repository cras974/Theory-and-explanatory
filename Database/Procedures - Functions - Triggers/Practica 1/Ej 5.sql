DROP FUNCTION IF EXISTS calcular_años;
DELIMITER //
CREATE FUNCTION calcular_años (fecha date)
RETURNS INT
DETERMINISTIC
BEGIN

	DECLARE diferencia int;
    
    set diferencia = DATEDIFF(CURDATE(),fecha);
    
    RETURN diferencia / 365;

END //

DELIMITER ;

select procedimientos.calcular_años('2010-01-02');