from flask import Flask, render_template, redirect, url_for, flash, abort, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from forms import BlogPostForm, RegisterForm, LoginForm
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = "b'\x80\xa5\xe2\x17;\xadv'" #generated with os.urandom(7)
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_final.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#AdminOnly
from functools import wraps
def admin_only(func):
    '''explaining @wraps ::
        https://artemrudenko.wordpress.com/2013/04/15/python-why-you-need-to-use-wraps-with-decorators/ '''
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if current_user.is_authenticated and current_user.id == 1:
            return func(*args, **kwargs)
        else:
            return abort(403)
    return decorated_func

##CREATE users(PARENT) table in DB
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(101), unique=True)
    password = db.Column(db.String(101))
    name = db.Column(db.String(501))
    blogposts= db.relationship(argument='BlogPost') #giving parent's relationship

##Create blog_posts(CHILD) table in DB
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(51), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=True)
    author = db.Column(db.String(250), nullable=False)
    author_id= db.Column(db.Integer, db.ForeignKey('users.id')) #child's relationship
#Line below only required once, when creating DB. 
db.create_all()

@app.route('/')
def home(): 
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)

@app.route('/post/<int:post_id>')
def show_blogpost(post_id):
    selected_post= None #in case somethin' goes wrong, we don't wanna break code but return 'None' that's why.
    selected_post= BlogPost.query.get(post_id)
    return render_template('post.html', post=selected_post) 

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/new-post', methods=['GET','POST'])
@admin_only
def new_post():
    new_post_form= BlogPostForm()
    if new_post_form.validate_on_submit():
        new_post= BlogPost(title=request.form.get('title'),
                            subtitle=request.form.get('subtitle'),
                            author=request.form.get('author'),
                            author_id=current_user.id,
                            img_url=request.form.get('img_url'),
                            body=request.form.get('body'),
                            date=date.today().strftime("%B %d, %Y"),
                        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("make_post.html", form=new_post_form, to_edit=False)


@app.route("/edit-post/<int:post_id>", methods=['GET','POST'])
@admin_only
def edit_post(post_id):
    selected_post= BlogPost.query.get(post_id)
    edit_post_form= BlogPostForm(title=selected_post.title,
                                subtitle=selected_post.subtitle,
                                author=selected_post.author,
                                author_id=current_user.id,
                                body=selected_post.body,
                                img_url=selected_post.img_url,
                                )
    if edit_post_form.validate_on_submit():
        selected_post.title= request.form.get('title')
        selected_post.subtitle= request.form.get('subtitle')
        selected_post.author= request.form.get('author')
        selected_post.body= request.form.get('body')
        selected_post.img_url= request.form.get('img_url')
        
        db.session.commit()
        return redirect(url_for('show_blogpost', post_id=selected_post.id))

    return render_template("make_post.html", form=edit_post_form, to_edit=True)

'''
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
'''

##### AUTHENTICATION STUFF ######
#managing user-login sessions
login_manager= LoginManager()
login_manager.init_app(app=app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Register
@app.route('/register', methods=['GET','POST'])
def register():
    register_form= RegisterForm()
    if register_form.validate_on_submit():

        #if user already registered in the table in DB
        if User.query.filter_by(email=register_form.email.data).first():
            flash("Already registerd, try logging in instead ;)")
            return redirect(url_for('login'))
        new_user= User(
            name= register_form.name.data,
            email= register_form.email.data,
            password= hashing(register_form.password.data),
        )
        db.session.add(new_user)
        db.session.commit()
        #Log-In the registered user 
        login_user(new_user)
        return redirect(url_for('home'))       
    return render_template("register.html", register_form=register_form)

#Login
@app.route('/login', methods=['GET','POST'])
def login():
    login_form= LoginForm()
    if login_form.validate_on_submit():
        the_user=User.query.filter_by(email=login_form.email.data).first()

        if not the_user:
            flash("No such User exists. Sorry, try again !!")
            return redirect(url_for('login'))
        elif not check_password_hash(pwhash=the_user.password, password=login_form.password.data):
            flash("Wrong Password !! Try again.. ")
            return redirect(url_for('login'))       
        else:
            login_user(the_user)
            return redirect(url_for('home'))

        login_user(the_user)
        return redirect(url_for('home'))
    return render_template("login.html", login_form=login_form)

#logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

def hashing(password):
    hpassword= generate_password_hash(password=password,
                                                method='pbkdf2:sha256',
                                                salt_length=7)
    return hpassword


if __name__ == "__main__":
    app.run(debug=True)
