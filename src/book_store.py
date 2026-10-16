import itertools
from src.fav_books import FavoriteBooks


class BookStore:
    def __init__(self):
        self.katalog = []
        self.favorites = FavoriteBooks()

        # Lägg till en bok i katalogen
    def add_book(self, author, title):
        book = Book(author, title)
        self.katalog.append(book)
        return book

        # Favoritmarkera en bok i katalogen
    def toggle_favorite(self, book_id):
        for book in self.katalog:
            if book.book_id == book_id:
                if book not in self.favorites.books:
                    self.favorites.add_book_to_favorites(book)
                else:
                    self.favorites.remove_book_from_favorites(book)

        # Ta ut en lista på böcker i katalogen
    def get_katalog(self):
        books = []
        for book in self.katalog:
            books.append(f"id: {book.book_id},"
                         f" title: {book.title}, author: {book.author}")
        return books


class Book:
    book_id = itertools.count()

    def __init__(self, author, title):
        self.book_id = next(Book.book_id)
        self.author = author
        self.title = title
