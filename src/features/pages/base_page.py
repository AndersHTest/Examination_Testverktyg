import re


class BasePage:
    def __init__(self, page):

        # Base page
        self.page = page
        self.catalog = page.get_by_test_id("catalog")
        self.add_book = page.get_by_test_id("add-book")
        self.my_books = page.get_by_test_id("favorites")
        self.statistics = page.get_by_test_id("statistics")
        self.heading = page.get_by_role("heading", name="Välkommen!")
        self.paragraph = page.get_by_text(re.compile("Sidan.+läsa.+favoriter."))
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
        self.list_object_pwc = page.get_by_test_id(re.compile("fav-Playwright: C.+"))
        self.paragraph_1 = page.get_by_text(re.compile("När.+visas här"))

        # Statistics
        self.book_count = page.get_by_test_id("book-count")
        self.favorite_count = page.get_by_test_id("stars-count")
        self.text_2 = page.get_by_text(re.compile(".+2 böcker[.]"))
        self.text_4 = page.get_by_text(re.compile(".+4 böcker[.]"))
        self.text_6 = page.get_by_text(re.compile(".+6 böcker[.]"))

        # Böcker
        self.book_general = page.get_by_test_id(re.compile("star-.+"))
        self.book_titanic = page.get_by_test_id("star-Titanic")
        self.book_opep = page.get_by_test_id(re.compile("star-Orm.+"))
        self.book_tpp = page.get_by_test_id(re.compile("star-The Pragmatic.+"))
        self.book_pff = page.get_by_test_id(re.compile("star-Python.+"))
        self.book_wyt = page.get_by_test_id(re.compile("star-Why Your Tests.+"))
        self.book_pwc = page.get_by_test_id(re.compile("star-Playwright: C.+"))
        self.book_gbo = page.get_by_test_id(re.compile("star-Git Blame.+"))

    def navigate(self):
        self.page.goto("https://tap-vt26-testautomatisering.github.io/exam/")
