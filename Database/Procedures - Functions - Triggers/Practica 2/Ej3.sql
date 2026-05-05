/*Realiza una función llamada CalcularCosteSalarial que reciba un nombre de departamento y devuelva la suma de los salarios y comisiones de los empleados de dicho departamento.*/

DROP FUNCTION IF EXISTS CalcularCosteSalarial;

DELIMITER //

CREATE FUNCTION CalcularCosteSalarial (nombre_dep varchar(50))
RETURNS int
DETERMINISTIC

BEGIN

	DECLARE TOTAL int;
    
    SET TOTAL = (SELECT SUM(SALARIO + COALESCE(COMISION,0)) FROM empleados
				JOIN departamentos USING (dep_no)
                WHERE dnombre = nombre_dep);
	
    RETURN TOTAL;

END //
DELIMITER ;

select empleados.CalcularCosteSalarial('INVESTIGACION');
