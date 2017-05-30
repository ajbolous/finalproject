from flask import Flask, render_template
from flask_socketio import SocketIO,send,emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,engineio_logger=True)


@socketio.on('service_pipe', namespace='/')
def service_handler(message):
    data = [];
    for i in range(1,10):
        data.append({'label':i, 'value':random.randint(1,100)})
    emit('service_response',{'data': data})

@socketio.on('echo_pipe', namespace='/')
def echo_handler(message):
    emit('echo_response', {'data': message})


if __name__ == '__main__':
    socketio.run(app)
