from flask import Flask, render_template, redirect
from models.book import Book
from models.author import Author

from repositories import book_repository
from repositories import author_repository
from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def index():
    books = book_repository.select_all()
    return render_template("books/index.html", all_books=books)

@books_blueprint.route("/books/<id>/delete", methods=['POST'])
def destroy(id):
    books = book_repository.delete(id)
    return redirect ("/books")