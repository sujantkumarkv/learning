from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators
from flask_ckeditor import CKEditorField

##WTForm
class BlogPostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[validators.DataRequired()])
    subtitle = StringField("Subtitle", validators=[validators.DataRequired()])
    author = StringField("Your Name", validators=[validators.DataRequired()])
    img_url = StringField("Blog Image URL", validators=[validators.DataRequired(), validators.URL()])
    body = CKEditorField("Blog Content", validators=[validators.DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    name= StringField("Your Name", validators=[validators.DataRequired()])
    email= StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password= PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=8)])
    submit= SubmitField("Register")

class LoginForm(FlaskForm):
    email= StringField("Email", validators=[validators.DataRequired(), validators.Email()])
    password= PasswordField("Password", validators=[validators.DataRequired(), validators.Length(min=8)])
    submit= SubmitField("Let me In")