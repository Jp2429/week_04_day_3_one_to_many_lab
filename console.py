import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author_1 = Author("John")
author_repository.save(author_1)
author_2 = Author("Kevin Crossley-Holland")
author_repository.save(author_2)

author_test = author_repository.select_all()
for author in author_test:
    print(author.__dict__)

single_author = author_repository.select(author_1.id)
print(single_author.__dict__)


book_1 = Book("The Art of Jam Rolls", author_1)
book_repository.save(book_1)
book_2 = Book("Norse Myths", author_2)
book_repository.save(book_2)

book_test = book_repository.select_all()
for book in book_test:
    print(book.__dict__)

single_book = book_repository.select(book_1.id)
print(single_book.__dict__)



