DELIMITER //

CREATE PROCEDURE crear_lista_emails_alumnos (OUT p_lista_emails TEXT)
BEGIN
    SELECT GROUP_CONCAT(email SEPARATOR ';') 
    INTO p_lista_emails
    FROM alumno;
END //

DELIMITER ;

CALL crear_lista_emails_alumnos(@mi_lista);

SELECT @mi_lista AS "Lista final";