from flask import Flask, render_template, request
from models import *

app = Flask(__name__)

#Pagina inicial
@app.route("/")
def index():
    return render_template("index.html")

#Funcoes para o laudo
@app.route("/laudo")
def laudoPage():
    return render_template("laudo.html")

@app.route('/laudo-success', methods=['POST'])
def getFormLaudo():
    cnpj = request.form['cnpj']
    produto = request.form['produtos_cliente']
    qtProduto = request.form['qtd_produtos']
    nChamado = request.form['num_chamado']
    opcaoEmbalagem = request.form['opcao_embalagem']
    estadoEmbalagem = 'N/A'
    conservacaoEmbalagem = 'N/A'
    opcaoPragas = request.form['Havia_pragas']
    nivelIdentificacao = 'N/A'
    nomePopular = 'N/A'
    conclusao = request.form['comentario']


    if opcaoEmbalagem == 'Sim':
        estadoEmbalagem = request.form['estado_embalagem']
        conservacaoEmbalagem = request.form['estado_embalagem2']


    if opcaoPragas == 'Sim':
        nivelIdentificacao = request.form['identificação_pragas']
        if nivelIdentificacao == 'Nome popular':
            nomePopular = request.form['nome_praga']

    inserir_laudo(cnpj, produto, qtProduto, nChamado, opcaoEmbalagem, estadoEmbalagem, conservacaoEmbalagem, opcaoPragas, nivelIdentificacao, nomePopular, conclusao)

    return '''<head><meta http-equiv="refresh" content="0; url=http://localhost:5000/"/></head>
<script>alert("Dados enviados com sucesso.");</script>'''

#Funcoes para o cadastro

@app.route("/cadastrar", methods=['GET', 'POST'])
def cadastroPage():
    estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA',
    'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    return render_template("cadastro.html", ufs = estados)

@app.route('/cadastro-success', methods=['GET', 'POST'])
def getFormCadastro():
    nome = request.form['cliente']
    cnpj = request.form['cnpj']
    email = request.form['email']
    endereco = request.form['endereco']
    estado = request.form['estado']
    cep = request.form['cep']
    
    inserir_cliente(nome, cnpj, email, endereco, estado, cep)
    
    return '''<head><meta http-equiv="refresh" content="0; url=http://localhost:5000/"/></head>
<script>alert("Dados enviados com sucesso.");</script>'''


if __name__ == '__main__':
    app.run(host='localhost', debug=True)
