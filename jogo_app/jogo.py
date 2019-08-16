from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from jogo_app.services.jogo_service import novo as novo_service, buscar as buscar_service
from jogo_app.services.jogadas_service import buscar as buscar_jogadas_service, faz_jogada as fazjogada_service
import json

jogo_app = Blueprint('jogo_app', __name__, static_folder='static', template_folder='templates', static_url_path='/jogo_app-static')

@jogo_app.route('/')
def index():
    session['titulo'] = 'Jogo Senha'
    print('Index Jogadas: ', session.get('jogadas'))
    #import ipdb; ipdb.set_trace()
    return render_template('index.html')

@jogo_app.route('/jogo/<int:id_jogo>', methods=['GET'])
@jogo_app.route('/jogo/', methods=['GET'])
def jogo(id_jogo=None):
    if id_jogo != None and session.get('usuario') == None:
        return redirect(url_for('.index'))
    if not session.get('jogo'):
        jogadas = buscar_jogadas_service({ 'id_jogo': id_jogo })
        jogo = buscar_service({'id_jogo': id_jogo, 'id_jogador': session.get('usuario').get('id') if session.get('usuario') else session.get('usuario')})
        session['jogo'] = jogo
        session['jogadas'] = jogadas
    print('Jogadas Atuais: ',session.get('jogadas'))
    return render_template('jogo.html')

from .events import authroute, nova_jogada
