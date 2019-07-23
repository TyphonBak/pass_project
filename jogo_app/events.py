from flask import session
from flask_socketio import emit
from create_app import socketio
from jogo_app.services.jogadas_service import faz_jogada as fazjogada_service

@socketio.on('jogada')
def nova_jogada(dados):
    #{'chute': ['1', '5', '7', '4']}
    id_usuario = session.get('usuario').get('id') if session.get('usuario') != None else 'Anonimo'
    res = fazjogada_service({'jogo': session.get('jogo'), 'id_jogador': id_usuario  ,'chute': dados.get('chute')})
    print('Retorno service: ', res)
    print('UltimaJogada:', session.get('jogadas')[-1])
    print('Todas Jogadas: ', session.get('jogadas'))
    print('Socket Received! ', dados)
    print(session.get('jogo'))
    if res.get('code') == 302:
        dados['qualidade'] = session.get('jogadas')[-1].get('qualidade')
        emit('retorna jogada', dados)
    return 'one', 2

@socketio.on('novo jogo')
def novo_jogo():
    session['jogo'] = None
    session['jogadas'] = []
