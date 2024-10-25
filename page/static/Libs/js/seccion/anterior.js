import { borrar } from "../botones/borrar.js";

const borrarBtn = document.getElementById("borrar-btn");
borrarBtn.addEventListener("click", () => {
    borrar("Anterior");
});