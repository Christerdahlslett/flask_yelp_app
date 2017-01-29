# Importing libaries. 

from flask import Flask, render_template, request
import yelp_script
import os

# And crating an instance of this class. 
app = Flask(__name__)

# The route() decorator tells Flask what URL should trigger our function.
# We define a varaibel called location, which requests the location from the user.
# Location is the argument our yelp_script.py function need to run. 
# We use an if-statement so we can show the recommendation only when a location is given.
# This is done by running the function from our yelp_script.py with the location requested earlier. 
# if there is no input of location there will be no recommendation given. 
# Then we return this to the index.html page, and we define what this should be called in the html document
# so we can call upon it there. 

# Last we have an if statement that runs the script. 

@app.route("/")
def index():
    location = request.values.get("location")
    if location:
        recommendation = yelp_script.get_businesses(location)
    else:
        recommendation = None
    return render_template("index.html", recommendation=recommendation)

if __name__ == "__main__":
    app.run()















