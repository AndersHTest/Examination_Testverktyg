import itertools
from src.fav_books import FavoriteBooks


class BookStore:
    def __init__(self):
        self.katalog = []
        self.favorites = FavoriteBooks()

    def add_book(self, author, title):
        book = Book(author, title)
        self.katalog.append(book)
        return book
        # Lägg till en bok i katalogen

    def toggle_favorite(self, book_id):
        for book in self.katalog:
            if book.book_id == book_id:
                if book not in self.favorites.books:
                    self.favorites.add_book_to_favorites(book)
                else:
                    self.favorites.remove_book_from_favorites(book)
        # Favoritmarkera en bok i katalogen


class Book:
    book_id = itertools.count()

    def __init__(self, author, title):
        self.book_id = next(Book.book_id)
        self.author = author
        self.title = title
