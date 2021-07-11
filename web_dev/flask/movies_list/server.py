from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import fields, validators
import requests, time

#themoviedb API
TMDB_API= 'cbae2017c8f36c7842741ae80f01a51f'
TMDB_SEARCH_URL= 'https://api.themoviedb.org/3/search/movie'
TMDB_MOVIE_DETAILS_URL= 'https://api.themoviedb.org/3/movie'
TMDB_MOVIE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

#app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

#DATABASE
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
db= SQLAlchemy(app=app)

#----------------------- FORMS ---------------------------
class EditMovieForm(FlaskForm):
    rating= fields.StringField(label="Add Rating(out of 10)", validators=[validators.NumberRange(max=10.0)])
    review= fields.StringField(label="Add Review")
    submit= fields.SubmitField(label="Submit")

class AddMovieForm(FlaskForm):
    moviename= fields.StringField(label="Add name of movie", validators=[validators.DataRequired()])
    add= fields.SubmitField(label="Add")

#creating table in database
class Movies(db.Model):
    id= db.Column(db.INTEGER, primary_key=True)
    title= db.Column(db.String(501), nullable=True, unique=False)
    year= db.Column(db.INTEGER, nullable=True, unique=False)
    description= db.Column(db.String(100001), nullable=True, unique=False)
    rating= db.Column(db.FLOAT, nullable=True, unique=False)
    ranking= db.Column(db.INTEGER, nullable=True, unique=True)
    review= db.Column(db.String(10001), nullable=True, unique=False)
    img_url= db.Column(db.String(10001), nullable=True, unique=False) 
'''db.create_all()

#adding data
new_movie= Movies(title="BigHero6",
                year=2014,
                description="Story of a young Robotics prodigy named Hero\
                            & a robot Baymax.Together they have an incredible journey & forming a deep friendship",
                rating=9.5,
                ranking=1,
                review="Just stop everything & watch this.",
                img_url="https://bit.ly/35Yrlee", #shortened          
)
db.session.add(new_movie)
db.session.commit()'''

#Writing it here outside the home() didnt' allowed data to be updated from the database.
#ALL_MOVIES= db.session.query(Movies).all()

@app.route("/")
def home():
    ALL_MOVIES= db.session.query(Movies).all()
    return render_template("index.html", movies=ALL_MOVIES)

@app.route("/edit", methods=['POST','GET'])
def edit_movie():
    form= EditMovieForm()
    #movie_id= request.args.get('id')
    movie= Movies.query.get(request.args.get('id'))#getting movie from DB tho' id from URL.

    if request.method=='POST': #EQV to request.method=='POST'
        #--- SECTION 1 : UPDATING OF EXISTING DATA ---
        new_rating= form.rating.data
        new_review= form.review.data
        #update only if smthng is entered, maybe user dont wanna update just clicked :)
        if new_rating != "":
            movie.rating= float(new_rating)
        if new_review != "":
            movie.review= new_review
        '''
        movie.rating = float(form.rating.data)
        movie.review = form.review.data '''
        db.session.commit()
        time.sleep(3)
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete", methods=['POST','GET'])
def delete_movie():
    movie= Movies.query.get(request.args.get("id"))
    if request.method=='POST':
        db.session.delete(movie)
        db.session.commit()
        time.sleep(3)
        return redirect(url_for('home'))
    return render_template("delete.html", movie=movie)
    
@app.route("/add", methods=['POST','GET'])
def add_movie():
    add_form= AddMovieForm()
    if request.method=='POST':
        movie= add_form.moviename.data #get the movie entered by user from moviename(I named it above)
        tmdb_params={
            "query": movie,
            "api_key": TMDB_API,
        }
        movies_data= requests.get(url=TMDB_SEARCH_URL, params=tmdb_params).json()['results'] #its a list of movies'
        return render_template("select.html", movies_data=movies_data)

    return render_template("add.html", form=add_form)

@app.route("/find")
def find_movie():
    '''The original API URL had title, year, img_url data too,kinda we dont need find_movie() if we didnt return
        the select.html template, after smthng is selected in select.html, we gotta transfer it back to update 
        in database but thats a return statement, also it would be confusing in the same function PLUS
        we need the movie name also for the 1st API URL, we can pass it but would make code more messy...'''

    movie_id= request.args.get('movie_id')
    if movie_id:
        movie_data= requests.get(url=f"{TMDB_MOVIE_DETAILS_URL}/{movie_id}", params={"api_key":TMDB_API}).json()
        new_movie= Movies(
                        title=movie_data['title'],
                        year=movie_data['release_date'].split("-")[0],
                        description=movie_data['overview'],
                        img_url=f"{TMDB_MOVIE_IMAGE_URL}{movie_data['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit_movie', id=new_movie.id)) #since title, year etc is updated in DB, so id is
                                                                #generated automatically & can be used :)

if __name__ == '__main__':
    app.run(debug=True)
