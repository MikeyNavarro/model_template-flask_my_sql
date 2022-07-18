from flask import render_template,redirect,request
from flask_app import app

# Change Burger to your specific model 

from flask_app.models.dojo import Dojo

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')
