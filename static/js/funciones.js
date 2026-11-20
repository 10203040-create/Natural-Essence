
// Identificar la página en la que se encuentra el usuario.
const paginaActual = window.location.pathname;

// Seleccionar los enlaces del menú.
const enlaces = document.querySelectorAll(".menu a");

// Marcar el enlace de la página actual.
enlaces.forEach((enlace) => {
    const direccion = enlace.getAttribute("href");

    if (direccion === paginaActual) {
        enlace.classList.add("activo");
    }
});
