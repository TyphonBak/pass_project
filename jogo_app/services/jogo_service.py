
from jogo_app.modules.jogo import Jogo
from jogo_app.modules.jogada import Jogada
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
    print('Buscar_Service, dados : ', dados)
    pass
    #jogo = buscar_db()

def faz_jogada(dados):
    chute = dados.get('chute').getlist('chute')
    jogo = buscar(dados.get('id_jogo'))
    jogada = jogo.faz_jogada(dados.get('user'), chute)
    if isinstance(jogo, Jogo):
        if isinstance(jogada, Jogada):                
            #registra jogada no banco (falta implementar)
            if jogo.acertou(jogada):
                jogo.finaliza_jogo()
                #retorna jogo + status da jogada (verificar se o codigo de retorno esta adequado)
                return { 'code': 302, 'jogo': jogo}
            return { 'code': 302, 'jogo': jogo}
        else:
            #(verificar se o codigo de retorno esta adequado)
            return {'code': 400, 'msg': 'Não foi possivel realizar a jogada. Contate o suporte'}
    else:
        #(verificar se o codigo de retorno esta adequado)
        return {'code': 400, 'msg': 'Não foi possivel encontrar o jogo. Contate o suporte'}
