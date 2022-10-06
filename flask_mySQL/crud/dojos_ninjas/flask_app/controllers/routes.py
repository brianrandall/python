# controllers.py
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo_ninja import Dojo, Ninja

@app.route('/')
def root():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html')

@app.route('/add_new_dojo', method=['post'])
def create_dojo():
    return redirect('/dojos')

@app.route('/ninjas')
def ninjas():
    return render_template('new_ninja.html')

@app.route('/create_new_ninja', method=['post'])
def create_ninja():
    return redirect('/dojos')
