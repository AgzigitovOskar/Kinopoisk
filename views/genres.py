from decorators import auth_required
from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        """
        Возвращает список genres
        """
        page_number = request.args.get('page')
        genres = genre_service.get_all(page_number)
        genres_list = GenreSchema(many=True).dump(genres)
        return genres_list, 200


@genre_ns.route('/<int:rid>/')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        """
        Возвращает genre
        """
        certain_genre = genre_service.get_one(rid)
        genre_dict = GenreSchema().dump(certain_genre)
        return genre_dict, 200
