    // verifica que el código se ejecute solo después de que el documento este cargado  
    $(document).ready(function() {
           // Asocia un evento de clic a los elementos con la clase "close"
        $(".close").click(function() {
            // Al hacer clic en el elemento con la clase "close", oculta el elemento padre
            $(this).parent().fadeOut();
        });
    });

    