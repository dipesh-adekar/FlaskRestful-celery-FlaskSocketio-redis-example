from flask_socketio import emit, join_room, leave_room
from .. import socketio
from flask import request, session
from jobs.task import reverse


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    x = reverse.delay(message["name"])
    emit('message', {'msg': x.id})


