from flask import Blueprint, render_template, request, redirect, url_for, session
from jogo_app.services.jogo_service import novo as novo_service, buscar as buscar_service, faz_jogada as fazjogada_service
from jogo_app.services.jogadas_service import buscar as buscar_jogadas_service
import json

jogo_app = Blueprint('jogo_app', __name__, static_folder='static', template_folder='templates', static_url_path='/jogo_app-static')

@jogo_app.route('/')
def index():
    print('Google: ', session.get('access_token'))
    #import ipdb; ipdb.set_trace()
    return render_template('index.html')

@jogo_app.route('/jogo/<int:id_jogo>', methods=['GET'])
@jogo_app.route('/jogo/', methods=['GET'])
def jogo(id_jogo=None):
    jogadas = buscar_jogadas_service({ 'id_jogo': id_jogo })
    jogo = buscar_service({'id_jogo': id_jogo, 'id_jogador': session.get('access_token')})
    context = {'jogo': jogo, 'jogadas': jogadas}
    print(jogo.segredo_j1)
    return render_template('jogo.html', id_jogo=1, context=context)

@jogo_app.route('/jogo/<int:id_jogo>', methods=['POST'])
def faz_jogada(id_jogo):
    print('bateu: ', request.form)
    print('jogo atual: ', session['jogo'])
    res = fazjogada_service({'id_jogo': id_jogo, 'chute': request.form})
    #print(request.headers.get('your-header-name'))
    return redirect(url_for('.jogo', id_jogo=id_jogo))

@jogo_app.route('/authroute', methods=['POST'])
def authroute():
    res = request.form
    print('Rota de Autorizacao: ', res)
    access_token = res.get('token')
    session['access_token'] = access_token
    session['usuario'] = res.get('nome')
    return redirect(url_for('.index'))
