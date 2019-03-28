from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 
from flask_heroku import Heroku 

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://bxsswwybqhvhic:b2fddf8a534912f868473b8fe9e66f66e153dbb02febfe1cb8b7041bfa11cb70@ec2-23-23-241-119.compute-1.amazonaws.com:5432/d4ibc8jtbqqp86'

heroku = Heroku(app)
db = SQLAlchemy(app)

class Goodies(db.Model):
    __tablename__ ="goodies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    summary = db.Column(db.String(80))
    cost = db.Column(db.String(10))
    goodieType = db.Column(db.String(40))
    quantity = db.Column(db.String(4))
    

    def __init__(self, title, summary, cost, goodieType, quantity):
        self.title = title
        self.summary = summary
        self.cost = cost
        self.goodieType = goodieType
        self.quantity = quantity

    def __repr__(self):
        return '<Title %r>' % self.title
    #     # This is string interpalation in python
    #     # the % self.title is setting a value to %r


@app.route("/")
def home():
    return "<h1>Hello World</h1>"



@app.route('/goodie/input', methods=['POST'])
def goodies_input():
    if request.content_type == 'application/json':
        post_data = request.get_json()

        title = post_data.get('title')
        cost = post_data.get('cost')
        goodieType = post_data.get('goodieType')
        summary = post_data.get('summary')
        quantity = post_data.get('quantity')

        reg = Goodies(title, summary, cost, goodieType, quantity)
        db.session.add(reg)
        db.session.commit()
        return jsonify("Data Posted")
    return jsonify("Something went wrong")


@app.route('/goodies', methods=['GET'])
def return_goodies():
    all_goodies = db.session.query(Goodies.id, Goodies.title, Goodies.summary, Goodies.cost, Goodies.goodieType, Goodies.quantity).all()
    return jsonify(all_goodies)

@app.route('/goodie/<id>', methods = ['GET'])
def return_single_goodie(id):
    one_goodie = db.session.query(Goodies.id, Goodies.title, Goodies.summary, Goodies.cost, Goodies.goodieType, Goodies.quantity).filter(Goodies.id == id).first()
    return jsonify(one_goodie)

@app.route('/delete/<id>', methods=['DELETE'])
def goodie_delete(id):
    if request.content_type == 'application/json':
        record = db.session.query(Goodies).get(id)
        db.session.delete(record)
        db.session.commit()
        return jsonify("Completed Delete Mehtod")
    return jsonify("Delete Failed")

@app.route('/search/<title>', methods=['GET'])
def goodies_search(title):
    search_goodies = db.session.query(Goodies.id, Goodies.title, Goodies.cost, Goodies.goodieType, Goodies.summary, Goodies.quantity).filter(Goodies.title == title).first()

    return jsonify(search_goodies)

if __name__ == '__main__':
    app.debug = True
    app.run()

















# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy 
# from flask_cors import CORS 
# from flask_heroku import Heroku 

# app = Flask(__name__)
# CORS(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://tlbjnprzxwowva:db0bc8667316928abf4ac3f261690a8459d0f33b1128149b9511ad0fe4daaa66@ec2-54-163-234-88.compute-1.amazonaws.com:5432/d3b8cct3rntuim'

# heroku = Heroku(app)
# db = SQLAlchemy(app)

# class Book(db.Model):
#     __tablename__ ="books"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(120))
#     author = db.Column(db.String(80))

#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __repr__(self):
#         return '<Title %r>' % self.title
#         # This is string interpalation in python
#         # the % self.title is setting a value to %r


# @app.route("/")
# def home():
#     return "<h1>Hello World</h1>"


# @app.route('/book/input', methods=['POST'])
# def books_input():
#     if request.content_type == 'application/json':
#         post_data = request.get_json()
#         title = post_data.get('title')
#         author = post_data.get('author')
#         reg = Book(title, author)
#         db.session.add(reg)
#         db.session.commit()
#         return jsonify("Data Posted")
#     return jsonify("Something went wrong")


# @app.route('/books', methods=['GET'])
# def return_books():
#     all_books = db.session.query(Book.id, Book.title, Book.author).all()
#     return jsonify(all_books)

# @app.route('/book/<id>', methods = ['GET'])
# def return_single_book(id):
#     one_book = db.session.query(Book.id, Book.title, Book.author).filter(Book.id == id).first()
#     return jsonify(one_book)

# @app.route('/delete/<id>', methods=['DELETE'])
# def book_delete(id):
#     if request.content_type == 'application/json':
#         record = db.session.query(Book).get(id)
#         db.session.delete(record)
#         db.session.commit()
#         return jsonify("Completed Delete Mehtod")
#     return jsonify("Delete Failed")

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
