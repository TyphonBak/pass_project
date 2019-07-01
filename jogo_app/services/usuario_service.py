from jogo_app.modules.usuario import Usuario
from jogo_app.services.auth_service import valid_token
from jogo_app.infra.usuario_db import buscar as buscar_db, novo as novo_db

def novo(dados):
    pass

def verifica_usuario(usuario):
    pass

def loga_usuario(dados):
    usuario = Usuario.cria(dados)
    token_valido = valid_token(usuario.token)
    if token_valido[0]:
        usuario.id = token_valido[1]
    verifica_usuario(usuario)
