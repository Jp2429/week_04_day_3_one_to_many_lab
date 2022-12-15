from flask import Flask, render_template, redirect, request, Blueprint
from models.book import Book
from models.author import Author

from repositories import book_repository
from repositories import author_repository

books_blueprint = Blueprint("books", __name__)

# select all books
@books_blueprint.route("/books")
def index():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)


# select single book
@books_blueprint.route("/books/<id>")
def show(id):
    book = book_repository.select(id)
    return render_template("/books/show_book.html", book=book)


# delete
@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def destroy(id):
    book_repository.delete(id)
    return redirect ("/books")


# new book
@books_blueprint.route("/books/new_book")
def new_book():
    all_authors = author_repository.select_all()
    return render_template("books/new_book.html", all_authors= all_authors)


# create book
@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, author)
    book_repository.save(book)
    return redirect('/books')


# edit book
@books_blueprint.route("/books/<id>/edit_book")
def edit(id):
    book = book_repository.select(id)
    authors = author_repository.select_all()
    return render_template("/books/edit_book.html", book=book, all_authors=authors)


# update book
@books_blueprint.route("/books/<id>/edit_book", methods=['POST'])
def update(id):
    title = request.form['title']
    author_id = request.form['author_id']
    author = author_repository.select(author_id)
    book = Book(title, author, id)
    book_repository.update(book)
    return redirect('/books')