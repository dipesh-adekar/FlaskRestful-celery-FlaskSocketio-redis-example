from application import create_app, socketio

app = create_app('default')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5050)

