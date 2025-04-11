from flask import Flask, request
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Evento para cuando alguien se conecta
@socketio.on('connect')
def handle_connect():
    print('🔌 Nuevo usuario conectado')

# Evento para cuando alguien manda un mensaje
@socketio.on('message')
def handle_message(msg):
    print(f'📩 Mensaje recibido: {msg}')
    send(msg, broadcast=True)  # Reenvía a todos

# Ejecutar el servidor
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
