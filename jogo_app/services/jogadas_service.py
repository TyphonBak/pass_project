from jogo_app.modules.jogada import Jogada

def buscar(dados):
    if dados.get('id_jogo'):
        #buscar no banco com dados['id_jogo']
        jogadas = [filter(lambda jgd: Jogada(jgd.jogador, jgd.chute, jgd.jogo), '''retornoDoBanco''')]
        return jogadas
    else:
        return []
