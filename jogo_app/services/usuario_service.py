from jogo_app.modules.usuario import Usuario
from jogo_app.services.auth_service import valid_token
from jogo_app.infra.usuario_db import buscar as buscar_db, novo as novo_db

def novo(dados):
    usuario = novo_db(dados)
    return usuario

def verifica_usuario(usuario):
    usuario_existente = buscar_db({ 'google_id': usuario.google_id })
    print('Usuario existente: ',usuario_existente)
    if isinstance(usuario_existente, Usuario):
        return usuario
    else:
        return novo(usuario.__dict__())

def loga_usuario(dados):
    token_valido = valid_token(dados.get('token'))
    if token_valido[0]:
        dados = {'token': dados['token'], 'nome': dados['nome'], 'email': dados['email']}
        dados['google_id'] = token_valido[1]
    else:
        return {'code': 401, 'msg': 'Token Invalido' }
    usuario = Usuario.cria(dados)
    return verifica_usuario(usuario)
