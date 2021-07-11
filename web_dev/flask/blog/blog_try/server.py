from flask import Flask, render_template
import random
from datetime import datetime as dt
import requests

app= Flask(__name__)

#///////////////////////////
params= {
    'name': 'prince',
}
genderize_response= requests.get(url='https://api.genderize.io/', params=params).json()
gender= genderize_response['gender']

agify_response= requests.get(url='https://api.agify.io/', params=params).json()
avg_age= agify_response['age']
#//////////////////////////////

@app.route('/')
def home():
    return render_template('index.html',
                           n=random.randint(1,11),
                           year=dt.now().year,)

@app.route('/guess/<string:name>')
def guess(name):
    #///////////////////////////
    params= {
        'name': name,
    }
    genderize_response= requests.get(url='https://api.genderize.io/', params=params).json()
    gender= genderize_response['gender']

    agify_response= requests.get(url='https://api.agify.io/', params=params).json()
    avg_age= agify_response['age']
    #//////////////////////////////
    return render_template('guess.html',
                            name=name,
                            gender=gender,
                            avg_age=avg_age)   

@app.route('/blog')
def blog():
    BLOG_URL= 'https://api.npoint.io/68fe828830bdab08bc8b'
    data= requests.get(url=BLOG_URL).json()
    return render_template('blog.html',
                            blogs=data,)


if __name__ == '__main__':
    app.run(debug=True)
