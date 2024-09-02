  const formularios = [ 
    document.getElementById('formularioAntecedente'),
    document.getElementById('formularioPersona'),
    document.getElementById('formularioMatricula'),
    document.getElementById('formularioActual')
  ];

  const inputs = document.querySelectorAll('input[type="number"], input[type="text"], input[type="date"]');
  const selects = document.querySelectorAll('select');
  const botonEnviar = document.getElementById('enviar-btn');

  inputs.forEach(input => {
    input.addEventListener('input', () => {
      if (input.value.trim() !== '') {
        input.style.border = '';
        input.previousElementSibling.style.color = ''; 
      }
    });
  });

  selects.forEach(select => {
    select.addEventListener('change', () => {
      if (select.value.trim() !== '') {
        select.style.border = '';
        select.previousElementSibling.style.color = ''; 
      }
    });
  });

  botonEnviar.addEventListener('click', (e) => {
    e.preventDefault(); 

    const camposVacios = formularios.flatMap(verificarFormulario);

    if (camposVacios.length > 0) {
      alert('Por favor, complete todos los campos obligatorios.');
      camposVacios.forEach(campo => {
        campo.style.border = '1px solid #ef233c'; 
        campo.previousElementSibling.style.color = '#ef233c'; 
      });
    } else {
      alert('Formulario enviado correctamente');
    }
  });

  function verificarFormulario(formulario) {
    return Array.from(formulario.elements).filter(campo => campo.value.trim() === '');
  }