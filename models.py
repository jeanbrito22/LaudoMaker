import sqlite3 as sql

def criar_tabela_clientes():
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        cur.executescript("""
drop table if exists clientes;
create table clientes (
id integer primary key autoincrement,
nome text not null,
cnpj varchar(14) not null,
email text not null,
endereco text not null,
estado text not null,
cep text not null
);
""")

def criar_tabela_laudos():
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        cur.executescript("""
drop table if exists laudos;
create table laudos (
id integer primary key autoincrement,
cnpj varchar(14) not null,
produto text not null,
quantidade integer,
chamado text not null,
embalagem varchar(3) not null,
estado text not null,
conservacao text not null,
praga varchar(3) not null,
identificacao text not null,
classe text not null,
ordem text not null,
familia text not null,
genero text not null,
especie text not null,
nomePopular text not null,
conclusao text not null
);
""")

def inserir_laudo(cnpj, produto, quantidade, chamado, embalagem, estado, conservacao, praga, identificacao,
 classe, ordem, familia, genero, especie, nomePopular, conclusao):
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO laudos (cnpj, produto, quantidade, chamado, embalagem, conservacao, estado, praga, identificacao, classe, ordem, familia, genero, especie, nomePopular, conclusao)
        VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (cnpj, produto, quantidade, chamado, embalagem, estado, conservacao, praga, identificacao, classe, ordem, familia, genero, especie, nomePopular, conclusao))
        conn.commit()
    

def inserir_cliente(nome, cnpj, email, endereco, estado, cep):
    with sql.connect("database.db") as conn:
        cur = conn.cursor()
        cur.execute('''INSERT INTO clientes (nome, cnpj, email ,endereco, estado, cep) VALUES  (?,?,?,?,?,?)''',
                    (nome, cnpj, email, endereco, estado, cep))
        conn.commit()

