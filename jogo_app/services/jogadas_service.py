from jogo_app.modules.jogada import Jogada
from jogo_app.modules.jogo import Jogo
from jogo_app.services.jogo_service import buscar as buscar_jogo_service
from jogo_app.infra.jogada_db import buscar as buscar_db, novo as novo_db
from jogo_app.services.segredo_service import qualifica_chute, converte_lista_para_str

def buscar(dados):
    if dados.get('id_jogo'):
        dados['jogo'] = dados.get('id_jogo')
        jogadas = buscar_db(dados)
        return [jogada.__dict__() for jogada in jogadas]
    else:
        return []

def faz_jogada(dados):
    chute = converte_lista_para_str(dados.get('chute').getlist('chute'))
    jogo = Jogo.cria(buscar_jogo_service({ 'id_jogo': dados.get('id_jogo') }))
    jogada = jogo.faz_jogada(dados.get('id_jogador'), chute)
    jogada.qualidade = qualifica_chute(jogo, jogada)
    if isinstance(jogo, Jogo):
        if isinstance(jogada, Jogada):                
            #registra jogada no banco (falta implementar)
            jogada = novo_db(jogada.__dict__())
            if jogo.acertou(jogada):
                jogo.finaliza_jogo()
                #retorna jogo + status da jogada (verificar se o codigo de retorno esta adequado)
                return { 'code': 302, 'jogo': jogo}
            
            return { 'code': 302, 'jogo': jogo}
        elif jogo.turno == None:
            #retornar que o jogo ja terminou
            pass
        else:
            #(verificar se o codigo de retorno esta adequado)
            return {'code': 400, 'msg': 'Não foi possivel realizar a jogada. Contate o suporte'}
    else:
        #(verificar se o codigo de retorno esta adequado)
        return {'code': 400, 'msg': 'Não foi possivel encontrar o jogo. Contate o suporte'}
