# controllers.py
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def root():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos = dojos)

@app.route('/add_new_dojo', methods=['post'])
def create_dojo():
    dojo = Dojo.create(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojos(id):
    dojo = Dojo.get_one({'id':id})
    ninjas = Ninja.get_one_dojo_id({'dojo_id':id})
    return render_template('one_dojo.html', dojo = dojo, ninjas = ninjas)
