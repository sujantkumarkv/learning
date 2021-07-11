from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import fields, validators
from flask_bootstrap import Bootstrap

app= Flask(__name__)
Bootstrap(app)
app.secret_key= "foff"

#--------------- FORMS -------------------
class LoginForm(FlaskForm):
    email= fields.StringField(label='email',
                            validators=[validators.DataRequired(message="Must input smthng"), 
                                        validators.Email(granular_message=True, check_deliverability=True)])
    password= fields.PasswordField(label='password',
                                    validators=[validators.DataRequired(message="must input smthng"),
                                                validators.Length(min=8, message="Must be 8 characters long")])
    submit= fields.SubmitField(label='LogIn')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    loginform= LoginForm()
    if loginform.validate_on_submit():#EQV to request.method=='POST'
        if loginform.email.data=="abc@xyz.com" and loginform.password.data=="sodabokugakirada": 
            return render_template('loginsuccess.html')
        else:
            return render_template('logindenied.html')
    return render_template('login.html', form=loginform)

if __name__ == "__main__":
    app.run(debug=True)




