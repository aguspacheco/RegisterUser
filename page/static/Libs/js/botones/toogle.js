function visualizarPass(abrirOjoUrl, cerrarOjoUrl   ) {
    var passwordInput = document.getElementById("id_contraseña");
    var passwordType = passwordInput.getAttribute("type");
    var toggleIcon = document.getElementById("toggle-icon");
    
    if (passwordType === "password") {
        passwordInput.setAttribute("type", "text");
        toggleIcon.src = abrirOjoUrl;
        toggleIcon.alt = "Abrir Ojo"
    } else {
        passwordInput.setAttribute("type", "password");
        toggleIcon.src = cerrarOjoUrl;
        toggleIcon.alt = "Cerrar Ojo"
    }
}
