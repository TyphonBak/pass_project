from create_app import create_app, socketio
import os

app = create_app(debug=True)
socketio.init_app(app)

if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 5000))
    #app.run(host='0.0.0.0', port=port, debug=True)
    socketio.run(app)
