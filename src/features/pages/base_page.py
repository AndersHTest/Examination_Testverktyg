import re


class BasePage:
    def __init__(self, page):

        # Base page
        self.page = page
        self.catalog = page.get_by_test_id("catalog")
        self.catalog_titanic = page.get_by_test_id("star-Titanic")
        self.add_book = page.get_by_test_id("add-book")
        self.my_books = page.get_by_test_id("favorites")
        self.statistics = page.get_by_test_id("statistics")
        self.heading = page.get_by_role("heading", name="Välkommen!")
        self.paragraph = page.get_by_text(re.compile("Sidan.+läsa.+favoriter."))
        self.add_favorite_pw = page.get_by_test_id(re.compile("star-Playwright: C.+"))
        self.bild = page.get_by_role("img", name="Bokklubb på café")

        # Add Book
        self.fill_title = page.get_by_test_id("add-input-title")
        self.fill_author = page.get_by_test_id("add-input-author")
        self.add_new_book = page.get_by_test_id("add-submit")
        self.title_label = page.get_by_label("Titel")
        self.author_label = page.get_by_label("Författare")

        # My Books
        self.book_list = page.get_by_test_id("book-list")
        self.list_object = page.get_by_test_id(re.compile("fav-.+"))
        self.list_object_pw = page.get_by_test_id(re.compile("fav-Playwright: C.+"))
        self.paragraph_1 = page.get_by_text(re.compile("När.+visas här"))

        # Statistics
        self.book_count = page.get_by_test_id("book-count")
        self.favorite_count = page.get_by_test_id("stars-count")

    def navigate(self):
        self.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")
