```
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
│       │   startsida.feature
│       │   statistics.feature
│       │
│       └───pages
│       │       base_page.py
│       │
│       └───steps
│               step_add_book.py
│               step_startsida.py
│               step_statistics.py 
│   
└───tests
│   │
│   └───integration
│   │       test_book_store_fav.py
│   │
│   └───unit
│           test_book_store.py
│           test_fav_books.py
```