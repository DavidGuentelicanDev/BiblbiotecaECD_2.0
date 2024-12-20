//Validacion de bootstrap para los campos vacios
(() => {
    'use strict'

    const forms = document.querySelectorAll('.needs-validation');

    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }

        form.classList.add('was-validated');
        }, false)
    });
})()

//recuperar contraseña
document.getElementById("link_recuperarContrasena").addEventListener("click", function(event) {
    event.preventDefault(); //evitar que la pagina se recargue

    Swal.fire({
        title: "Recuperar Contraseña",
        input: "text",
        inputLabel: "Ingresa tu correo electrónico de Biblioteca ECD",
        inputPlaceholder: "correo@bibliotecaecd.cl",
        confirmButtonText: "Enviar",
        showCancelButton: true,
        inputValidator: (value) => {
            //verificar si esta vacio
            if (!value) {
                return "Debes ingresar un correo electrónico";
            }

            //validar formato email personalizado
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                return "Por favor, ingresa un correo electrónico válido.";
            }
            //si todo esta ok, no hay mensaje
            return null;
        },
        preConfirm: (value) => {
            return new Promise((resolve) => {
                setTimeout(() => {
                    resolve(value)
                }, 500);
            });
        }
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire({
                icon: "success",
                title: "Correo enviado",
                text: `Se han enviado instrucciones al correo: ${result.value} para recuperar la contraseña`,
                confirmButtonText: "Aceptar"
            });
        }
    });
});

//boton de ojo para mostrar/ocultar contraseña
document.getElementById("btn_contrasena").addEventListener("click", function() {
    const contrasenaVisible = document.getElementById("txt_contrasena");
    const icono = document.getElementById("icon_contrasena");

    //alternar el tipo de texto entre password y text para invisible y visible respectivamente
    if (contrasenaVisible.type === "password") {
        contrasenaVisible.type = "text";
        icono.classList.remove("bi bi-eye-fill");
        icono.classList.add("bi bi-eye-slash-fill");
    } else {
        contrasenaVisible.type = "password";
        icono.classList.remove("bi bi-eye-slash-fill");
        icono.classList.add("bi bi-eye-fill");
    }
});
