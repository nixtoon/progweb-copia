// la funcion se ejecutará cuando se precione el botón de iniciar sesión 
// de tipo submit
$("#main").submit(
    function () {
        // capturamos el formulario de registro por medio del id
        var $iniciar = $("#main")

        //metodo creado para evitar los espacios en los inputs
        $.validator.addMethod("espacios", function (value, element) {
            return value == ' ' || value.trim().length != 0
        }, "Espacios no son permitidos");

        // validamos el formulario de registro campo por campo
        if ($iniciar.length) {
            $iniciar.validate({
                // pasamos los parametros de validacion
                rules: {
                    email: {
                        required: true,
                        email: true
                    },
                    password: {
                        required: true,
                        espacios: true,
                        minlength: 5,
                        maxlength: 15
                    }
                },
                // escribimos los mensajes para que aparezcan cuando los campos
                // sean incorrectos
                messages: {
                    email: {
                        required: 'Correo es obligatorio',
                    },
                    password: {
                        required: 'Contraseña es obligatorio',
                        minlength: 'Debe tener un mínimo de 5 caracteres',
                        maxlength: 'Debe tener un máximo de 15 caracteres',
                    }
                }

            })
        }
        // evitamos que el formulario se envíe por decfecto al apretar el boton
        // de iniciar
        event.preventDefault();
    }
);