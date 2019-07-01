from flask import Flask
from jogo_app.jogo import jogo_app

def create_app():
    app = Flask(__name__)

    app.register_blueprint(jogo_app)
    app.secret_key = 'development key'

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5000, debug=True)
