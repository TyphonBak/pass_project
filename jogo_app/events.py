from flask_socketio import emit
from create_app import socketio

@socketio.on('jogada')
def nova_jogada(dados):
    print('Socket Received! ', dados)
    emit('retorna jogada', dados)
    return 'one', 2
