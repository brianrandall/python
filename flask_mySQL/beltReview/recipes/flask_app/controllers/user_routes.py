# controllers.py
import re
from flask_app import app, bcrypt
from flask import render_template,redirect,request,session
from flask_app.models.users import User
from flask_app.models.recipes import Recipe

# @app.route below

@app.route("/")
def index():
    return render_template("index.html")
            

@app.route('/create_user', methods=["POST"])
def create_user():
    
    if not User.validate_new_user(request.form):
        return redirect('/')

    hashed_password = bcrypt.generate_password_hash(request.form['password'])
    data={**request.form, 'password':hashed_password}
    session_userid=User.create(data)
    session['session_userid'] = session_userid
    return redirect('/home')

@app.route('/user_login', methods=['post'])
def user_login():
    
    if not User.validate_login(request.form):
        return redirect('/')
    
    return redirect('/home')

@app.route('/home')
def display_all_recipes():

    user = User.get_one({'id':session['session_userid']})
    recipes = Recipe.get_all()
    return render_template('all_recipes.html', recipes = recipes, user = user)

@app.route('/user_logout') 
def user_logout():
    if 'session_userid' in session: 
        del session['session_userid']
    return redirect('/')

#  ______ 
# < PYTHON ROXX >
#  ------ 
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#              u ||----w |
#                 ||     ||