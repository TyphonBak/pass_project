from flask import current_app
from jogo_app.modules.jogada import Jogada
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
            result = cursor.fetchall()
            print('Resultado: ', result)
            return result
    except Exception as e:
        print('Alerta(Jogada DB): ', e)
        return None
    finally:
        cursor.close()
        conexao.close()

def buscar(dados):
    comando = 'SELECT id, jogador, chute, jogo, qualidade FROM Jogada WHERE jogo==:jogo'
    return [Jogada.cria_de_tupla(jogada) for jogada in filter(lambda jg: jg != None, conecta(comando, dados))]

def novo(dados):
    comando = 'INSERT INTO Jogada (jogador, chute, jogo, qualidade) VALUES (:jogador, :chute, :jogo, :qualidade)'
    conecta(comando, dados)
    return buscar(dados=dados)[-1]
