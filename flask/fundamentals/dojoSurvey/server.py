from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "##SECRETKEYHERE##"


@app.route('/')
def helloWorld():
    return render_template('/index.html') 


@app.route('/process', methods=['POST'])
def proccess():

    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    return redirect('/result')

@app.route('/result')
def result():

    return render_template('/result.html')

@app.route('/reset')
def destroyer():
    session.clear()
    return redirect('/')



if __name__=="__main__":    
    app.run(debug=True)    

#always run 'pipenv install flask' to install flask in root directory
#then 'pipenv shell', 'python (filename).py to run