import re
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.users import User
from flask_app.models.recipes import Recipe


@app.route('/recipes/new')
def add_recipe():
    return render_template('add_recipe.html')

@app.route('/recipes/new/process', methods = ['post'])
def add_recipe_to_db():
    if not Recipe.validate_recipe(request.form):
        return redirect ('/recipes/new')

    Recipe.create(request.form)
    return redirect('/home')

@app.route('/recipes/edit/<int:id>')
def edit (id):
    recipes = Recipe.get_one({"id": id})
    return render_template("edit_recipe.html", recipes = recipes)

@app.route('/recipes/edit/process', methods=['post'])
def edit_recipe ():
    print(request.form)
    Recipe.update(request.form)
    return redirect('/home')

@app.route('/recipes/<int:id>')
def show (id):
    recipes = Recipe.get_one({'id': id})
    print(recipes.user_id)
    return render_template("one_recipe.html", recipes = recipes)


@app.route('/recipes/delete/<int:id>')
def delete(id):
    
    recipes = Recipe.delete({'id':id})
    return redirect('/home')
