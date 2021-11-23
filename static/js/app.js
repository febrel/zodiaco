const year_HTML = document.querySelector("#yearInput");
const months_HTML = document.querySelector("#monthInput");
const day_HTML = document.querySelector("#dayInput");

// Objeto date
let fecha = new Date();
let yearMax = fecha.getFullYear();
let yearMin = yearMax - 100;
let months = fecha.getMonth();
let day = fecha.getDate();


// Variables Bandera
let bandera1 = false;
let bandera2 = false;
let bandera3 = false;

console.log("Mes", months);
console.log("Dia", day);

// Arreglo
let meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"];
let diasMeses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];


eventListener();

function eventListener() {
    llenarSelectYears();
    llenarSelectMonths();
    llenarSelectDay();

}

// Llena select de year
function llenarSelectYears() {

    for (let y = yearMax; y > yearMin; y--) {
        const yearOpciones = document.createElement("option");


        yearOpciones.value = y;
        yearOpciones.textContent = `
            ${y} 
        `;

        // Insertar en HTML
        year_HTML.appendChild(yearOpciones); // Agrega las opciones al select
    }
}

// Llena select de meses
function llenarSelectMonths() {

    for (const iterator of meses) {
        const monthsOpciones = document.createElement("option");

        monthsOpciones.value = iterator;
        monthsOpciones.textContent = `
            ${iterator}
        `;

        // Insertar en HTML
        months_HTML.appendChild(monthsOpciones); // Agrega las opciones al select

    }

}


// Llena select de meses
function llenarSelectDay() {

    for (let index = 1; index <= 31; index++) {

        const dayOpciones = document.createElement("option");

        dayOpciones.value = index;
        dayOpciones.textContent = `
            ${index}
        `;

        // Insertar en HTML
        day_HTML.appendChild(dayOpciones); // Agrega las opciones al select

    }

}