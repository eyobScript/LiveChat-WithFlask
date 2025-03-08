from flask import Flask, render_template, session, request, redirect, flash
from flask_socketio import join_room, leave_room, SocketIO, send
import random
from string import ascii_uppercase


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gdfvbnsoehkcxdtfcygvuhijofebcw'
socketio = SocketIO(app=app)


rooms = {}

def generate_room_code(length):
    while True:
        code = ''
        for _ in range(length):
            code=+ random.choice(ascii_uppercase)
        if code not in rooms:
            break
    return code

@app.route('/', methods=['GET', 'POST'])
def home():
    session.clear()
    if request.method == 'POST':
        name = request.form.get('name')
        code = request.form.get('code')
        create = request.form.get('create', False)
        join = request.form.get('join', False)

        if not name:
            return render_template('home.html', error='Please enter your name.', code=code, name=name)

        if join != False and not code:
            return render_template('home.html', error='Please enter room code.', code=code, name=name)

        room = code
        if create != False == True:
            room = generate_room_code(5)
            rooms[room] = {"messages": [], "members": 0}
        elif code not in rooms:
            return render_template('home.html', error="Room doesn't exist!", code=code, name=name)



        session["room"] = room
        session["name"] = name


    return render_template('home.html')



if __name__ == "__main__":
    socketio.run(app, debug=True)