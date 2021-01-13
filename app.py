from flask import Flask
from sqmodels import connect
from views.views import library_view, book_details_view, delete_view


app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/library/", methods=["GET", "POST"])
def library():
    return library_view()


@app.route("/library/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    return book_details_view(book_id)


@app.route("/library/delete/<int:book_id>/", methods=["GET", "POST"])
def delete(book_id):
    return delete_view(book_id)


if __name__ == "__main__":
    app.run(debug=True)
    connect("library.db")
