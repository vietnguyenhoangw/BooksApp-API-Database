# import class
from flask import Flask
from flask import Response
from flask import jsonify
from flask import g
from flask import request
from flask import make_response
import json
import sqlite3
import os

Image_FOLDER = os.path.join('static', 'image')

# data base name
DATABASE = 'database/books_db'

app = Flask(__name__, static_folder="image")

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

''' GET DATA '''
@app.route('/books',methods=["GET"])
def books_list():
    db = get_db()
    data = db.execute('SELECT * FROM books').fetchall()
    res = []
    for book in data:
        item = {
            'bookID':book[0],
            'bookName':book[1],
            'bookAuthor':book[2],
            'bookDescription':book[3],
            'bookImage':book[4]
        }
        res.append(item)
    return jsonify({
        'books': res
    })

# get test text 'hello world'
@app.route('/', methods=["GET"])
def hello():
    return "Hello World!"

# main method
# run at port 5000
if (__name__ == "__main__"):
	app.run(host='0.0.0.0',port=5000)

