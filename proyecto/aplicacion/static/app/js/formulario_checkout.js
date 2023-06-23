// la funcion se ejecutará cuando se precione el botón de continuar
// de tipo submit
$("#continuar").submit(
    function(){
        // capturamos el formulario de compra por medio del id
        var $continuar = $("#continuar")

        //metodo creado para evitar los espacios en los inputs
        $.validator.addMethod("espacios", function(value, element){
            return value == ' ' || value.trim().length != 0
        }, "Espacios no son permitidos");

        // validamos el formulario de registro campo por campo
        if($continuar.length){
            $continuar.validate({
                rules:{
                    // parametros de validacion
                    nombre: {
                        required: true,
                        espacios: true,
                        minlength: 4,
                        maxlength: 20,
                    },
                    apellido: {
                        required: true,
                        espacios: true,
                        minlength: 4,
                        maxlength: 20,
                    },
                    correo: {
                        required: true,
                        email: true
                    }
                },

                // escribimos los mensajes para que aparezcan cuando los campos
                // sean incorrectos
                messages:{
                    nombre: {
                        required: 'Nombre es obligatorio',
                        minlength:'debe tener un mínimo de 4 caracteres',
                        maxlength:'debe tener un máximo de 20 caracteres',
                        text:'Solo se aceptan letras',
                    },
                    correo: {
                        required: 'Correo es obligatorio',
                    }
                }

            })
        }
        // evitamos que el formulario se envíe por decfecto al apretar el boton
        // de registrarse
        event.preventDefault();
    }
);