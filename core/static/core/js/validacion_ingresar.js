

$(document).ready(function () {
    // Mensajes de validación predeterminados en español
    $.extend($.validator.messages, {
        required: "Este campo es obligatorio.",
        email: "Por favor, ingrese un correo electrónico válido.",
        minlength: $.validator.format("Por favor, ingrese al menos {0} caracteres.")
    });

    // Método de validación para el correo electrónico
    $.validator.addMethod("validEmail", function (value, element) {
        var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return this.optional(element) || regex.test(value);
    }, "Por favor, ingrese un correo electrónico válido.");

    // Método de validación para la contraseña
    $.validator.addMethod("validPassword", function (value, element) {
        return this.optional(element) || value.length >= 8;
    }, "La contraseña debe tener al menos 8 caracteres.");

    // Configuración de la validación del formulario
    $("#formulario-ingreso").validate({
        rules: {
            correo: {
                required: true,
                email: true,
                validEmail: true
            },
            password: {
                required: true,
                validPassword: true
            }
        },
        messages: {
            correo: {
                required: "El correo electrónico es un campo requerido.",
                email: "Por favor, ingrese un correo electrónico válido.",
                validEmail: "Por favor, ingrese un correo electrónico válido."
            },
            password: {
                required: "La contraseña es un campo requerido.",
                validPassword: "La contraseña debe tener al menos 8 caracteres."
            }
        },
        highlight: function (element) {
            $(element).addClass("is-invalid").removeClass("is-valid");
        },
        unhighlight: function (element) {
            $(element).addClass("is-valid").removeClass("is-invalid");
        },
        submitHandler: function (form) {
            // Aquí puedes agregar la lógica para manejar el formulario cuando es válido
            alert("Formulario válido y enviado.");
            form.submit();
        }
    });
});
