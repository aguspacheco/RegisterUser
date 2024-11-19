function visualizarPass() {
    var passwordInput = document.getElementById("id_contraseña");
    var toggleIcon = document.getElementById("toggle-icon");
    
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleIcon.src = "/static/images/abrirojo.png";
    } else {
        passwordInput.type = "password";
        toggleIcon.src = "/static/images/cerrarojo.png";
    }
}
