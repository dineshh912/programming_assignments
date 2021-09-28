# importing python packages
from flask import Flask, render_template, request
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
            message = "Review added successfully"
        except:
            # If any error during insert operation
            conn.rollback()
            conn.close()
            message = "unable to inset review"
        finally:
            # After inserting the values into database
            return render_template("addReview.html", title="Add Review", message=message)
    return render_template("addReview.html", title="Add Review")

# Get Review & Show Review
@app.route("/getReview", methods=["POST", "GET"])
def getReview():
    if request.method == "POST":
        try:
            # Get values from form
            restaurant = request.form["restaurant"]
            # Establish connection to the database
            conn = create_connection(database)
            cursor = conn.cursor()
            cursor.execute(f'''SELECT DISTINCT a.username, a.Restaurant, a.Rating, a.Review, a.ReviewTime,
                                b.Food, b.Service, b.Ambience, b.Price from reviews as a, ratings as b 
                                where a.Restaurant == '{restaurant}' and a.Restaurant == b.Restaurant''')
            # Save retrived value
            data = cursor.fetchall()
            # If there is no restruant in the table
            if len(data) != 0:
                return render_template("showReviews.html", data=data)
            else:
                msg = f"Unable to find review for the restraunt {restaurant}"
                return render_template("showReviews.html", msg=msg)
        except Exception as e:
            print(str(e))
    return render_template("getReview.html", title="Get & Show Review")


# Show Report
@app.route("/topRestaurant")
def topRestaurant():
    # Establish connection
    conn = create_connection(database)
    cursor = conn.cursor()
    cursor.execute('''select DISTINCT a.Restaurant, b.Food, b.Service,
                    b.Ambience, b.Price, a.Rating from reviews as a, ratings as b
                    WHERE a.Restaurant == b.Restaurant ORDER BY a.Rating DESC''')
    data = cursor.fetchall()

    return render_template("showReport.html", title="Show Report", data=data)



if __name__ == "__main__":
    app.run()
