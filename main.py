from flask import Flask, render_template, session, request, redirect
from flask_socketio import join_room, leave_room, SocketIO, send
import random
from string import ascii_uppercase


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gdfvbnsoehkcxdtfcygvuhijofebcw'
socketio = SocketIO(app=app)


@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        create = request.form.get('create', False)
        join = request.form.get('join', False)

        if not name:
            return render_template('home.html', error='Please enter your name.')

        if code != False and join:
            return render_template('home.html', error='Please enter room code.')

    return render_template('home.html')



if __name__ == "__main__":
    socketio.run(app, debug=True)