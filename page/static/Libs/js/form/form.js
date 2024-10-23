    // verifica que el código se ejecute solo después de que el documento este cargado  
    $(document).ready(function() {
        $(".close").click(function() {
            $(this).parent().fadeOut();
        });
    });

    