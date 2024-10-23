import { borrar } from "./borrar.js";

const cancelarBtn = document.getElementById("cancelar-btn");
cancelarBtn.addEventListener("click", () => {
    borrar("Antecedente");
});