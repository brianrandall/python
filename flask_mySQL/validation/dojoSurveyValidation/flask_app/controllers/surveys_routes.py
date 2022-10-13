from flask import render_template,request, redirect
from flask_app import app
from flask_app.models.survey import Survey


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def create_survey():
    if Survey.is_valid(request.form):
        Survey.create(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def results():
    return render_template('result.html', survey = Survey.get_last_survey())