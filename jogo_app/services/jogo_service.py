
from jogo_app.modules.jogo import Jogo
from jogo_app.modules.jogada import Jogada
from jogo_app.infra.jogo_db import novo as novo_db, buscar as buscar_db

def novo(dados):
    jogo = Jogo.cria(dados)
    if not dados.get('jogador2'):
        jogo.define_segredo(jogo.jogador1, None)
    if jogo.jogador1 == 'Anonimo':
        return jogo
    try:
        return novo_db(jogo.__dict__())
    except Exception as e:
        print('Novo service error: ', e)
        return {'code': 400, 'msg': 'Não foi possivel iniciar um novo jogo. Contate o suporte.'}

def buscar(dados):
    if dados.get('id_jogo') == None:
        jogo = novo({ 'jogador1': dados.get('id_jogador') if dados.get('id_jogador') else 'Anonimo' })
    else:
        jogo = buscar_db( { 'id_jogo': dados.get('id_jogo') })
    print('Este eh o jogo', jogo.__dict__())
    return jogo.__dict__()
