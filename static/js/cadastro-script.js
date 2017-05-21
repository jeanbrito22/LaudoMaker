$(document).ready(function(){


    //Validando o formulário.
	$("#info_form").bootstrapValidator({
        feedbackIcons: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            cliente: {
                validators: {
                        stringLength: {
                        min: 2,
                    },
                        notEmpty: {
                        message: 'Por favor digite seu nome'
                    }
                }
            },
             cnpj: {
                validators: {
                     integer: {
                        message: 'Por favor, digite apenas numeros.'
                    },
                    stringLength: {
                    	min: 14,
                    	max: 14,
                       message: 'Por favor, digite um CNPJ valido sem sinais.'
                    },
                    notEmpty: {
                    	message: 'Por favor, digite o CNPJ do cliente'
                    }
                }
            },
            email: {
                validators: {
                    notEmpty: {
                        message: 'Por favor digite seu endereco de email'
                    },
                    emailAddress: {
                        message: 'Por favor digite um email valido'
                    }
                }
            },	
            endereco: {
                validators: {
                     stringLength: {
                        min: 8,
                        message: 'Por favor, digite mais de 8 caracteres'
                    },
                    notEmpty: {
                        message: 'Por favor, digite seu endereco.'
                    }
                }
            },
            estado: {
                validators: {
                    notEmpty: {
                        message: 'Por favor selecione seu estado'
                    }
                }
            },
            cep: {
                validators: {
                    notEmpty: {
                        message: 'Por favor digite seu CEP'
                    },
                    zipCode: {
                        country: 'BR',
                        message: 'Por favor digite um CEP valido'
                    }
                }
            }
            }
        })



		    //Se a validação der certo, mostre a mensagem de sucesso.
            .on('success.form.bv', function(e) {
                $('#success_message').slideDown({ opacity: "show" }, "slow")
        });
});