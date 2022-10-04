from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "session keyyyy"

@app.route('/')
def counter():
    
    if 'count' in session:
        print (f"counter is {session['count']}")
    else:
        session['count'] = -1

    session['count'] += 1
    print()
    return render_template('index.html') 

@app.route('/count', methods=['POST'])
def whatever(): 
    return redirect('/')

@app.route('/add2', methods=['POST'])
def whatever2(): 
    session['count'] += 2
    return redirect('/')

@app.route('/addNum', methods=['POST'])
def addNum():
    
    if request.form['user_input'].isdigit() == True:
    
        session['count'] += int(request.form['user_input']) - 1
        print(request.form['user_input'])
        return redirect('/')
    else:
        return redirect('/youaredumb')

@app.route('/youaredumb')
def nothing():
    session['count'] -= 1
    return redirect('/')

@app.route('/destroy_session')
def destroyer():
    session.clear()
    return redirect('/')


if __name__=="__main__":    
    app.run(debug=True)    

#always run 'pipenv install flask' to install flask in root directory
#then 'pipenv shell', 'python (filename).py to run