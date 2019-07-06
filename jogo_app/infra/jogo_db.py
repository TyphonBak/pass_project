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
        print('Alerta(Jogo DB): ', e)
        return None
    finally:
        cursor.close()
        conexao.close()

def buscar(dados):
    comando = 'SELECT (id, jogador1, jogador2, segredo1, segredo2, turno) FROM Jogo WHERE id==:id_jogo'
    return conecta(comando, dados)

def listar(dados=None):
    if dados:
        comp = ' WHERE'
        comp += f' jogador1==:jogador1 OR'
        comp += f' jogador2==:jogador2' if dados.get('jogador2') else ' FALSE'

    comando = 'SELECT (id, jogador1, jogador2, segredo1, segredo2, turno) FROM Jogo' + comp if dados else ''
    return conecta(comando, dados)

def novo(dados):
    comando = 'INSERT INTO Jogo (jogador1, jogador2, segredo1, segredo2, turno) VALUES (:jogador1, :jogador2, :segredo1, :segredo2, :turno)'
    conecta(comando, dados)
    return listar(dados=dados)[-1]

def deleta(dados):
    comando = 'DELETE FROM Jogo WHERE id==:id'
    return conecta(comando, dados)