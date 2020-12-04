from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    author = StringField("author", validators=[DataRequired()])
    pages = IntegerField("pages", validators=[DataRequired()])
    description = TextAreaField("description")
    price = FloatField("price", validators=[DataRequired()])

