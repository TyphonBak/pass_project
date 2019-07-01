
from jogo_app.modules.jogo import Jogo
from jogo_app.infra.jogo_db import novo as novo_db, listar as buscar_db

def novo(dados):
    jogo = Jogo.cria(dados)
    try:
        pass
        #return novo_db(dados)
    except Exception as e:
        print('Novo service error: ', e)
        return {'code': 400, 'msg': 'Não foi possivel iniciar um novo jogo. Contate o suporte.'}

def buscar(dados):
    pass
    #jogo = buscar_db()
