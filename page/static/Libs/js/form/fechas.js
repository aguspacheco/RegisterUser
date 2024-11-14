document.addEventListener('DOMContentLoaded', function () {
    const juridicosInput = document.getElementById('fechaJuridicos');
    const matriculaInput = document.getElementById('fechaMatricula');
    const juridicosError = document.getElementById('juridicosError');
    const matriculaError = document.getElementById('matriculaError');

    const hoy = new Date().toISOString().split("T")[0];

    function validarDia(input, errorElement) {
        if (input.value > hoy) {
            errorElement.style.display = "inline";
        } else {
            errorElement.style.display = "none";
        }
    }

    juridicosInput.addEventListener('change', function () {
        validarDia(juridicosInput, juridicosError);
    });

    matriculaInput.addEventListener('change', function () {
        validarDia(matriculaInput, matriculaError);
    });

    document.getElementById('formularioTomo').addEventListener('submit', function (e) {
        let valid = true;

        if (!validarDia(juridicosInput, juridicosError)) {
            valid = false;
        }

        if (!valid) {
            e.preventDefault();
        }
    });

    document.getElementById('formularioMatricula').addEventListener('submit', function (e) {
        let valid = true;

        if (!validarDia(matriculaInput, matriculaError)) {
            valid = false;
        }

        if (!valid) {
            e.preventDefault();
        }
    });
});