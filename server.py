
## have two route, first route is a wait page. on page have JS do an ajax call as soon as page loads to get second route results 
### 
##############################################################################

from jinja2 import StrictUndefined
from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from datetime import datetime
from yelpapi import YelpAPI 
from pprint import pprint
import os 
import yelp_results
import json

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")

# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
app.jinja_env.undefined = StrictUndefined



@app.route('/')
def index():
	"""Render homepage plus search field for location."""

	return render_template("homepage.html")



@app.route("/process_search", methods=["GET"])
def search_process():
	"""Process the search and show results"""
	
	location = request.args.get('location')
	term = request.args.get('term')
	datestring = request.args.get('date')

	print "date", type(datestring)
	print "location", location

	yelp_result = yelp_results.get_business_results(location, term)
	
	return render_template("search_results.html", location=location,yelp_result=yelp_result)



if __name__ == "__main__":
	# We have to set debug=True here, since it has to be True at the point
	# that we invoke the DebugToolbarExtension
	

	# connect_to_db(app, os.environ.get("DATABASE_URL"))
	# db.create_all(app=app)

	DEBUG = "NO_DEBUG" not in os.environ
	PORT = int(os.environ.get("PORT", 5000))
	
	app.run(host="0.0.0.0", port=PORT, debug=False)


	# Use the DebugToolbar
	# DebugToolbarExtension(app)

	

