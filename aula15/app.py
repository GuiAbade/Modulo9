# SQL - Structured Query Language
# db.sqlite3

import sqlite3

with sqlite3.connect('artistas.db') as conexao:
    # Criar uma conexão com o banco de dados
    sql = conexao.cursor()
    # Rodar comando SQL
    sql.execute(
        'CREATE TABLE IF NOT EXISTS banda (nome text, estilo text, membros interger);')
    sql.execute(
        'INSERT INTO banda(nome, estilo, membros) values ("Banda 1", "Rock", 3);')
    # Exemplo de usar dados da minha aplicação em um comando SQL
    nome = input('Digite o nome da banda')
    estilo = input('Digite o estilo da banda')
    qtd_integrantes = int(input('Quantidade de integrantes da banda'))

    sql.execute('INSERT INTO banda values (?,?,?)',
                [nome, estilo, qtd_integrantes])
    # Salvando alterações no banco de dados
    conexao.commit()

    # Exibir dados no console python(terminal)
    bandas = sql.execute('select * from banda;')
    for banda in bandas:
        print(banda)
