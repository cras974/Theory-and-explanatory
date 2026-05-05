CREATE TABLE Cuenta (
    total INT DEFAULT 0
);
INSERT INTO Cuenta (total) SELECT COUNT(*) FROM empleados;

DROP TRIGGER IF EXISTS tr_aumentar_cuenta;

DELIMITER //

CREATE TRIGGER tr_aumentar_cuenta
AFTER INSERT ON empleados
FOR EACH ROW
BEGIN
    UPDATE Cuenta SET total = total + 1;
END //

DELIMITER ;

DROP TRIGGER IF EXISTS tr_disminuir_cuenta;

DELIMITER //

CREATE TRIGGER tr_disminuir_cuenta
AFTER DELETE ON empleados
FOR EACH ROW
BEGIN
    UPDATE Cuenta SET total = total - 1;
END //

DELIMITER ;