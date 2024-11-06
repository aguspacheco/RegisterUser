document.addEventListener("DOMContentLoaded", function() {
    const hoy = new Date().toISOString().split('T')[0];

    const fechaJuridicos = document.getElementById("fechaJuridicos");
    const errorFechaJuridicos = document.getElementById("errorFechaJuridicos");
    const fechaMatricula = document.getElementById("fechaMatricula");
    const errorFechaMatricula = document.getElementById("errorFechaMatricula");

    function validarFecha(input, errorElement) {
        if (input.value > hoy) {
            errorElement.style.display = "inline";
            input.setCustomValidity("Fecha no válida");
        } else {
            errorElement.style.display = "none";
            input.setCustomValidity("");
        }
    }
    
    fechaJuridicos.addEventListener("input", function () {
        validarFecha(fechaJuridicos, errorFechaJuridicos);
    });

    fechaMatricula.addEventListener("input", function () {
        validarFecha(fechaMatricula, errorFechaMatricula);
    });
});