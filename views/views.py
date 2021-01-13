from forms.forms import BookForm
from flask import request, render_template, redirect, url_for
from sqmodels import bookstore


def library_view():
    form = BookForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            bookstore.create(form.data)
            bookstore.save_all()
        return redirect(url_for("library"))
    return render_template("library.html", form=form, library=bookstore.all(), error=error)


def book_details_view(book_id):
    book = bookstore.get(book_id)
    form = BookForm()
    if request.method == "POST":
        if form.validate_on_submit():
            bookstore.update(book_id, form.data)
            bookstore.save_all()
        return redirect(url_for("library"))
    return render_template("book.html", form=form, book=book, book_id=book_id)


def delete_view(book_id):
    if request.method == "POST":
        bookstore.delete(book_id)
        bookstore.save_all()
        return redirect(url_for("library"))
    return render_template("delete.html")
