document.addEventListener('DOMContentLoaded', function() {
    const editarBoton = document.getElementById('editar-btn');
    const guardarBoton = document.getElementById('guardar-btn');
    const usuarioInput = document.getElementById('usuario-input');
    const emailInput = document.getElementById('email-input');

    function getCsrfToken() {
        return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    }

    function habilitarEdicion() {
        usuarioInput.disabled = false;
        emailInput.disabled = false;
        guardarBoton.disabled = false;
        editarBoton.disabled = true;
    }

    function deshabilitarEdicion() {
        usuarioInput.disabled = true;
        emailInput.disabled = true;
        guardarBoton.disabled = true;
        editarBoton.disabled = false;
    }

    function enviarDatosActualizados () {
        const datosActualizados = {
            username: usuarioInput.value,
            email: emailInput.value
        }
    
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
    
    editarBoton.addEventListener('click', habilitarEdicion);
    guardarBoton.addEventListener('click', enviarDatosActualizados);
});