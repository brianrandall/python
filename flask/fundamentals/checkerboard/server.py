from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html" , row=8, col=8, color1="red", color2='black')

@app.route('/<num>')
def row(num):
    return render_template("index.html" , row=int(num), col=8, color1="red", color2='black')

@app.route('/<num>/<num2>')
def row_col(num, num2):
    return render_template("index.html" , row=int(num), col=int(num2), color1="red", color2='black')

@app.route('/<num>/<num2>/<firstColor>')
def row_col_one_color(num, num2, firstColor):
    return render_template("index.html" , row=int(num), col=int(num2), color1=str(firstColor), color2='black')

@app.route('/<num>/<num2>/<firstColor>/<secondColor>')
def row_col_two_colors(num, num2, firstColor, secondColor):
    return render_template("index.html" , row=int(num), col=int(num2), color1=str(firstColor), color2=str(secondColor))



if __name__=="__main__":    
    app.run(debug=True)    
