## Examination: Testautomatisering och testverktyg

| Krav       | Status | 🟠🟡🟢 |
|------------|--------|--------|
| G          | 100%   | 🟢     |
| VG         | 100%   | 🟢     |

### Instruktioner
<pre>
Kör 'pytest' i terminalen för att köra TDD-tester
Kör 'behave --format progress3' i terminalen för att köra BDD-tester
Kör 'flake8' i terminalen för att testa linting
</pre>

### Filträd
<pre>
project
│   .gitignore
│   ANSWERS.md
│   behave.ini
│   conftest.ini
│   pytest.ini
│   README.md
│   requirements.txt
│   setup.cfg
│   STORIES.md
│
└───.github
│   │
│   └───workflows
│       ci.yml
│
└───src
│   │   book_store.py
│   │   fav_books.py
│   │
│   └───features
│       │   add_book.feature
│       │   environment.py
│       │   my_books.feature
│       │   navigation.feature
│       │   startsida.feature
│       │   statistics.feature
│       │
│       └───pages
│       │       base_page.py
│       │
│       └───steps
│               step_add_book.py
│               step_my_books.py
│               step_navigation
│               step_startsida.py
│               step_statistics.py 
│   
└───tests
    │
    └───integration
    │       test_book_store_fav.py
    │
    └───unit
            test_book_store.py
            test_fav_books.py
</pre>