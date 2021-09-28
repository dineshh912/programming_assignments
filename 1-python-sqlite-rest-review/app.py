from flask import Flask, render_template, request, flash
from setup import create_connection
from datetime import datetime



# Initializing flak application
app = Flask(__name__)

# Initialize database
database = "reviewData.db"


# Home page
@app.route("/")
def index():
    return render_template("index.html", title="Home")


# Add Review
@app.route("/addReview", methods=["POST", "GET"])
def addReview():
    if request.method == "POST":
        try:
            # Get all form inputs
            username = request.form["username"]
            restaurant = request.form["restaurant"]
            food = request.form["food"]
            service = request.form["service"]
            ambience = request.form["ambience"]
            price = request.form["price"]
            overall = request.form["overall"]
            review = request.form["review"]
            # Establish connection
            conn = create_connection(database)
            curs = conn.cursor()
            curs.execute("INSERT INTO reviews (username, Restaurant, ReviewTime, Rating, Review) VALUES (?,?,?,?,?)",
                            (username, restaurant, datetime.now(), overall, review))

            curs.execute("INSERT INTO RATINGS (Restaurant, Food, Service, Ambience, Price, Overall) VALUES (?,?,?,?,?,?)",
                            (restaurant, food, service, ambience, price, overall))
            conn.commit()
            conn.close()
            flash("Review added successfully")
        except:
            conn.rollback()
            conn.close()
            flash("unable to inset review")
        finally:
            return render_template("addReview.html", title="Add Review")
    return render_template("addReview.html", title="Add Review")

# Get Review & Show Review
@app.route("/getReview", methods=["POST", "GET"])
def getReview():
    if request.method == "POST":
        try:
            restaurant = request.form["restaurant"]

            conn = create_connection(database)
            pass
        except:
            pass
        finally:
            return render_template("showReviews.html", data=data)
    return render_template("getReview.html", title="Get & Show Review")


# Show Report
@app.route("/topRestaurant")
def topRestaurant():
    return render_template("showReport.html", title="Show Report" )



if __name__ == "__main__":
    app.run(debug=True)
