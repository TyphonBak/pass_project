from flask import current_app
from jogo_app.modules.jogo import Jogo
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
        print('Alerta(Jogo DB): ', e)
        return None
    finally:
        cursor.close()
        conexao.close()

def buscar(dados):
    comando = 'SELECT id, jogador1, jogador2, segredo1, segredo2, turno FROM Jogo WHERE id==:id_jogo'
    return Jogo.cria_de_tupla(conecta(comando, dados)[0])

def listar(dados=None):
    if dados:
        comp = ' WHERE'
        comp += f' jogador1==:jogador1 OR'
        comp += f' jogador2==:jogador2' if dados.get('jogador2') else ' 0'

    comando = 'SELECT id, jogador1, jogador2, segredo1, segredo2, turno FROM Jogo' + comp if dados else ''
    return conecta(comando, dados)

def novo(dados):
    comando = 'INSERT INTO Jogo (jogador1, jogador2, segredo1, segredo2, turno) VALUES (:jogador1, :jogador2, :segredo1, :segredo2, :turno)'
    conecta(comando, dados)
    return Jogo.cria_de_tupla(listar(dados=dados)[-1])

def deleta(dados):
    comando = 'DELETE FROM Jogo WHERE id==:id'
    return conecta(comando, dados)