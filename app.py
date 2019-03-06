from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 
from flask_heroku import Heroku 

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tlbjnprzxwowva:db0bc8667316928abf4ac3f261690a8459d0f33b1128149b9511ad0fe4daaa66@ec2-54-163-234-88.compute-1.amazonaws.com:5432/d3b8cct3rntuim'

heroku = Heroku(app)
db = SQLAlchemy(app)

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Interger, primary_key = True) # a bunch of exel sheets you cant look at, id is a column that exepts a integer, uniqe id number 
    title = db.Column(db.String(120))
    author = db.Column(db.String(80)) # needs to have a data base if your working with columns 

    def __inti__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self): # repr build in python method 
        return '<Title %r>' % self.title # the second % is what actully gets shown, anouther way of doing string interpalation 


@app.route('/')
def home():
    return "<h1>Hi from Flask</h1>"

@app.route('/book/input', methods = ['POST'])
def books_input():
    if request.content_type == 'application/json':
        post_data = request.get_json()
        title = post_data.get('title')
        author = post_data.get('author')
        reg = Book(title, author)
        db.session.add(reg)
        db.session.commit()
        return jsonify("Data Posted")
    return jsonify('Somethings amiss')

if __name__ == '__main__':
    app.debug = True
    app.run()