from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(debug=False):
    app = Flask(__name__)
 
    app.db = 'jogo_senha.db'
    app.debug = debug
    app.secret_key = 'development key'

    from jogo_app.jogo import jogo_app
    app.register_blueprint(jogo_app)

    socketio.init_app(app)

    return app