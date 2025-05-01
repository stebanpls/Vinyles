document.addEventListener("DOMContentLoaded", function () {
    const pagoModal = document.getElementById("pago-modal");
    const closePagoModal = document.querySelector(".close-pago-modal");
    const confirmarPagoButton = pagoModal.querySelector(".btn-success");
    const pagoButton = document.getElementById("pago-button");

    if (pagoButton) {
    pagoButton.addEventListener("click", function () {
        pagoModal.style.display = "block";
    });
    }

    closePagoModal.addEventListener("click", function () {
        pagoModal.style.display = "none";
    });

    window.addEventListener("click", function (event) {
        if (event.target === pagoModal) {
            pagoModal.style.display = "none";
        }
    });

    confirmarPagoButton.addEventListener("click", function () {
        alert("¡Pago confirmado!");
        pagoModal.style.display = "none";
    });
});
