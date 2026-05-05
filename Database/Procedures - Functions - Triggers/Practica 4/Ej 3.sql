DROP TRIGGER IF EXISTS trigger_guardar_alumnos_eliminados;

DELIMITER //

CREATE TRIGGER trigger_guardar_alumnos_eliminados
AFTER DELETE ON alumnos
FOR EACH ROW
BEGIN
    INSERT INTO log_alumnos_eliminados (id_alumno,fecha_hora,nombre,apellido1,apellido2,email)
    VALUES (OLD.id,NOW(),OLD.nombre,OLD.apellido1,OLD.apellido2,OLD.email);
END //

DELIMITER ;