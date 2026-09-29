// Cierra un mensaje flash al dar clic en su botón
document.querySelectorAll('.notification .delete').forEach(boton => {
    boton.addEventListener('click', () => boton.parentNode.remove());
});

// Pide confirmación antes de eliminar la cuenta
document.querySelectorAll('.form-eliminar').forEach(form => {
    form.addEventListener('submit', e => {
        if (!confirm('¿Seguro que quieres eliminar tu cuenta?')) {
            e.preventDefault();
        }
    });
});
