from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template('new_ninja.html', dojos = Dojo.get_all())

@app.route('/create_new_ninja', methods=['post'])
def create_ninja():
    ninja = Ninja.create(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")