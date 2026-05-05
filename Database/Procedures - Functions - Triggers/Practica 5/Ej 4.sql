/*PROCEDIMIENTOS

4.Construir un procedimiento que almacene en la tabla casa ya con la información calculada (llame a las funciones necesarias). 

Tenga en cuenta lo siguiente para llamar la función que calcula el valor de la casa primero debe  buscar  el valor guardado en valor metro.*/

DROP PROCEDURE IF EXISTS almacenar

DELIMITER //

CREATE PROCEDURE almacenar(IN n_largo int, IN n_ancho int, IN n_valor int)

BEGIN
	
    DECLARE n_precio int;
	DECLARE n_area int;
	DECLARE n_perimetro int;
    
	SET n_precio = (select test.valor(n_largo,n_ancho,n_valor));
    
    SET n_area = (select test.calcular_area(n_largo, n_ancho));
    
    SET n_perimetro = (select test.perimetro(n_largo,n_ancho));
   
	INSERT INTO casa (largo,ancho,area,valor,perimetro)
	VALUES (n_largo,n_ancho, n_area,n_precio,n_perimetro);

END //

DELIMITER ;

SELECT * FROM casa;