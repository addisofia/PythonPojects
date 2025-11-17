#from crypt import methods

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating out of 10", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title= StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

# CREATE DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///MovieList.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    __tablename__ = "movie"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    year: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[float] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(nullable=False)
    img_url: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<Movies {self.title} - {self.rating}>"

with app.app_context():
    db.create_all()

new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
            )
"""
second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
            )
with app.app_context():
    db.session.add(new_movie)
    db.session.add(second_movie)
    db.session.commit()

"""

@app.route("/",methods=['POST','GET'])
def home():
    #all_movies=Movie.query.all() the 2 command below it's the some!
    all_movies=db.session.execute(db.select(Movie)).scalars().all()
    return render_template("index.html",all_movies=all_movies)


@app.route("/edit/<int:id>",methods=['POST','GET'])
def edit(id):
    movie = db.get_or_404(Movie, id)  #movie=Movie.query.get_or_404(id) encien methode with query object
    form=RateMovieForm()
    if form.validate_on_submit():  #request.method == "POST" validate empeche d'enregister des données vide ou invalide
        movie.rating=float(form.rating.data) # =request.form.get('rating') c'est la methode basique sans WTform
        movie.review=form.rating.data
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("edit.html",form=form,movie=movie)


@app.route("/delete",methods=['POST','GET'])
def delete():
    movie_id = request.args.get("id") # get the id from the url by using request
    movie=db.get_or_404(Movie,movie_id)
    db.session.delete(movie)
    db.session.commit()

    return render_template("index.html")

@app.route("/add",methods=['POST','GET'])
def add():
    form=AddMovieForm()
    if form.validate_on_submit():
        title=form.title.data

    return render_template("add.html",form=form)



if __name__ == '__main__':

    app.run(debug=True)

