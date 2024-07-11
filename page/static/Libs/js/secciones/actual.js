import { borrar } from "../botones/borrar.js";

const cancelarBtn = document.getElementById("cancelar.btn");
cancelarBtn.addEventListener("click", () => {
    borrar("Actual");
})