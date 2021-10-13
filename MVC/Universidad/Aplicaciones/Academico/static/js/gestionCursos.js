(function () {

    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn =>{
        btn.addEventListener('click', (e)=>{
            const confirmacion = confirm('¿Seguro quieres eliminar el curso?');
            if(!confirmacion){
                e.preventDefault();
            }
        });
    });

})();