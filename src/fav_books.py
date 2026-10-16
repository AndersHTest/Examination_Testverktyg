class FavoriteBooks:
    def __init__(self):
        self.books = []

    def add_book_to_favorites(self, book):
        if book not in self.books:
            self.books.append(book)

    def remove_book_from_favorites(self, book):
        if book in self.books:
            self.books.remove(book)
