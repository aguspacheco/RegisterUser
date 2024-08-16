const inputs = document.querySelectorAll('input[type="number"]');

inputs.forEach(input => {
  input.addEventListener('input', () => {
    if (!/^\d+$/.test(input.value)) {
      input.value = '';
    }
  });
}); 