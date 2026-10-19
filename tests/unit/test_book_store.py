import pytest
import src.book_store as book_store


# Patchar Book så att add_book() returnerar min fejkade bok.
# Lägger till en bok och verifierar att den är tillagd i katalogen.
@pytest.mark.unit
def test_book_store_add_book__mock(anders_bokhandel, mocker):
    # Arrange
    book1 = mocker.sentinel.book
    book_constructor = mocker.patch.object(
        book_store, "Book", return_value=book1
    )

    # Act
    result = anders_bokhandel.add_book("Peter Petersson", "Titanic")

    # Assert
    book_constructor.assert_called_once_with("Peter Petersson", "Titanic")
    assert result == book1
    assert anders_bokhandel.katalog == [book1]


# Initierar en bokhandel, skapar en mockad bok, toggle on favorite
@pytest.mark.unit
def test_book_store_toggle_on__mock(anders_bokhandel, mock_book, favorites):
    # Arrange
    favorites.books = []

    # Act
    anders_bokhandel.toggle_favorite(mock_book.book_id)

    # Assert
    favorites.add_book_to_favorites.assert_called_once_with(mock_book)
    favorites.remove_book_from_favorites.assert_not_called()


# Initierar en bokhandel, lägger till en mockad bok i favoriter, toggle off favorite
@pytest.mark.unit
def test_book_store_toggle_off__mock(anders_bokhandel, mock_book, favorites):
    # Arrange
    favorites.books = [mock_book]

    # Act
    anders_bokhandel.toggle_favorite(mock_book.book_id)

    # Assert
    favorites.remove_book_from_favorites.assert_called_once_with(mock_book)
    favorites.add_book_to_favorites.assert_not_called()
