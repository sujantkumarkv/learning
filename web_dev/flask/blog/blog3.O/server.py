from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

##Now we use DB not npoint online API ;)
# import requests
# posts= requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = "b'\x80\xa5\xe2\x17;\xadv'"
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(51), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class BlogPostForm(FlaskForm):
    title = StringField("Blog Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def home():
    posts= db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:id>')
def show_blogpost(id):
    selected_post= None #in case somethin' goes wrong, we don't wanna break code but return 'None' that's why.
    selected_post= BlogPost.query.get(id)
    return render_template('post.html', post=selected_post) 

@app.route('/new-post', methods=['GET','POST'])
def new_post():
    new_post_form= BlogPostForm()
    if new_post_form.validate_on_submit():
        new_post_data= request.form
        new_post= BlogPost(title=new_post_data.get('title'),
                            subtitle=new_post_data.get('subtitle'),
                            author=new_post_data.get('author'),
                            img_url=new_post_data.get('img_url'),
                            body=new_post_data.get('body'),
                            date=date.today().strftime("%B %d, %Y"),
                        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("make_post.html", form=new_post_form, to_edit=False)

@app.route('/edit-post/<int:id>', methods=['GET','POST'])
def edit(id):
    selected_post= BlogPost.query.get(id)
    edit_post_form= BlogPostForm(title=selected_post.title,
                                subtitle=selected_post.subtitle,
                                author=selected_post.author,
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
        return redirect(url_for('show_blogpost', id=selected_post.id))

    return render_template("make_post.html", form=edit_post_form, to_edit=True)



@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        #data= request.form
        name= request.form['name']
        email= request.form['email']
        phone= request.form['phone']
        msg= request.form['message']
        #print(f"{name} \n{email} \n{phone} \n{msg}")
        send_mail(name=name, email=email, message=msg, phone=phone)
        return render_template('contact.html', msg_heading='Sent successfully', msg_subheading='I\'ll get to U ASAP..')

    return render_template('contact.html', msg_heading='Contact Me', msg_subheading='Have questions? I have answers.')

if __name__ == "__main__":
    app.run(debug=True)