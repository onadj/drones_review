import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'drones2020'
app.config["MONGO_URI"] = 'mongodb+srv://onadj:Signacare2020@myfirstcluster-hbcie.mongodb.net/drones2020?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_reviews')
def get_reviews():
    return render_template("drones_review.html", reviews=mongo.db.reviews.find())

@app.route('/add_review')
def add_review():
    return render_template('add_drones_review.html' ,
                           categories=mongo.db.categories.find())

@app.route('/insert_review', methods=['POST'])
def insert_review():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('get_reviews'))

if __name__ == '__main__':
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)