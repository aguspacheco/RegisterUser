// obtiene referencias a los elementos del DOM
document.addEventListener('DOMContentLoaded', function() {
    const editarBoton = document.getElementById('editar-btn');
    const guardarBoton = document.getElementById('guardar-btn');
    const usuarioInput = document.getElementById('usuario-input');
    const emailInput = document.getElementById('email-input');

    // obtiene el token CSRF del meta tag en el documento
    function getCsrfToken() {
        return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    }

    // habilita la edición en los campos de entrada y botones
    function habilitarEdicion() {
        usuarioInput.disabled = false;
        emailInput.disabled = false;
        guardarBoton.disabled = false;
        editarBoton.disabled = true;
    }

    // deshabilita la edición en los campos de entrada y botones
    function deshabilitarEdicion() {
        usuarioInput.disabled = true;
        emailInput.disabled = true;
        guardarBoton.disabled = true;
        editarBoton.disabled = false;
    }

    // envia los datos actualizados al servidor
    function enviarDatosActualizados () {
        // crea un objeto con los datos actuales de los campos de entrada
        const datosActualizados = {
            username: usuarioInput.value,
            email: emailInput.value
        }
        // envía los datos al servidor usando la API Fetch.
        fetch('/update-user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify(datosActualizados)
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la respuesta de la red');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert('Información actualizada con éxito.');
                deshabilitarEdicion();
            } else {
                alert('Error al actualizar la información.');
            }
        })
        .catch(error => {
            console.error('Hubo un problema con la operación fetch', error);
        });
    }
    
    // listeners para manejar clics
    editarBoton.addEventListener('click', habilitarEdicion);
    guardarBoton.addEventListener('click', enviarDatosActualizados);
});