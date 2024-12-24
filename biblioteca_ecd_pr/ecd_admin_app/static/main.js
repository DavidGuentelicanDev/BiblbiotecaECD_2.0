//logout
document.addEventListener("DOMContentLoaded", function() {
    const btnCerrarSesion = document.getElementById("btn_cerrarSesion");

    if (btnCerrarSesion) {
        btnCerrarSesion.addEventListener("click", function(event) {
            event.preventDefault();

            //sweetalert para confirmar
            Swal.fire({
                title: "Cerrar sesión",
                text: "¿Estás seguro de cerrar sesión?",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Cerrar Sesión",
                cancelButtonText: "Cancelar"
            }).then((result) => {
                if (result.isConfirmed) {
                    //csrf token
                    let csrfToken = document.querySelector("[name=csrfmiddlewaretoken]").value;

                    //llamar logout
                    fetch("/biblioteca_admin/adm_logout/", {
                        method: "POST",
                        headers: {
                            "X-CSRFToken": csrfToken,
                            "Content-Type": "application/json"
                        }
                    })
                    .then((response) => response.json())
                    .then((data) => {
                        console.log(data);

                        if (data.status === "success") {
                            //redirigir al login
                            Swal.fire({
                                title: "Cerrando sesión",
                                text: "Serás redirigido al inicio de sesión...",
                                icon: "success",
                                allowOutsideClick: false,
                                showConfirmButton: false,
                                timer: 2000,
                                didOpen: () => {
                                    Swal.showLoading();
                                }
                            }).then((result) => {
                                if (result.dismiss === Swal.DismissReason.timer) {
                                    window.location.href = "/biblioteca_admin/";
                                }
                            });
                        } else {
                            //error si no se pudo cargar el logout
                            Swal.fire({
                                title: "Error",
                                text: "No se pudo cerrar la sesión. Inténtalo nuevamente.",
                                icon: "error",
                                confirmButtonText: "Aceptar",
                            });
                        }
                    })
                    .catch((error) => {
                        console.error("Error:", error);
                        Swal.fire({
                            title: "Error",
                            text: "Ocurrió un problema al cerrar la sesión: " + error,
                            icon: "error",
                            confirmButtonText: "Aceptar",
                        });
                    });
                }
            });
        });
    }
});
