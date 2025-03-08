import json

from flask import Flask, render_template, session, request, redirect, flash, url_for
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
            code +=random.choice(ascii_uppercase)
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
        if create != False:
            room = generate_room_code(5)
            rooms[room] = {"messages": [], "members": 0}
        elif code not in rooms:
            return render_template('home.html', error="Room doesn't exist!", code=code, name=name)



        session["room"] = room
        session["name"] = name

        return redirect(url_for('room'))

    return render_template('home.html')


@app.route('/room')
def room():
    room = session.get('room')
    if room is None or session.get('name') is None or room not in rooms:
        return redirect(url_for('home'))
    return render_template('room.html', code=room, messages=rooms[room]["messages"])

@socketio.on("message")
def message(data):
    room = session.get('room')
    if room not in rooms:
        return
    content = {
        "name": session.get("name"),
        "message": data["data"]
    }
    send(content, to=room)
    rooms[room]["messages"].append(content)



@socketio.on("connect")
def connect(auth):
    name = session.get('name')
    room = session.get('room')

    # if name and room doesnt exist in session
    if not name or not room:
        return
    # if room doesnt exist in rooms
    if room not in rooms:
        leave_room(room=room)
        return

    #  allows the user to join the room
    join_room(room=room)
    send(message={"name": name, "message":"hase enterd the room"}, to=room)
    rooms[room]['members'] += 1
    print(f'{name} joined in room {room}')

@socketio.on("disconnect")
def disconnect():
    name = session.get('name')
    room = session.get('room')
    leave_room(room)

    if room in rooms:
        rooms[room]["members"] -= 1
        if rooms[room]["members"] <= 0:
            del rooms[room]
        send(message={"name": name, "message": "hase left the room"}, to=room)
        print(f'{name} left in room {room}')


if __name__ == "__main__":
    socketio.run(app, debug=True)