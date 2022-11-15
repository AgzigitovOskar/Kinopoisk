from decorators import auth_required
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        """
        Возвращает список фильмов. Окончательный список зависит от
        наличия фильтров(статус и номер страницы)
        """
        status = request.args.get('status')
        page_number = request.args.get('page')

        filters = {
            "status": status,
            "page": page_number
        }

        movies = movie_service.get_all(filters)
        movies_list = MovieSchema(many=True).dump(movies)
        return movies_list, 200


@movie_ns.route('/<int:bid>/')
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        """
        Возвращает определенный фильм
        """
        certain_movie = movie_service.get_one(bid)
        movie_dict = MovieSchema().dump(certain_movie)
        return movie_dict, 200
