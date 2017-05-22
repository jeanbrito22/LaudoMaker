$(document).ready(function(){

    // Efeito na opção de pragas.
    $("#estado_embalagem").hide(0);
		$("#sim_embalagem, #nao_embalagem").click(function (){
			if(this.id == 'sim_embalagem'){
				$("#estado_embalagem").show(500);
			}else{
				$("#estado_embalagem").hide(500);
			}
		});

		$("#info-pragas").hide();
		$("#sim_praga, #nao_praga").click(function (){
			if(this.id =='sim_praga'){
				$("#info-pragas").show(500);
				$("#text-name, #text-species, #text-gender").hide();
				$("#text-family, #text-order, #text-class").hide();

				$("#classe, #ordem, #familia, #genero, #especie, #popular-name").click(function (){
					if(this.id == 'popular-name'){
						$("#text-name").show(500);
					}else{
						$("#text-name").hide(500);
					}

					if (this.id == 'especie') {
						$("#text-species").show(500);
					}else{
						$("#text-species").hide(500);
					}

					if (this.id == 'genero'){
						$("#text-gender").show(500);
					}else{
						$("#text-gender").hide(500);
					}

					if (this.id == 'familia'){
						$("#text-family").show(500);
					}else{
						$("#text-family").hide(500);
					}

					if (this.id == 'ordem'){
						$("#text-order").show(500);
					}else{
						$("#text-order").hide(500);
					}

					if (this.id == 'classe'){
						$("#text-class").show(500);
					}else{
						$("#text-class").hide(500);
					}
				});

			}else{
				$("#info-pragas").hide(500);
			}
		});

    //Validando o formulário.
	$("#info_form").bootstrapValidator({
		feedbackIcons: {
			valid: 'glyphicon glyphicon-ok',
			invalid: 'glyphicon glyphicon-remove',
			validating: 'glyphicon glyphicon-refresh'

		},
		fields: {
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
					message: 'Por favor, digite o CNPJ do cliente.'

				}
			}
		},
		    produtos_cliente: {
			    validators: {
				    stringLength: {
					    min: 2,
					    message: 'Por favor, digite mais de 2 caracteres.	'
				    },
				    notEmpty: {
					    message: 'Por favor, digite ao menos 1 produto'
				    }
			    }
		    },
		    qtd_produtos: {
			    validators: {
				    integer: {
					    message: 'Digite um numero válido.'
				    },
				    notEmpty: {
					    message: 'Digite a quantidade de produtos.'
				    }
			    }
		    },
		    num_chamado: {
		        validators: {
		            integer: {
		                message: 'Digite um numero válido.'
		            },
		            notEmpty: {
		                message: 'Digite o numero do chamado.'
		            }
		        }
		    },

		    comentario: {
			    validators: {
				    stringLength: {
					     min: 10,
					    max: 200,
					    message:'Por favor, digite no minimo 10 caracteres e no maximo 200.'
				    },
				    notEmpty: {
					    message: 'Por favor, escreva a conclusão sobre a análise.'
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