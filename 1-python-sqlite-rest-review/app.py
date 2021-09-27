from flask import Flask, render_template

# Initializing flak application
app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html", title="Home")


# Add Review
@app.route("/addReview")
def addReview():
    return render_template("addReview.html", title="Add Review")

# Get Review & Show Review
@app.route("/getReview")
def getReview():
    return render_template("getReview.html", title="Get & Show Review")


# Show Report
@app.route("/topRestaurant")
def topRestaurant():
    return render_template("showReport.html", title="Show Report" )



if __name__ == "__main__":
    app.run(debug=True)
