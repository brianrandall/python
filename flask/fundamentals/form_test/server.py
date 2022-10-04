from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "secretKey is a Secret"
# our index route will handle rendering our form

@app.route('/')
def default():
    return render_template('index.html')


@app.route('/users', methods=['POST'])
def index():
    print("got post info")
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    print(session)
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('show.html')


if __name__ == "__main__":
    app.run(debug=True)
