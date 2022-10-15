import re
from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.users import User
from flask_app.models.bands import Band


@app.route('/band/new')
def add_recipe():
    return render_template('create_band.html')

@app.route('/band/new/process',methods=['post'])
def add_band_to_db():
    if not Band.validate_band(request.form):
        return redirect ('/band/new')

    Band.create(request.form)
    return redirect('/home')

@app.route('/band/edit/<int:id>')
def edit(id):
    band = Band.get_one({"id": id})
    return render_template("edit_band.html", band = band)

@app.route('/band/edit/process', methods=['post'])
def edit_band ():
    print(request.form)
    Band.update(request.form)
    return redirect('/home')

@app.route('/mybands/<int:id>')
def my_bands (id):
    user = User.get_one({'id': id})
    bands = Band.get_all()
    return render_template("my_bands.html", bands=bands, user=user)


@app.route('/band/delete/<int:id>')
def delete(id):
    Band.delete({'id': id})
    return redirect('/home')
