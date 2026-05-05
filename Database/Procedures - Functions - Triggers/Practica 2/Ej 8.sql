DROP PROCEDURE IF EXISTS BorrarBecarios;

DELIMITER //

CREATE PROCEDURE BorrarBecarios()
BEGIN
    DECLARE v_dep INT;
    DECLARE fin INT DEFAULT 0;
    
    DECLARE cur_deps CURSOR FOR SELECT dep_no FROM departamentos;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin = 1;

    OPEN cur_deps;

    FETCH cur_deps INTO v_dep;

    WHILE fin = 0 DO
        
        DELETE FROM empleados 
        WHERE dep_no = v_dep 
        ORDER BY fecha_alt DESC 
        LIMIT 2;

        FETCH cur_deps INTO v_dep;
        
    END WHILE;

    CLOSE cur_deps;
END //

DELIMITER ;