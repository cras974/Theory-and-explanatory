/*Haz una función llamada DevolverCodDept que reciba el nombre de un departamento y devuelva su código.*/

DROP FUNCTION DevolverCodDept
DELIMITER //

CREATE FUNCTION DevolverCodDept (depa varchar(50))
RETURNS INT
DETERMINISTIC
BEGIN

	DECLARE num_dep INT;

	SET num_dep = (SELECT dep_no
    FROM departamentos
    WHERE dnombre = depa);

	RETURN num_dep;

END //
DELIMITER ;

select empleados.DevolverCodDept('CONTABILIDAD');
