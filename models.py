import sqlite3 as sql

def inserir_laudo(cnpj, produto, quantidade, chamado, embalagem, estado, conservacao, praga, identificacao,
 classe, ordem, familia, genero, especie, nomePopular, conclusao):
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO laudos (cnpj, produto, quantidade, chamado, embalagem, estado,  conservacao, praga, identificacao, classe, ordem, familia, genero, especie, nomePopular, conclusao)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (cnpj, produto, quantidade, chamado, embalagem, estado, conservacao, praga, identificacao, classe, ordem, familia, genero, especie, nomePopular, conclusao))
        conn.commit()


def inserir_cliente(nome, cnpj, email, endereco, estado, cep):
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO clientes (nome, cnpj, email ,endereco, estado, cep) VALUES  (?,?,?,?,?,?)''',
                    (nome, cnpj, email, endereco, estado, cep))
        conn.commit()

def selecionar_cnpjs():
    cnpjs = []
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT cnpj FROM clientes")
        result = cur.fetchall()
        for cnpj in result:
            cnpjs.append(cnpj[0])
        return cnpjs

def checar_cliente(cnpj):
    string = "SELECT cnpj FROM clientes WHERE cnpj = %s" %cnpj
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        result = cur.execute(string)
        try:
            cnpj = result.fetchall()[0][0]
            return True
        except IndexError:
            return False

def deletar_cliente(cnpj):
    string = "DELETE FROM clientes WHERE cnpj = %s" %cnpj
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        result = cur.execute(string)
        conn.commit()


def checar_chamado(chamado):
    string = "SELECT chamado FROM laudos WHERE chamado = %s" %chamado
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        result = cur.execute(string)
        try:
            cnpj = result.fetchall()[0][0]
            return True
        except IndexError:
            return False

