# This is the main FLASK server file for upgrade to BLOG 2.O
from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)
BLOG_URL= 'https://api.npoint.io/07ae64d6c9a4d299cb72' #npoint.io API service :)
all_posts= requests.get(url=BLOG_URL).json()

@app.route('/')
def home():
    return render_template('index.html', all_posts=all_posts)

@app.route('/about')
def about():
    return render_template('about.html')

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

'''This was my way which is simple & lengthy, soln given is better combining both functions in contact, see above :)
@app.route('/contact', methods=['POST', 'GET'])
def contact_form():
    name= request.form['name']
    email= request.form['email']
    phone= request.form['phone']
    msg= request.form['message']
    print(f"{name} \n{email} \n{phone} \n{msg}")
    return render_template('contact.html', msg_heading='Sent successfully', msg_subheading='I\'ll get to U ASAP..')
'''

@app.route('/post/<int:id>')
def show_blogpost(id):
    selected_post= None #in case somethin' goes wrong, we don't wanna break code but return 'None' that's why.
    for post in all_posts:
        if post['id'] == id:
            selected_post= post

    return render_template('post.html', post=selected_post)  

MY_EMAIL = "yagamilight1362@gmail.com"
PASSWORD = "YAGAMIRAITOprince123#"
RECEIVER_MAIL = 'keiyagami67@gmail.com'

def send_mail(name, email, message, phone):
    mail_msg= f"Subject:Someone tryin' contact\n\n{name} with contact no- {phone} contacted you on blog site saying\n {message}"
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_MAIL, msg=mail_msg)

if __name__ == "__main__":
    app.run(debug=True)