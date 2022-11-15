import pytest

from dao.genre import GenreDAO
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_Dao: GenreDAO):
        self.genre_service = GenreService(genre_Dao)

    def test_get_one(self):
        certain_genre = self.genre_service.get_one(1)

        assert certain_genre is not None
        assert certain_genre.id == 1
        assert certain_genre.name == 'horror'

    def test_get_all(self):
        all_genres = self.genre_service.get_all(None)

        assert all_genres is not None
        assert type(all_genres) == list
