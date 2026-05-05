DELIMITER //
DROP PROCEDURE IF EXISTS pais_fab//
CREATE PROCEDURE pais_fab (IN p_pais varchar(30))
BEGIN
	SELECT COUNT(*) AS "Numero de fabricantes"
		FROM fabricantes
		WHERE pais=p_pais;
END //
DELIMITER ;

call almacen.pais_fab('ESPAÑA');
