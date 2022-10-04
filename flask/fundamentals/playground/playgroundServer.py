from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def helloWorld():
    return "hello world" 
@app.route('/play/')
def level1():
    return render_template('play.html', phrase="blue", times=3)
@app.route('/play/<num>')
def level2(num):
    if num.isdigit() == True:
        print(f'{num} squares')
        return render_template('play.html', phrase="blue", times=int(num))
    else:
        return "you gotta put in a number, u turd"
@app.route('/play/<num>/<color>')
def level3(num, color):
    if num.isdigit() == True and color.isdigit() == False:
        print(f'{num} {color} squares this time...')
        return render_template('play.html', phrase=str(color), times=int(num))
    else:
        return "you did something wrong, go do it right"

if __name__=="__main__":    
    app.run(debug=True)    
