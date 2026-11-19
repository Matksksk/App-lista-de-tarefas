import sqlite3
conexao=sqlite3.connect("rockleeVSgaara.db")
cursor=conexao.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS listas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome text NOT NULL
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS tarefas_lista(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa text NOT NULL
    )""")
cursor.execute("""CREATE TABLE IF NOT EXISTS lixeira(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome text NOT NULL
    )""")
def inserir_lista(nome_lista):
    try:
        cursor.execute("INSERT INTO listas (nome) VALUES (?)", (nome_lista,))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False
def buscar_listas():
    cursor.execute("SELECT nome FROM listas")
    return [linha[0] for linha in cursor.fetchall()]
def atualizar_nome(nome_novo,nome_antigo):
    try:
        cursor.execute(("UPDATE listas SET nome = ? WHERE nome = ?"),(nome_novo,nome_antigo))
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        return False