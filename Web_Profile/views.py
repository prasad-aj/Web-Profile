import os
from flask import render_template
from web_profile_app import app


@app.route('/')
def hello_world():
	return render_template('profile_homepage.html')