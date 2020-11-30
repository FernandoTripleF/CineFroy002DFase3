

function valorEntrada()
{
  var nom= document.getElementById('nombre').value;
  var cantidad = parseInt(document.getElementById('cantidad').value);
  var valor = parseInt(cantidad)*2500;
  alert('Sus entradas fueron enviadas a su correo electronico. Tienen un valor de ' +  valor + ' a nombre de ' + nom);
}

$(function() 
      {
        $("#mi-formulario").validate({
             rules: {
                    email: {
                        required: true,
                        email: true
                    },  
                    nombre: "required",
                    apellido: "required",
                    fecha: "required",
                    email: "required",
                    password2: {
                        required: true,
                        equalTo: "#password"
                    }   
                }, //rules
            messages: {
                nombre:{
                    required: 'Ingrese su nombre',
                    nombre: 'Formato de nombre incorrecto'
                },
                email: {
                    required: 'Ingresa tu correo electrónico',
                    email: 'Formato de correo no válido'
                },
                apellido:{
                  required: 'Ingrese su apellido',
                  apellido: 'Formato de apellido incorrecto'
                },
                fecha:{
                    required: 'Seleccione una fecha válida',
                    min: 'Fecha no corresponde'
                }
            }//messages
        }); //$('#mi-formulario').validate
    }); //function

    $(function () {
        $('[data-toggle="popover"]').popover()
      })

      $(function () {
        $('.example-popover').popover({
          container: 'body'
        })
      })