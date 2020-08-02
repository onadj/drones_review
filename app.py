
import os
from flask import (Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key=os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route('/')


@app.route('/index')
def index():
    return render_template("home.html")

@app.route('/sendmail')
def sendmail():
    return render_template("sendMail.html")

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


@app.route('/edit_review/<review_id>')
def edit_review(review_id):
    the_review =  mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edit_review.html', review=the_review,
                           categories=all_categories)


@app.route('/update_review/<review_id>', methods=["POST"])
def update_review(review_id):
    reviews = mongo.db.reviews
    reviews.update( {'_id': ObjectId(review_id)},
    {
        'category_name': request.form.get('category_name'),
        'name': request.form.get('name'),
        'review': request.form.get('review')  
    })
    return redirect(url_for('get_reviews'))


@app.route('/delete_review/<review_id>')
def delete_review(review_id):
    mongo.db.reviews.remove({'_id': ObjectId(review_id)})
    return redirect(url_for('get_reviews'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)