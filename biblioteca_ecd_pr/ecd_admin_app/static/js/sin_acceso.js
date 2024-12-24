//volver al login
document.getElementById("btn_volverLogin").addEventListener("click", function(event) {
    event.preventDefault();

    //sweetalert de carga
    Swal.fire({
        title: "Cargando...",
        text: "Redirigiendo a la página inicial",
        icon: "info",
        allowOutsideClick: false,
        showConfirmButton: false,
        timer: 2000,
        didOpen: () => {
            Swal.showLoading();
        }
    }).then((result) => {
        if (result.dismiss === Swal.DismissReason.timer) {
            window.location.href = "/biblioteca_admin/"
        }
    });
});
