document.addEventListener('DOMContentLoaded', function() {
    const editarBoton = document.getElementById('editar-btn');
    const guardarBoton = document.getElementById('guardar-btn');
    const usuarioInput = document.getElementById('usuario-input');
    const emailInput = document.getElementById('email-input');

    function getCsrfToken() {
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        return csrfToken;
    }

    editarBoton.addEventListener('click', function() {
        usuarioInput.disabled = false;  
        emailInput.disabled = false;
        guardarBoton.disabled = false;
        editarBoton.disabled = true;
    });

    guardarBoton.addEventListener('click', function() {
        const actualizarUsuario = usuarioInput.value;
        const actualizarEmail = emailInput.value;
    
        fetch('/update-user/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCsrfToken()
            },
            body: JSON.stringify({
                username: actualizarUsuario,
                email: actualizarEmail
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                alert('Información actualizada con éxito.');
                usuarioInput.disabled = true;
                emailInput.disabled = true;
                guardarBoton.disabled = true;
                editarBoton.disabled = false;
            } else {
                alert('Error al actualizar la información.');
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    });
});       
