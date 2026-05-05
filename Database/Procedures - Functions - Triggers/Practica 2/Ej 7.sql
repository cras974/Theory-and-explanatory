/*Realiza un procedimiento RecortarSueldos que recorte el sueldo un 20% a los empleados cuyo nombre empiece por la letra que recibe como parámetro.*/
DROP PROCEDURE IF EXISTS RecortarSueldos;

DELIMITER //

CREATE PROCEDURE RecortarSueldos(p_letra CHAR(1))
BEGIN
    DECLARE v_id INT;
    DECLARE fin INT DEFAULT 0;
    
    DECLARE cur CURSOR FOR 
        SELECT emp_no FROM empleados WHERE apellido LIKE CONCAT(p_letra, '%');
        
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = 1;

    OPEN cur;

    bucle: LOOP
        FETCH cur INTO v_id;
        
        IF fin = 1 THEN 
            LEAVE bucle; 
        END IF;

        UPDATE empleados SET salario = salario * 0.8 WHERE emp_no = v_id;
    END LOOP;

    CLOSE cur;
END //

DELIMITER ;