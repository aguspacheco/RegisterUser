export function borrar(clase) {
    const formulario = document.getElementById(`formulario${clase}`);
    formulario.reset();
}