import pytest
import src.book_store as book_store


@pytest.mark.unit
def test_book_store_add_book__mock(mocker):
    # Arrange
    book1 = mocker.sentinel.book
    book_constructor = mocker.patch.object(
        book_store, "Book", return_value=book1
    )
    bokhandel = book_store.BookStore()

    # Act
    result = bokhandel.add_book("Peter Petersson", "Titanic")

    # Assert
    book_constructor.assert_called_once_with("Peter Petersson", "Titanic")
    assert result == book1
    assert bokhandel.katalog == [book1]


@pytest.mark.unit
def test_book_store_toggle_on__mock(mocker):
    # Arrange
    bokhandel = book_store.BookStore()
    book = mocker.Mock(book_id=0)
    bokhandel.katalog.append(book)
    favorites = mocker.patch.object(bokhandel, "favorites")
    favorites.books = []

    # Act
    bokhandel.toggle_favorite(book.book_id)

    # Assert
    favorites.add_book_to_favorites.assert_called_once_with(book)
    favorites.remove_book_from_favorites.assert_not_called()


@pytest.mark.unit
def test_book_store_toggle_off__mock(mocker):
    # Arrange
    store = book_store.BookStore()
    book = mocker.Mock(book_id=0)
    store.katalog.append(book)

    favorites = mocker.patch.object(store, "favorites")
    favorites.books = [book]

    # Act
    store.toggle_favorite(book.book_id)

    # Assert
    favorites.remove_book_from_favorites.assert_called_once_with(book)
    favorites.add_book_to_favorites.assert_not_called()
