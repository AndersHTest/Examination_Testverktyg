import pytest
from src.fav_books import FavoriteBooks


@pytest.mark.unit
def test_fav_books_add__mock(mocker):
    # Assert
    fb = FavoriteBooks()
    book = mocker.Mock()

    # Act
    fb.add_book_to_favorites(book)
    result = len(fb.books)

    # Assert
    assert result == 1


@pytest.mark.unit
def test_fav_books_remove__mock(mocker):
    # Arrange
    fb = FavoriteBooks()
    book = mocker.Mock()
    fb.add_book_to_favorites(book)

    # Act
    fb.remove_book_from_favorites(book)
    result = len(fb.books)

    # Assert
    assert result == 0
