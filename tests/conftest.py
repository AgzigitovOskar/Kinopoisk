from unittest.mock import MagicMock

import pytest

from app import app
from dao.genre import GenreDAO
from dao.model.genre import Genre


@pytest.fixture()
def genre_Dao():
    """
    fixture for genre service_tests tests
    """

    genre_dao = GenreDAO(None)

    g1 = Genre(id=1, name='horror')
    g2 = Genre(id=2, name='comedy')
    g3 = Genre(id=3, name='action')

    genre_dao.get_one = MagicMock(return_value=Genre(id=1, name='horror'))
    genre_dao.get_all = MagicMock(return_value=[g1, g2, g3])

    return genre_dao


@pytest.fixture()
def client():
    return app.test_client()


