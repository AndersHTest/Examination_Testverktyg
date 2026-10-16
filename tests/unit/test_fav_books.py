import pytest
from src.fav_books import FavoriteBooks


@pytest.mark.unit
def test_fav_books_add__mock(mocker):
    fb = FavoriteBooks()
    book = mocker.Mock()

    fb.add_book_to_favorites(book)

    assert len(fb.books) == 1


@pytest.mark.unit
def test_fav_books_remove__mock(mocker):
    fb = FavoriteBooks()
    book = mocker.Mock()

    fb.add_book_to_favorites(book)
    fb.remove_book_from_favorites(book)

    assert len(fb.books) == 0
