/*Realiza un procedimiento MostrarMejorVendedor que muestre el nombre del  vendedor con más comisión.*/

DROP PROCEDURE IF EXISTS MostrarMejorVendedor;

DELIMITER //

CREATE PROCEDURE MostrarMejorVendedor ()

BEGIN

	SELECT emp_no,COMISION FROM empleados
            ORDER BY COMISION ASC;

END //

DELIMITER ;