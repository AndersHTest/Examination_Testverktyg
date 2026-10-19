import pytest
from src.book_store import BookStore
from src.fav_books import FavoriteBooks


@pytest.fixture
def anders_bokhandel():
    a = BookStore()
    return a

@pytest.fixture
def favorites(anders_bokhandel, mock_book, mocker):
    anders_bokhandel.katalog.append(mock_book)
    favorites = mocker.patch.object(anders_bokhandel, "favorites")
    return favorites

@pytest.fixture
def mock_book(anders_bokhandel, mocker):
    book = mocker.Mock(book_id=0)
    return book

@pytest.fixture
def favorite_books():
    fb = FavoriteBooks()
    return fb

@pytest.fixture
def fav_book(mocker):
    book = mocker.Mock()
    return book
