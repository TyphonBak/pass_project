from flask import Flask
from jogo_app.jogo import jogo_app
import os

def create_app():
    app = Flask(__name__)

    app.register_blueprint(jogo_app)
    app.secret_key = 'development key'

    return app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host='0.0.0.0', port=port)
