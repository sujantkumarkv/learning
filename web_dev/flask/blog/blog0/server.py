from flask import Flask, render_template
import requests

app = Flask(__name__)
BLOG_URL= 'https://api.npoint.io/68fe828830bdab08bc8b' #npoint.io API service :)
data= requests.get(url=BLOG_URL).json()

@app.route('/')
def home():
    return render_template('index.html', blogs=data)

@app.route('/blog/<int:id>')
def blogpost(id):
    return render_template('blogpost.html', blog=data[id])
    #id is set from '0' so we can directly pass on the 
    #blog to be rendered by sending that specific piece 
    #since we made it a list in npoint.io...

if __name__ == "__main__":
    app.run(debug=True)
