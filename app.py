from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
   socketio.run(app)