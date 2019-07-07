from random import choice

def gera_segredo():
    escolhas = []
    opcoes = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while len(escolhas) < 4:
        escolha = choice(opcoes)
        opcoes.remove(escolha)
        escolhas += [escolha]
    return converte_lista_para_str(escolhas)

def converte_lista_para_str(lista):
    return ''.join(map(str, lista))

def compara(chute, segredo):
    resultado = { 'otimo': 0, 'bom': 0, 'ruim': 0 }
    chute_lista = list(str(chute))
    segredo_lista = list(segredo)
    for i in range(len(chute_lista)):
        if chute_lista[i] == segredo_lista[i]:
            resultado['otimo'] += 1
            chute_lista[i] = None
            segredo_lista[i] = None
    for valor in chute_lista:
        if valor in segredo_lista:
            resultado['bom'] += 1
        else:
            resultado['ruim'] += 1
    return ''.join([str(item) for item in resultado.values()])

def qualifica_chute(jogo, jogada):
    if jogada.jogador == jogo.jogador1:
        segredo_a_comparar = jogo.segredo2
    elif jogada.jogador == jogo.jogador2:
        segredo_a_comparar = jogo.segredo1
    else:
        raise Exception('Erro ao qualificar chute')
    return compara(jogada.chute, segredo_a_comparar)
