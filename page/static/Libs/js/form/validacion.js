// Selecciona los inputs de tipo number
const inputs = document.querySelectorAll('input[type="number"]');

inputs.forEach(input => {
  input.addEventListener('input', () => {
    // Verifica si el valor ingresado es un numero positivo
    if (!/^\d+$/.test(input.value)) {
      input.value = '';
    }
  });
}); 