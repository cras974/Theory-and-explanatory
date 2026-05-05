CREATE TABLE HISTORIAL_BONOS (
    emp_no INT,
    nombre VARCHAR(50),
    bonificacion DECIMAL(10, 2),
    fecha_registro DATE
);

DROP PROCEDURE IF EXISTS AplicarBonificaciones;

DELIMITER //

CREATE PROCEDURE AplicarBonificaciones()
BEGIN
    INSERT INTO HISTORIAL_BONOS (emp_no, nombre, bonificacion, fecha_registro)
    SELECT 
        emp_no, 
        apellido,
        CASE 
            WHEN dnombre = 'VENTAS' AND salario < 30000 THEN salario * 0.08
            WHEN dnombre = 'CONTABILIDAD' THEN 
                IF(salario < 25000, salario * 0.10, salario * 0.07)
            ELSE salario * 0.01
        END,CURDATE()
    FROM empleados 
    JOIN departamentos USING (dep_no);

    UPDATE empleados
    JOIN departamentos USING (dep_no)
    SET salario = salario + CASE 
        WHEN dnombre = 'VENTAS' AND salario < 30000 THEN salario * 0.08
        WHEN dnombre = 'CONTABILIDAD' THEN 
            IF(salario < 25000, salario * 0.10, salario * 0.07)
        ELSE salario * 0.01
    END;
END //

DELIMITER ;