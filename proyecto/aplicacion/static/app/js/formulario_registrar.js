// la funcion se ejecutará cuando se precione el botón de registrarse 
// de tipo submit
$("#registrar").submit(
    function(){
        // capturamos el formulario de registro por medio del id
        var $registrar = $("#registrar")

        //metodo creado para evitar los espacios en los inputs
        $.validator.addMethod("espacios", function(value, element){
            return value == ' ' || value.trim().length != 0
        }, "Espacios no son permitidos");

        // validamos el formulario de registro campo por campo
        if($registrar.length){
            $registrar.validate({
                rules:{
                    // pasamos los parametros de validacion
                    nombre: {
                        required: true,
                        espacios: true,
                        minlength: 4,
                        maxlength: 20,
                    },
                    correo: {
                        required: true,
                        email: true
                    },
                    pass:{
                        required: true,
                        espacios: true,
                        minlength: 5,
                        maxlength: 15
                    },
                    confirmar: {
                        required: true,
                        equalTo:'#inputPass',
                        espacios: true,
                        minlength: 5,
                        maxlength: 15
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
                    },
                    pass: {
                        required: 'Contraseña es obligatorio',
                        minlength: 'Debe tener un mínimo de 5 caracteres',
                        maxlength: 'Debe tener un máximo de 15 caracteres',
                    },
                    confirmar:{
                        required: 'Confirmación es obligatoria',
                        equalTo: 'Debe ingresar la misma contraseña'
                    }
                }

            })
        }
        // evitamos que el formulario se envíe por decfecto al apretar el boton
        // de registrarse
        event.preventDefault();
    }
);