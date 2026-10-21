## Examination: Testautomatisering och testverktyg

| Krav       | Status | 🟠🟡🟢 |
|------------|--------|--------|
| G          | 100%   | 🟢     |
| VG         | 100%   | 🟢     |

### Instruktioner
<pre>
Kör 'pytest' i terminalen för att köra TDD-tester

Kör 'behave --format progress3' i terminalen för att köra BDD-tester. Tid: ca 5s.
-Alternativt 'behave --format plain' för att skriva ut alla steg. Tid: ca 5s.
-För att granska körningen visuellt, med lagom hastighet, ersätt flaggan
i environment-filen på rad 7 till 'headless=False, slow_mo=1000'. Tid: ca 60s.

Kör 'flake8 src tests' i terminalen för att analysera källkod (linting)

Mina svar på teorifrågorna finns i ANSWERS.md.
Mina användarberättelser finns i STORIES.md.
Källkod för backend finns i katalogen src.
BDD-test finns i src/features och dess underkataloger.
TDD-test finns i tests/integration samt tests/unit.
Inställningar för CI workflow finns under .github/workflows.
Övriga konfigurationer och inställningar återfinns i roten.
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