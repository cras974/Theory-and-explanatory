use empleados;
drop procedure if exists BuscarMasAntiguos;
delimiter //
create procedure BuscarMasAntiguos()
begin

declare p_dep_no int ;
declare final int default false;
declare cur_dpto cursor for 
select dep_no from departamentos;
declare continue handler for not found set final = true;

open cur_dpto;
	fin_bucle:loop
		fetch cur_dpto into p_dep_no;
		
        if final then
			leave fin_bucle;
		end if;
        
        select apellido,dnombre from empleados 
        join departamentos using (dep_no)
        where dep_no = p_dep_no
        order by fecha_alta desc limit 1;
        
	end loop;
    close cur_dpto;
end //
delimiter ;
call BuscarMasAntiguos();