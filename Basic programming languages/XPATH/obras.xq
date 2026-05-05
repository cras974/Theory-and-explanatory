(: Todos los nodos museo 
//museo

/obras/obra

//obra/@pais

Obra del pais España

//obra[@pais="España"]

Titulo cuya obra esta visible

//museo[@visible="true"]/../titulo

//museo[@visible="true"]/../titulo/string()

Funciones XPATH que manejan cadenas de caracteres

//obra/titulo/string() Todos los titulos (Solo el texto) de todas las obras

//obra/@pais/string() Todos los valores (Solo el texto) de los atributos pais de los nodos obra

//obra/museo/text() Hace lo mismo que strig, solo funciona con nodos :)