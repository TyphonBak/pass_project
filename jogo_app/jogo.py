from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from jogo_app.services.jogo_service import novo as novo_service, buscar as buscar_service
from jogo_app.services.jogadas_service import buscar as buscar_jogadas_service, faz_jogada as fazjogada_service
from jogo_app.services.usuario_service import loga_usuario as loga_usuario_service
from jogo_app.modules.usuario import Usuario
import json

jogo_app = Blueprint('jogo_app', __name__, static_folder='static', template_folder='templates', static_url_path='/jogo_app-static')

@jogo_app.route('/')
def index():
    session['titulo'] = 'Jogo Senha'
    #import ipdb; ipdb.set_trace()
    return render_template('index.html')

@jogo_app.route('/jogo/<int:id_jogo>', methods=['GET'])
@jogo_app.route('/jogo/', methods=['GET'])
def jogo(id_jogo=None):
    if not session.get('jogo'):
        jogadas = buscar_jogadas_service({ 'id_jogo': id_jogo })
        jogo = buscar_service({'id_jogo': id_jogo, 'id_jogador': session.get('usuario').get('id') if session.get('usuario') else session.get('usuario')})
        session['jogo'] = jogo
        session['jogadas'] = jogadas
    return render_template('jogo.html')

@jogo_app.route('/jogo/<int:id_jogo>', methods=['POST'])
@jogo_app.route('/jogo/', methods=['POST'])
def faz_jogada(id_jogo=None):
    print('bateu: ', request.form)
    print('jogo atual: ', session['jogo'])
    id_usuario = session.get('usuario').get('id') if session.get('usuario') != None else 'Anonimo'
    res = fazjogada_service({'jogo': session.get('jogo'), 'id_jogador': id_usuario  ,'chute': request.form})    
    #print(request.headers.get('your-header-name'))
    print('Jogadas:', session['jogadas'])
    return redirect(url_for('.jogo', id_jogo=id_jogo))

@jogo_app.route('/authroute', methods=['POST'])
def authroute():
    res = request.form
    print('Rota de Autorizacao: ', res)
    usuario = loga_usuario_service(res)
    print('USuario: ',usuario.__dict__())
    if not isinstance(usuario, Usuario):
        print('Erro ao logar: ', usuario)
        return jsonify(usuario)
    session['usuario'] = usuario.__dict__()
    return redirect(url_for('.index'))

from .events import nova_jogada, conectado
