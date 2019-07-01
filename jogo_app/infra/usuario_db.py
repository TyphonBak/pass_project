from flask import current_app
from jogo_app.modules.usuario import Usuario
import sqlite3

def conecta(comando, dados):
    conexao = sqlite3.connect(current_app.db)
    try:
        cursor = conexao.cursor()
        cursor.execute(comando, dados)
        return cursor.fetchall()
    except Exception as e:
        print('Alerta: ', e)
        return None
    finally:
        cursor.close()
        conexao.close()

def buscar(dados):
    dados = {'id_usuario': dados.get('id_usuario')}
    comando = 'SELECT (id, nome, email, google_id) FROM Usuario WHERE google_id==:id_usuario'
    return conecta(comando, dados)

def novo(dados):
    comando = 'INSERT INTO Usuario (nome, email, google_id) VALUES (:nome, :email, :google_id)'
    conecta(comando, dados)
    return listar(dados=dados)[-1]
