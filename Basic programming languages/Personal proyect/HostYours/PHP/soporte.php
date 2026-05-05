<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $nombre  = htmlspecialchars($_POST['nombre']);
    $email   = htmlspecialchars($_POST['email']);
    $asunto  = htmlspecialchars($_POST['asunto']);
    $mensaje = htmlspecialchars($_POST['mensaje']);

    echo "<h1>Ticket de Soporte Recibido</h1>";
    echo "<p>Hola <strong>" . $nombre . "</strong>, hemos recibido tu consulta sobre <strong>" . $asunto . "</strong>.</p>";
    
    echo "<div style='border: 1px solid #ccc; padding: 15px; background-color: #f9f9f9;'>";
    echo "<h3>Resumen de tu mensaje:</h3>";
    echo "<p><em>" . nl2br($mensaje) . "</em></p>";
    echo "</div>";

    echo "<p>Te responderemos lo antes posible al correo: <strong>" . $email . "</strong></p>";
    
    echo "<br><a href='../HTML/Pagina.html'>Volver al inicio</a>";

} else {
    echo "No se han recibido datos.";
}
?>