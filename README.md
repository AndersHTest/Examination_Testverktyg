## <ins> Examination: Testautomatisering och testverktyg </ins>
<br>

### Instruktioner
<pre>
Kör 'pytest' i terminalen för att köra TDD-tester.

Kör 'behave --format progress3' i terminalen för att köra BDD-tester. Tid: ca 5s.
-Alternativt 'behave --format plain' för att skriva ut alla steg. Tid: ca 5s.
-För att granska körningen visuellt, med lagom hastighet, ersätt flaggan
i environment-filen på rad 7 till 'headless=False, slow_mo=1000'. Tid: ca 60s.

Kör 'flake8 src tests' i terminalen för att analysera källkod (linting).

Mina svar på teorifrågorna finns i ANSWERS.md.
Mina användarberättelser finns i STORIES.md.
Källkod för backend finns i katalogen src.
BDD-test finns i src/features och dess underkataloger.
TDD-test finns i tests/integration samt tests/unit.
Inställningar för CI workflow finns under .github/workflows.
Övriga konfigurationer och inställningar återfinns i projektets rotkatalog.
</pre>
<br>

### Krav
| Krav       | Status | 🟠🟡🟢 |
|------------|--------|--------|
| G          | 100%   | 🟢     |
| VG         | 100%   | 🟢     |

<pre>
Jag har arbetat med följande krav:

    • Det finns enhetstester och integrationstester för BookStore och FavoriteBooks.
    • Det finns user stories som täcker all funktionalitet i vyerna Katalog, Lägg till bok samt Mina böcker.
    • Alla user stories har minst en feature. Alla features har minst ett scenario. Alla steg implementeras i någon step-fil.
    • Det går att starta ditt projekt, med hjälp av instruktionerna du har skrivit i README.md.
    • Alla test är gröna.
    • Högre kvalitet och kod som återanvänds.
    • User stories som täcker in vyn Statistik.
    • Du använder designmönstret Page Object.
    • Du använder Scenario Outline.
    • Dina features försöker täcka alla meningsfulla möjligheter för motsvarande user story.
</pre>
<br>

### Projektstruktur
<pre>
projekt
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
    │   test_book_store_fav.py
    │
    └───unit
        test_book_store.py
        test_fav_books.py
</pre>