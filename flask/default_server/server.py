from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "##SECRETKEYHERE##"


@app.route('/')
def helloWorld():
    return "hello world" 
@app.route('/play/')
def level1():
    return render_template('index.html', phrase="blue", times=3)

if __name__=="__main__":    
    app.run(debug=True)    

#always run 'pipenv install flask' to install flask in root directory
#then 'pipenv shell', 'python (filename).py to run