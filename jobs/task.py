from application import celery
from flask_socketio import SocketIO
socketio = SocketIO(message_queue='redis://localhost:6379')


@celery.task(name="task.reverse")
def reverse(string):
    socketio.emit('message', {'msg': string}, namespace="/chat")
    return {"message": string}

