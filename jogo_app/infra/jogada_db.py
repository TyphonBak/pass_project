from flask import current_app
from jogo_app.modules.jogada import Jogada
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
    comando = 'SELECT (id, jogador, chute, jogo) FROM Jogada WHERE jogo==:id_jogo'
    return conecta(comando, dados)

def novo(dados):
    comando = 'INSERT INTO Jogada (jogador, chute, jogo) VALUES (:jogador, :chute, :jogo)'
    conecta(comando, dados)
    return listar(dados=dados)[-1]
