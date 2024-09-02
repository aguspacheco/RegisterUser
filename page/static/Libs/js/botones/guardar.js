document.getElementById('editar-btn').addEventListener('click', function() {
    document.getElementById('username').removeAttribute('readonly');
    document.getElementById('email').removeAttribute('readonly');
    document.getElementById('password').removeAttribute('readonly');
    document.getElementById('guardar-btn').removeAttribute('disabled');
});

document.getElementById('guardar-btn').addEventListener('click', function() {
    alert('Datos guardados correctamente');
});

