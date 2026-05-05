/*Realiza un procedimiento MostrarCostesSalariales que muestre los nombres de todos los departamentos y el coste salarial de cada uno de ellos y los introduzca en una nueva tabla llamada Costes. 
Incluir manejo de errores. Puedes usar la función del ejercicio 3.*/

CREATE TABLE IF NOT EXISTS Costes (
    nombre_dep VARCHAR(50),
    coste_total INT,
    fecha_calculo TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DROP PROCEDURE IF EXISTS MostrarCostesSalariales;

DELIMITER //

CREATE PROCEDURE MostrarCostesSalariales()
BEGIN
    DECLARE v_dnombre VARCHAR(50);
    DECLARE v_coste INT;
    DECLARE fin_cursor BOOLEAN DEFAULT FALSE;

    DECLARE cursor_deps CURSOR FOR SELECT dnombre FROM departamentos;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin_cursor = TRUE;
    
    DECLARE EXIT HANDLER FOR SQLEXCEPTION 
    BEGIN
        SELECT 'Error' AS MensajeError;
    END;

    TRUNCATE TABLE Costes;

    OPEN cursor_deps;

    bucle_deps: LOOP
        FETCH cursor_deps INTO v_dnombre;
        
        IF fin_cursor THEN
            LEAVE bucle_deps;
        END IF;

        SET v_coste = CalcularCosteSalarial(v_dnombre);

        INSERT INTO Costes (nombre_dep, coste_total) VALUES (v_dnombre, v_coste);
        
        SELECT v_dnombre AS 'Departamento', v_coste AS 'Coste Salarial';

    END LOOP;

    CLOSE cursor_deps;
    
    SELECT 'Proceso finalizado: Datos guardados en la tabla Costes.' AS Resultado;

END //

DELIMITER ;