DROP PROCEDURE IF EXISTS CalcularBonos;

DELIMITER //

CREATE PROCEDURE CalcularBonos()
BEGIN
    DECLARE v_id INT;
    DECLARE v_sal FLOAT;
    DECLARE v_dep VARCHAR(50);
    DECLARE v_bono FLOAT;
    DECLARE fin INT DEFAULT 0;

    DECLARE cur CURSOR FOR 
        SELECT emp_no, salario, dnombre FROM empleados JOIN departamentos USING (dep_no);
    
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = 1;

    OPEN cur;
    FETCH cur INTO v_id, v_sal, v_dep;

    WHILE fin = 0 DO

        IF v_dep = 'VENTAS' AND v_sal < 30000 THEN
            SET v_bono = v_sal * 0.03;
        ELSEIF v_dep = 'INVESTIGACION' AND v_sal < 250000 THEN
            SET v_bono = v_sal * 0.10;
        ELSEIF v_dep = 'INVESTIGACION' AND v_sal >= 250000 THEN
            SET v_bono = v_sal * 0.05;
        ELSE
            SET v_bono = v_sal * 0.01;
        END IF;


        INSERT INTO historial_bonos (emp_no, bono) VALUES (v_id, v_bono);
        UPDATE empleados SET salario = salario + v_bono WHERE emp_no = v_id;

        FETCH cur INTO v_id, v_sal, v_dep;
    END WHILE;

    CLOSE cur;
END //

DELIMITER ;