//importacion de la funcion borrar desde el archivo borrar.js
import { borrar } from "./borrar.js";

//Codigo que se ejecuta cuando se carga el contenido
document.addEventListener("DOMContentLoaded", function () {
    const btnCancelar = document.getElementById("cancelar-btn");

    //Llama a la funcion borrar para cada formulario
    btnCancelar.addEventListener("click", function () {
        borrar("Anterior");
        borrar("Actual");
        borrar("Antecedente");
        borrar("Persona");
        borrar("Tomo");
        borrar("Matricula");

        const labels = document.querySelectorAll(".label-active");
        labels.forEach((label) => {
            label.classList.remove(" label-active");
        });    
    });
});

//Espera a que todo el contendio del HTML se cargue antes de ejecutar el codigo y selecciona todos los elementos input.
document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll('input[type="number"], input[type="text"]');

    //Agrega un evento se clickea un label
    inputs.forEach((input) => {
        input.addEventListener("focus", function () {
            this.previousElementSibling.classList.add("label-active");
        });

    //Agrega un evento cuando se sale del label
    input.addEventListener("blur", function () {
        if (this.value === "") {
            this.previousElementSibling.classList.remove("label-active");
        }
    });

    //Verifica que la cadena no este vacia
    if (input.value != "") {
        input.previousElementSibling.classList.add("label-active")
    }
    })
})