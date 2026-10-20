import pytest


@pytest.mark.integration
def test_book_store_add_book__integration(anders_bokhandel):
    # Act
    anders_bokhandel.add_book("Guido van Rossum",
                              "Ormar på ett plan: En Python-berättelse")
    result = len(anders_bokhandel.katalog)

    # Assert
    assert result == 1


@pytest.mark.integration
def test_book_store_toggle_favorite__integration(anders_bokhandel):
    # Arrange
    bok1 = anders_bokhandel.add_book("Guido van Rossum",
                                     "Ormar på ett plan: En Python-berättelse")

    # Act
    anders_bokhandel.toggle_favorite(bok1.book_id)
    result = len(anders_bokhandel.favorites.books)

    # Assert
    assert result == 1


@pytest.mark.integration
def test_book_store_toggle_favorite__remove(anders_bokhandel):
    # Arrange
    bok1 = anders_bokhandel.add_book("Guido van Rossum",
                                     "Ormar på ett plan: En Python-berättelse")

    # Act
    anders_bokhandel.toggle_favorite(bok1.book_id)
    anders_bokhandel.toggle_favorite(bok1.book_id)
    result = len(anders_bokhandel.favorites.books)

    # Assert
    assert result == 0
