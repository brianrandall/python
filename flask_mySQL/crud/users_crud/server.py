from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route("/")
def index():
    # call the get all classmethod to get all friends
    return render_template("index.html")
            

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users/all')

@app.route('/users/all')
def display_users():
    
    return render_template('/show_all.html', user=User.get_all())

@app.route('/users/edit/<int:id>')
def edit (id):
    data = {
    "id": id
    }
    return render_template("edit_one.html", user=User.get_one(data))

@app.route('/users/show/<int:id>')
def show (id):
    data = {
    "id": id
    }
    return render_template("show_one.html", user=User.get_one(data))

@app.route('/users/update', methods=['post'])
def update():
    User.update(request.form)
    return redirect ('/users/all')

@app.route('/users/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/users/all')


if __name__ == "__main__":
    app.run(debug=True)