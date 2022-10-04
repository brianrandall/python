from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def helloWorld():
    return "hello world" 

@app.route('/table')
def list():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template('index.html', list_of_students=users)



if __name__=="__main__":    
    app.run(debug=True)    

#always run 'pipenv install flask' to install flask in root directory
#then 'pipenv shell', 'python (filename).py to run