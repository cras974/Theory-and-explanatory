USE EMPLEADOS;
DROP TRIGGER IF EXISTS NO_MODIFICAR_EMP_NO;

DELIMITER //

CREATE TRIGGER NO_MODIFICAR_EMP_NO
BEFORE UPDATE ON EMPLEADOS
FOR EACH ROW
BEGIN
    
        if OLD.emp_no != NEW.emp_no THEN 
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'ERRORRRRRR: No se puede modificar el EMP_NO';
		end if;
        -- 2. Si el salario sube más del 10%
        if NEW.salario > (OLD.salario * 1.10) THEN 
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'errrorrrrr: El aumento supera el 10%';
		end if;

END//

DELIMITER ;

UPDATE EMPLEADOS
SET emp_no = 7368
WHERE EMP_NO = 7369;
