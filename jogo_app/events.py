from flask import session, redirect, url_for
from flask_socketio import emit
from create_app import socketio
from jogo_app.services.jogadas_service import faz_jogada as fazjogada_service
from jogo_app.services.usuario_service import loga_usuario as loga_usuario_service
from jogo_app.modules.usuario import Usuario

@socketio.on('jogada')
def nova_jogada(dados):
    #{'chute': ['1', '5', '7', '4']}
    id_usuario = session.get('usuario').get('id') if session.get('usuario') != None else 'Anonimo'
    res = fazjogada_service({'jogo': session.get('jogo'), 'id_jogador': id_usuario  ,'chute': dados.get('chute')})
    print('Retorno service: ', res)
    print('Todas Jogadas: ', session.get('jogadas'))
    print('Socket Received! ', dados)
    print(session.get('jogo'))
    #adicionar retorno de erro (alerta)
    if res.get('code') == 302:
        dados['qualidade'] = session.get('jogadas')[-1].get('qualidade')
        emit('retorna jogada', dados)
        if res.get('jogo').turno == 'None':
            emit('fim de jogo', dados)
    else:
        emit('emite alerta', res)
    return 'one', 2

@socketio.on('novo jogo')
def novo_jogo():
    session['jogo'] = None
    session['jogadas'] = []

@socketio.on('authroute')
def authroute(user):
    res = user
    print('Rota de Autorizacao: ', res)
    usuario = loga_usuario_service(res)
    print('USuario: ',usuario.__dict__())
    if not isinstance(usuario, Usuario):
        print('Erro ao logar: ', usuario)
        return jsonify(usuario)
    session['usuario'] = usuario.__dict__()
    return redirect(url_for('jogo_app.index'))
