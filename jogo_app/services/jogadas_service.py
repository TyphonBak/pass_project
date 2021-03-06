from jogo_app.modules.jogada import Jogada
from jogo_app.modules.jogo import Jogo
from jogo_app.services.jogo_service import buscar as buscar_jogo_service
from jogo_app.infra.jogada_db import buscar as buscar_db, novo as novo_db
from jogo_app.services.segredo_service import qualifica_chute, converte_lista_para_str
from flask import session

def buscar(dados):
    if dados.get('id_jogo'):
        dados['jogo'] = dados.get('id_jogo')
        jogadas = buscar_db(dados)
        return [jogada.__dict__() for jogada in jogadas]
    else:
        return session.get('jogadas') if session.get('jogadas') else []

def faz_jogada(dados):
    chute = converte_lista_para_str(dados.get('chute'))
    dados_jogo = buscar_jogo_service({ 'id_jogo': dados.get('jogo').get('id') }) if dados.get('jogo').get('id') else dados.get('jogo')
    jogo = Jogo.cria(dados_jogo)
    jogada = jogo.faz_jogada(dados.get('id_jogador'), chute)
    if isinstance(jogo, Jogo):
        if isinstance(jogada, Jogada):
            jogada.qualidade = qualifica_chute(jogo, jogada)
            if jogo.jogador1 != 'Anonimo':
                jogada = novo_db(jogada.__dict__())
            session['jogadas'] += [jogada.__dict__()]
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
