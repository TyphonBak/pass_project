from flask import current_app
from jogo_app.modules.usuario import Usuario
import sqlite3

def conecta(comando, dados):
    conexao = sqlite3.connect(current_app.db)
    try:
        cursor = conexao.cursor()
        if dados:
            cursor.execute(comando, dados)
        else:
            cursor.execute(comando)
        if 'INSERT' in comando:
            conexao.commit()
        else:
            return cursor.fetchall()
    except Exception as e:
        print('Alerta(Usuario DB): ', e)
        return None
    finally:
        cursor.close()
        conexao.close()

def listar():
    comando = 'SELECT id, nome, email, google_id FROM Usuario'
    return conecta(comando, None)

def buscar(dados):
    comp = ' WHERE'
    if dados.get('id_usuario'):
        comp+= ' id==:id_usuario'
    elif dados.get('google_id'):
        comp += ' google_id==:google_id'
    else:
        return { 'erro': 'id_usuario e google_id não passados' }
    comando = 'SELECT id, nome, email, google_id FROM Usuario'+comp
    res = conecta(comando, dados)
    return Usuario.cria_de_tupla(res[0]) if len(res) else None

def novo(dados):
    comando = 'INSERT INTO Usuario (nome, email, google_id) VALUES (:nome, :email, :google_id)'
    print(dados)
    conecta(comando, dados)
    print(listar())
    return Usuario.cria_de_tupla(listar()[-1])
