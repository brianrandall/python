# controllers.py
import re
from flask_app import app, bcrypt
from flask import render_template,redirect,request,session
from flask_app.models.users import User
from flask_app.models.bands import Band

# @app.route below

@app.route("/")
def index():
    return render_template("index.html")
            

@app.route('/create_user', methods=["POST"])
def create_user():
    
    if not User.validate_new_user(request.form):
        return redirect('/')
    # //////pipenv install flask-bcrypt///////
    hashed_password = bcrypt.generate_password_hash(request.form['password'])
    data={**request.form, 'password':hashed_password}
    session_userid=User.create(data)
    session['userid'] = session_userid
    return redirect('/home')

@app.route('/user_login', methods=['post'])
def user_login():
    
    if not User.validate_login(request.form):
        return redirect('/')
    
    return redirect('/home')

@app.route('/home')
def dashboard():

    user = User.get_one({'id':session['userid']})
    bands = Band.get_all()
    return render_template('all_bands.html', bands = bands, user = user)

@app.route('/user/logout') 
def user_logout():
    if 'session_userid' in session: 
        del session['userid']
        del session['user_first_name']
    return redirect('/')

#  ______ 
# < PYTHON ROXX >
#  ------ 
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#              u ||----w |
#                 ||     ||