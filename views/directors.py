from decorators import auth_required
from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        """
        Возвращает список directors
        """
        page_number = request.args.get('page')
        directors = director_service.get_all(page_number)
        directors_list = DirectorSchema(many=True).dump(directors)
        return directors_list, 200


@director_ns.route('/<int:rid>/')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        """
        Возвращает director
        """
        certain_director = director_service.get_one(rid)
        director_dict = DirectorSchema().dump(certain_director)
        return director_dict, 200


