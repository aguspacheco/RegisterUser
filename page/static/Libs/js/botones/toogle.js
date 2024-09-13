function visualizarPass() {
    var passwordInput = document.getElementById("id_contraseña");
    var passwordType = passwordInput.getAttribute("type");
    
    if (passwordType === "password") {
        passwordInput.setAttribute("type", "text");
    } else {
        passwordInput.setAttribute("type", "password");
    }
}
