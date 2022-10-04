from curses.ascii import isdigit
import random
import re
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "##SECRETKEYHERE##"



@app.route('/')
def helloWorld():
    
    session['boxxxyActivate'] = ''
    session['boxxxyText'] = ''
    session['boxxxyColor'] = ''
    session['inputType'] = 'hidden'
    if 'random' in session:
        print ("random number is", session['random'])
    else:
        guess = random.randint(1, 100)
        session['random'] = guess
        type(int(session['random']))

    if 'user_input' in session:
        print("user input", session['user_input'])
    else:
        session['user_input'] = 0

    if session['user_input'] == 0:
        print('nothing')
    elif int(session['user_input']) < session['random']:
        session['boxxxyActivate'] = '#'
        session['boxxxyText'] = 'Too low, try again!'
        session['boxxxyColor'] = 'red'
    elif int(session['user_input']) > session['random']:
        session['boxxxyActivate'] = '#'
        session['boxxxyText'] = 'Too high, try again!'
        session['boxxxyColor'] = 'red'
    else:
        session['boxxxyActivate'] = '#'
        session['boxxxyText'] = 'nice work. play again?'
        session['boxxxyColor'] = 'green'
        session['inputType'] = 'submit'
        print('damn u guessed it')
        

    return render_template('index.html')


@app.route('/input', methods=['POST'])
def input():
    
    if request.form['user_input'].isdigit() == True:
        session['user_input'] = request.form['user_input']
    else:
        redirect('/')
    return redirect('/')

@app.route('/destroy_session')
def destroyer():
    session.clear()
    return redirect('/')

if __name__=="__main__":    
    app.run(debug=True)    
