from flask import Flask
from flask_socketio import SocketIO
from flask_session import Session

socketio = SocketIO(manage_session=False)

def create_app(debug=False):
    app = Flask(__name__)
 
    app.db = 'jogo_senha.db'
    app.debug = debug
    app.config['SECRET_KEY'] = 'development key'
    app.config['SESSION_TYPE'] = 'filesystem'

    from jogo_app.jogo import jogo_app
    app.register_blueprint(jogo_app)

    Session(app)
    socketio.init_app(app)

    return app