DROP TRIGGER IF EXISTS trigger_guardar_email_after_update;

DELIMITER //

CREATE TRIGGER trigger_guardar_email_after_update
AFTER UPDATE ON alumnos
for each row
BEGIN

	if old.email != new.email then
		insert into log_cambios_email (id_alumno,fecha_hora,old_email,new_email) 
        VALUES (1,now(),old.email,new.email);
	
    end if;

END //

DELIMITER ;