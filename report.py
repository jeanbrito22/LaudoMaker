import os
import sqlite3 as sql

def criar_pasta(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)


def criar_relatorio(cnpj, produto, quantidade, chamado, opcaoEmbalagem, estado, conservacao, opcaoPragas,
    nivelIdentificacao,  conteudoIdentificacao):
    cliente = importar_nome(cnpj)
    nomeRelatorio = cnpj + "-" + chamado
    if opcaoEmbalagem == 'Sim' and opcaoPragas == 'Sim':
        with open("Relatorios/" + nomeRelatorio, "w") as f:
            f.write("*----------------------------------------------------------------------------------------------*\n")
            f.write("*                                        LAUDO DE ANALISE                                      *\n")
            f.write("\nCliente: %s\nProduto: %s\nChamado: %s\n\n\n  Recebemos para analise %s unidade(s) dos produtos %s,\n  com a embalagem %s e %s.\n\n  Analisando a amostra, foram encontrados infestantes do(a) %s: %s\n"
            % (cliente, produto, chamado, quantidade, produto, estado, conservacao, nivelIdentificacao, conteudoIdentificacao))
            f.write("\n")
            f.write( "                  _______________________         _______________________          \n")
            f.write("                   Assinatura Analista              Assinatura Cliente             \n\n")


    elif opcaoEmbalagem == 'Sim' and opcaoPragas == 'Não':
        with open("Relatorios/" + nomeRelatorio, "w") as f:
            f.write("*----------------------------------------------------------------------------------------------*\n")
            f.write("*                                        LAUDO DE ANALISE                                      *\n")
            f.write("\nCliente: %s\nProduto: %s\nChamado: %s\n\n\n  Recebemos para analise %s unidade(s) dos produtos %s,\n  com a embalagem %s e %s.\n\n  Analisando a amostra, não foram encontrados infestantes.\n"
            % (cliente, produto, chamado, quantidade, produto, estado, conservacao))
            f.write("\n")
            f.write( "                  _______________________         _______________________          \n")
            f.write("                   Assinatura Analista              Assinatura Cliente             \n\n")



    elif opcaoEmbalagem == 'Não' and opcaoPragas == 'Sim':
        with open("Relatorios/" + nomeRelatorio, "w") as f:
            f.write("*----------------------------------------------------------------------------------------------*\n")
            f.write("*                                        LAUDO DE ANALISE                                      *\n")
            f.write("\nCliente: %s\nProduto: %s\nChamado: %s\n\n\n  Recebemos para analise %s unidade(s) dos produtos %s,\n  sem embalagem.\n\n  Analisando a amostra, foram encontrados infestantes do(a) %s: %s\n"
            % (cliente, produto, chamado, quantidade, produto, nivelIdentificacao, conteudoIdentificacao))
            f.write("\n")
            f.write( "                  _______________________         _______________________          \n")
            f.write("                   Assinatura Analista              Assinatura Cliente             \n\n")

    else:
        with open("Relatorios/" + nomeRelatorio, "w") as f:
            f.write("*----------------------------------------------------------------------------------------------*\n")
            f.write("*                                        LAUDO DE ANALISE                                      *\n")
            f.write("\nCliente: %s\nProduto: %s\nChamado: %s\n\n\n  Recebemos para analise %s unidade(s) dos produtos %s,\n  sem embalagem.\n\n  Analisando a amostra, não foram encontrados infestantes.\n"
            % (cliente, produto, chamado, quantidade, produto))
            f.write("\n")
            f.write( "                  _______________________         _______________________          \n")
            f.write("                   Assinatura Analista              Assinatura Cliente             \n\n")




def importar_nome(cnpj):
    string = "SELECT nome FROM clientes  WHERE cnpj = %s" %cnpj
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        result = cur.execute(string)
        return result.fetchall()[0][0]