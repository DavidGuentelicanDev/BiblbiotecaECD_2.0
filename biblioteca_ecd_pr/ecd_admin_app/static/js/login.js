//Validacion de bootstrap para los campos vacios
(() => {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation')

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }

        form.classList.add('was-validated')
        }, false)
    });
})()

//recuperar contraseña
document.getElementById("link_recuperarContrasena").addEventListener("click", function(event) {
    event.preventDefault(); //evitar que la pagina se recargue

    Swal.fire({
        title: "Recuperar Contraseña",
        input: "email",
        inputLabel: "Ingresa tu correo electrónico de Biblioteca ECD",
        inputPlaceholder: "correo@bibliotecaecd.cl"
    });
});
