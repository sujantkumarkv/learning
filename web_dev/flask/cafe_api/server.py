from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rd

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to silence deprecation warnings.
db = SQLAlchemy()
db.__init__(app)

##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

#We see later,the data from database is an object & doesnt directly converts to dict.
#So, explicitly defining a func that converts it to dict.
def to_dict(self):
    cafe_dict= {}
    for column in self.__table__.columns:
        col_name= column.name
        value= getattr(self, column.name)
        cafe_dict[col_name]= value
    return cafe_dict
    #return {column.name: getattr(self, column.name) for column in self.__table__.columns}

@app.route("/")
def home():
    return render_template("index.html")
    
## HTTP GET - Read Record
@app.route('/random', methods=['GET', 'POST'])
def random():
    cafe_id= rd.randint(1, 21)
    cafe= Cafe.query.get(cafe_id)
    return jsonify( id=cafe_id,
                    name=cafe.name,
                    location=cafe.location,
                    coffee_price=cafe.coffee_price,
                    seats=cafe.seats,
                    img_url=cafe.img_url,
                    map_url=cafe.map_url,
                    has_wifi=cafe.has_wifi,
                    has_sockets=cafe.has_sockets,
                    can_take_calls=cafe.can_take_calls,
                    has_toilet=cafe.has_toilet,
                    )

@app.route('/all')
def all_cafes():
    cafes_list=[]
    cafes= db.session.query(Cafe).all()
    for cafe in cafes:
        '''Can be done this way but not a great approach,as it would be impossible to do
            this way in LARGE DATABASE also exposes the data columns & structure in code.
        each_cafe= {
                    'id':cafe.id,'name':cafe.name,'location':cafe.location,'coffee_price':cafe.coffee_price,
                    'seats':cafe.seats,'img_url':cafe.img_url,'map_url':cafe.map_url,'has_wifi':cafe.has_wifi,
                    'has_sockets':cafe.has_sockets,'can_take_calls':cafe.can_take_calls,'has_toilet':cafe.has_toilet,
        }'''
        cafes_list.append(to_dict(cafe))
    return jsonify(cafes=cafes_list)

@app.route("/search", methods=['POST', 'GET'])
def search():
    return_data= None
    loc= request.args.get('loc')
    cafes= db.session.query(Cafe).all()
    cafes_list=[]
    for cafe in cafes:
        if cafe.location.lower() == loc.lower():
            cafes_list.append(to_dict(cafe))

    if len(cafes_list) ==0:
        error_msg={
                "Not Found": "We dont have a cafe at your said location. FOFF !!"
            }
        return_data= jsonify(error=error_msg)
    else:
        return_data= jsonify(cafes=cafes_list)
    return return_data
    


## HTTP POST - Create Record
@app.route('/add', methods=['POST'])
def add():
    new_cafe = Cafe(
                name=request.form.get("name"),
                map_url=request.form.get("map_url"),
                img_url=request.form.get("img_url"),
                location=request.form.get("loc"),
                #Its simple Logic. If the field is filled,its True,if empty, then False.
                #Eg, we leave in POSTMAN "sockets" field empty and get False in the database cafes.db
                has_sockets=bool(request.form.get("sockets")),
                has_toilet=bool(request.form.get("toilet")),
                has_wifi=bool(request.form.get("wifi")),
                can_take_calls=bool(request.form.get("calls")),
                seats=request.form.get("seats"),
                coffee_price=request.form.get("coffee_price"),
                )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify({"sucess":"Cafe added successfully to database ;)"})

## HTTP PUT/PATCH - Update Record
@app.route('/update-price/<int:cafe_id>', methods=['PATCH'])
def update_price(cafe_id):
    new_price= request.args.get('new_price') #get the new-price from the URL
    cafe= db.session.query(Cafe).get(cafe_id) #get the cafe to be updated from class(table)"Cafe"
    if cafe:      
        cafe.coffee_price= new_price
        db.session.commit()
        return jsonify({"sucess":"Cafe's coffee price successfully UPDATED ;)"}), 200
    else:
        #404: Resource not found
        return jsonify({"error": "Sorry your details doesnt match with our database"}), 404


## HTTP DELETE - Delete Record
TOP_SECRET_API_KEY= 'TopSecretApiKey'
@app.route('/report-closed/<int:cafe_id>', methods=['DELETE'])
def report_closed(cafe_id):
    cafe= db.session.query(Cafe).get(cafe_id)
    api_key= request.args.get('api-key')
    if api_key != TOP_SECRET_API_KEY:
        return jsonify({"error":"Not allowed. Make sure you have the right API KEY"}), 403
    if cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify({"sucess":"Cafe's data deleted ;)"}), 200
    else:
        return jsonify({"error":"No such cafe found."}), 404


if __name__ == '__main__':
    app.run(debug=True)
