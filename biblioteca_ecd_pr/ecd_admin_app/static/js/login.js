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

//recuperar contraseña con sweetalert2
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
                return "Debes ingresar un correo electrónico.";
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
                text: `Se han enviado instrucciones al correo: ${result.value} para recuperar la contraseña.`,
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

//login
document.addEventListener("DOMContentLoaded", function() {
    //constantes y variables del html
    const formulario = document.getElementById("form_loginAdm");
    let usuario = document.getElementById("txt_usuario");
    let contrasena = document.getElementById("txt_contrasena");

    //evento del envio del form
    formulario.addEventListener("submit", function(event) {
        event.preventDefault();

        if (!usuario.value.trim() || !contrasena.value.trim()) {
            console.log("Campos vacíos, no se envía la solicitud");
            return;
        }

        //obtener datos del form
        let datosFormulario = new FormData(formulario);
        let datos = Object.fromEntries(datosFormulario);

        //enviar datos con fetch
        fetch("adm_login/", {
            method: "POST",
            headers: {
                "X-CSRFToken": datosFormulario.get("csrfmiddlewaretoken"),
                'Content-Type': "application/json"
            },
            body: JSON.stringify(datos)
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if (data.status == "success") {
                //redirigir a la pagina principal de la app
                Swal.fire({
                    title: "Éxito",
                    text: "Login exitoso",
                    icon: "success",
                    confirmButtonText: "Aceptar"
                }).then(() => {
                    window.location.href = "home/";
                });
            } else {
                //error
                Swal.fire({
                    title: "Error",
                    text: data.message || "Credenciales inválidas",
                    icon: "error",
                    confirmButtonText: "Aceptar"
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            Swal.fire({
                title: "Error",
                text: "Ocurrió un problema al iniciar sesión",
                icon: "warning",
                confirmButtonText: "Aceptar"
            });
        });
    });
});
