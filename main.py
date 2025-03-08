from flask import Flask, render_template, session, request, redirect
from flask_socketio import join_room, leave_room, SocketIO, send
import random
from string import ascii_uppercase


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gdfvbnsoehkcxdtfcygvuhijofebcw'
socketio = SocketIO(app=app)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')



if __name__ == "__main__":
    socketio.run(app, debug=True)