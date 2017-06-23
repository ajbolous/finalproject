from flask import Flask, render_template
from flask_socketio import SocketIO,send,emit
import random
from opmop.main import Application
import threading
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'opmop_secret_key'
socketio = SocketIO(app,host="0.0.0.0", async_mode='threading')


@socketio.on('service_pipe', namespace='/')
def service_handler(message):
    return updateMachines()

@socketio.on('echo_pipe', namespace='/')
def echo_handler(message):
    emit('echo_response', {'data': message})

def updateMachines():
    data = [];
    for machine in Application.database.getMachines():
        data.append({'label': machine.id , 'value':machine.fuelCapacity})
    socketio.emit('service_response',{'data': data})


def periodicUpdate():
    with app.test_request_context():
        from flask import request
        while True:
            time.sleep(5)    
            updateMachines()

if __name__ == '__main__':
    th = threading.Thread(target=periodicUpdate)
    th.start()

    socketio.run(app, host="0.0.0.0")
