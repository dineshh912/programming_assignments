# import packages
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraping


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"

# initialize PyMongo APP
mongo = PyMongo(app)

# Index page
@app.route("/")
def index():
    mars_hemisphere_image = mongo.db.data.find_one()
    return render_template("index.html", mars_img = mars_hemisphere_image)


# Adding scrap data
@app.route("/scrape_data")
def scrape_data():
    # this fucntion recall scrapping.py script and scrap the data
    mars_db = mongo.db.data
    data = scraping.scrape_all()
    mars_db.update_one({}, {"$set":data}, upsert=True)
    return redirect('/', code=302)



if __name__ == "__main__":
    app.run(debug=True)