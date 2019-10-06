from flask import jsonify, request, current_app
from flask_restful import Resource, Api
from application import socketio
from . import application_model

from jobs.task import reverse

api = Api(attendance_model)


class HelloWorld(Resource):
    def get(self, name):
        print(name)
        x = reverse.delay(name)
        return x.id


api.add_resource(HelloWorld, '/<name>')

