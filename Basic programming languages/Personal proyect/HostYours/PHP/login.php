<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $usuario = htmlspecialchars($_POST['usuario']);
    $password = htmlspecialchars($_POST['contrasena']);

    echo "<h1>¡Datos recibidos con éxito!</h1>";
    echo "<p>El sistema ha detectado el intento de inicio de sesión.</p>";
    echo "<ul>";
    echo "<li><strong>Usuario/Email recibido:</strong> " . $usuario . "</li>";
    echo "<li><strong>Contraseña recibida:</strong> (Protegida por seguridad)</li>";
    echo "</ul>";
    
    echo "<br><a href='../HTML/Login.html'>Volver al formulario</a>";

} else {
    echo "Acceso no autorizado.";
}
?>