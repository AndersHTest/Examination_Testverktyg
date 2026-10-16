import pytest
from src.book_store import BookStore


@pytest.mark.integration
def test_book_store_add_book__integration():
    # Arrange
    bs = BookStore()

    # Act
    bs.add_book("Guido van Rossum",
                "Ormar på ett plan: En Python-berättelse")
    result = len(bs.katalog)

    # Assert
    assert result == 1


@pytest.mark.integration
def test_book_store_toggle_favorite__integration():
    # Arrange
    bs = BookStore()
    bok1 = bs.add_book("Guido van Rossum",
                       "Ormar på ett plan: En Python-berättelse")

    # Act
    bs.toggle_favorite(bok1.book_id)
    result = len(bs.favorites.books)

    # Assert
    assert result == 1


@pytest.mark.integration
def test_book_store_toggle_favorite__remove():
    # Arrange
    bs = BookStore()
    bok1 = bs.add_book("Guido van Rossum",
                       "Ormar på ett plan: En Python-berättelse")

    # Act
    bs.toggle_favorite(bok1.book_id)
    bs.toggle_favorite(bok1.book_id)
    result = len(bs.favorites.books)

    # Assert
    assert result == 0
