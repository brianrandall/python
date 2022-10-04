## pre-requisits
- install pipenv 'globally'
```
pip3 install pipenv
```
- this only needs to be ran once, per machine

# flask checklist
- setup file structure.... 
- create project directory
```
    >main project directory
        -pipfile
        -pipfile.lock
        -server.py
        > static
            > img
                -picture(s).png
            > js
                -script.js
            > styles
                -styles.css
        > templates
            -index.html
            -otherPage.html
```
- CD into folder
- install flask
```
pipenv install flask
```
- then run
```
pipenv shell
```
- then
```
python3 server.py
```

## server.py
```py
from flask import Flask, render_template
app = Flask(__name__)

# THIS IS GONIG TO MOVE TO /controllers

@app.route('/')
def helloWorld():
    return "hello world" 

# JUST THAT STUFF ^^

# THIS NEEDS TO STAY AT THE BOTTOM OF ALL SERVER.PY FILES
if __name__=="__main__":    
    app.run(debug=True)  
```