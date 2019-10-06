from flask import Flask
from flask_cors import CORS
from config import config
from flask_socketio import SocketIO
from celery import Celery

socketio = SocketIO()
celery = Celery(__name__)
celery.config_from_object('jobs.celeryconfig')


def create_app(config_name):
    import eventlet
    eventlet.monkey_patch()
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    celery.conf.update(app.config)
    CORS(app)
    from .main import application_model
    app.register_blueprint(application_model, url_prefix="/application")
    socketio.init_app(app, async_mode='eventlet', message_queue='redis://localhost:6379')

    return app
