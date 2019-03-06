from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hi from Flask</h1>"

if __name__ == '__main__':
    app.debug = True
    app.run()