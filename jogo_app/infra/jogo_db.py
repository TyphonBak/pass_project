from flask import current_app
from jogo_app.modules.jogo import Jogo
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

def listar(dados=None):
    if dados:
        comp = ' WHERE'
        comp += f' jogador1==:jogador1 OR'
        comp += f' jogador2==:jogador2' if dados.get('jogador2') else ' FALSE'

    comando = 'SELECT (id, jogador1, jogador2) FROM Jogo'+comp
    return conecta(comando, dados)

def novo(dados):
    comando = 'INSERT INTO Jogo (jogador1, jogador2) VALUES (:jogador1, :jogador2)'
    conecta(comando, dados)
    return listar(dados=dados)[-1]

def deleta(dados):
    comando = 'DELETE FROM Jogo WHERE id==:id'
    return conecta(comando, dados)