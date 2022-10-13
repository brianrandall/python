# controllers.py
import re
from flask_app import app
from flask import render_template,redirect,request,session
from flask_app.models.email import Email


@app.route("/")
def index():
    return render_template("index.html")
            

@app.route('/process', methods=["POST"])
def check_email():
    
    if not Email.valid_email(request.form):
        return redirect('/')

    Email.save(request.form)

    return redirect('/emails')

@app.route('/emails')
def show_emails():
    
    emails = Email.get_all()

    return render_template('emails.html', emails = emails)

