from flask import Flask, request, render_template, redirect, url_for
from forms import BookForm
from models import bookstore


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/library/", methods=["GET", "POST"])
def library():
    form = BookForm()
    if request == "POST":
        if form.validate_on_submit():
            bookstore.create(form.data)
            bookstore.save_all()
        return redirect(url_for("library"))
    return render_template("library.html", form=form, library=bookstore.allitems)


@app.route("/library/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = bookstore.get(book_id - 1)
    form = BookForm()

    if request.method == "POST":
        if form.validate_on_submit():
            bookstore.update(book_id, form.data)
        return redirect(url_for("library"))
    return render_template("book.html", form=form, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)

