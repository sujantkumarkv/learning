from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

#app
app = Flask(__name__)
app.config['SECRET_KEY'] = "b'\x80\xa5\xe2\x17;\xadv'" #generated with os.urandom(7)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(101), unique=True)
    password = db.Column(db.String(101))
    name = db.Column(db.String(501))
#Line below only required once, when creating DB. 
#db.create_all()

#managing user-login sessions
login_manager= LoginManager()
login_manager.init_app(app=app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    #When the user is authenticated & loggedIn, we dont wanna render the login/Register buttons on navbar
    #so, we pass on the user_logged_in state to the pages
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        hashed_password= hashing(password=request.form['password'])    
        new_user= User(name=request.form['name'],
                        email=request.form['email'],
                        password=hashed_password,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError: #from sqlalchemy.exc import IntegrityError (github user's help)
            flash(message='User exits. Try with a different one !!')
            return redirect(url_for('register'))

        #login & authenticate user after adding into DB
        login_user(new_user)
        return redirect(url_for('secrets'))

    return render_template("register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        the_user=User.query.filter_by(email=request.form['email']).first()
        
        if not the_user:
            flash("No such User exists. Sorry, try again !!")
            return redirect(url_for('login'))

        elif not check_password_hash(pwhash=the_user.password, password=request.form['password']):
            flash("Wrong Password !! Try again.. ")
            return redirect(url_for('login'))
        
        else:
            login_user(the_user)
            return redirect(url_for('secrets'))

    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    #print(current_user.name)
    return render_template("secrets.html", user=current_user)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required 
def download():
    filepath='files/cheat_sheet.pdf'
    return send_from_directory(directory='static',
                                path=filepath,
                                as_attachment=True)

def hashing(password):
    hpassword= generate_password_hash(password=password,
                                                method='pbkdf2:sha256',
                                                salt_length=7)
    return hpassword

if __name__ == "__main__":
    app.run(debug=True)
