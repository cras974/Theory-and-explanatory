<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $usuario    = htmlspecialchars($_POST['usuario']);
    $email      = htmlspecialchars($_POST['email']);
    $contrasena = htmlspecialchars($_POST['contrasena']);
    $telefono   = htmlspecialchars($_POST['telefono']);
    $nacimiento = htmlspecialchars($_POST['nac']);

    // Respuesta de confirmación
    echo "<h1>¡Registro recibido!</h1>";
    echo "<p>Gracias por unirte, <strong>" . $usuario . "</strong>. Hemos recibido tus datos correctamente:</p>";
    
    echo "<ul>";
    echo "<li><strong>Email:</strong> " . $email . "</li>";
    echo "<li><strong>Teléfono:</strong> " . $telefono . "</li>";
    echo "<li><strong>Fecha de Nacimiento:</strong> " . $nacimiento . "</li>";
    echo "</ul>";

    echo "<p>La contraseña ha sido procesada de forma segura.</p>";
    echo "<br><a href='../HTML/Login.html'>Ir al inicio de sesión</a>";

} else {
    echo "Acceso no permitido.";
}
?>