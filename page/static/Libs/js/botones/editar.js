document.addEventListener('DOMContentLoaded', function() {
    const elements = {
        editarBoton: document.getElementById('editar-btn'),
        guardarBoton: document.getElementById('guardar-btn'),
        usuarioInput: document.getElementById('usuario-input'),
        emailInput: document.getElementById('email-input'),
        container: document.querySelector('.container')
    };

    function limpiarMensajesPrevios() {
        const mensajesPrevios = elements.container.querySelectorAll('.mensaje-exito, .mensaje-error');
        mensajesPrevios.forEach(msg => msg.remove()); 
    }
    
    function getCsrfToken() {
        return document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    }

    function toggleEdicion(habilitar) {
        const estado = !habilitar;
        elements.usuarioInput.disabled = estado;
        elements.emailInput.disabled = estado;
        elements.guardarBoton.disabled = estado;
        elements.editarBoton.disabled = habilitar;
    }

    function mostrarMensaje(mensaje, tipo) {
        limpiarMensajesPrevios();
        const mensajeDiv = document.createElement('div');
        mensajeDiv.className = tipo;
        mensajeDiv.textContent = mensaje;
        elements.container.appendChild(mensajeDiv)

        setTimeout(() => mensajeDiv.remove(), 2000);
    }

    function enviarDatosActualizados() {
        const datosActualizados = {
            username: elements.usuarioInput.value,
            email: elements.emailInput.value
        };

        fetch('/update-user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify(datosActualizados)
        })
        .then(response => {
            if (!response.ok) throw new Error('Error en la respuesta de la red');
            return response.json();
        })
        .then(data => {
            const tipoMensaje = data.success ? 'mensaje-exito' : 'mensaje-error';
            const mensaje = data.success ? 'Información actualizada con éxito.' : 'Error al actualizar la información.';
            mostrarMensaje(mensaje, tipoMensaje);
            if (data.success) toggleEdicion(false);
        })
        .catch(error => {
            console.error('Hubo un problema con la operación fetch', error);
            mostrarMensaje('Hubo un problema con la operación. Intenta nuevamente', 'mensaje-error');
        });
    }

    // listeners para manejar clics
    elements.editarBoton.addEventListener('click', () => toggleEdicion(true));
    elements.guardarBoton.addEventListener('click', enviarDatosActualizados);

    const volverBoton = document.getElementById('volver-btn');
    volverBoton.addEventListener('click', () => {
        window.history.back();
    });
});