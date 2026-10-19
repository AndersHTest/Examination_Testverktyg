import pytest


# Lägger till en bok i favoriter
@pytest.mark.unit
def test_fav_books_add__mock(favorite_books, fav_book):
    # Act
    favorite_books.add_book_to_favorites(fav_book)
    result = len(favorite_books.books)

    # Assert
    assert result == 1


# Tar bort en bok ur favoriter
@pytest.mark.unit
def test_fav_books_remove__mock(favorite_books, fav_book):
    # Arrange
    favorite_books.add_book_to_favorites(fav_book)

    # Act
    favorite_books.remove_book_from_favorites(fav_book)
    result = len(favorite_books.books)

    # Assert
    assert result == 0
