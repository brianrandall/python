from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

#1
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

#2
@app.route('/dojo')
def return_dojo():
    return 'Dojo!'

#3
@app.route('/say/<name>')
def hello(name):
    return "Hi " + str(name) + "!"

#4
@app.route('/repeat/<num>/<word>')
def repeater(num, word):
    if num.isdigit() == False or word.isdigit() == True:
        return "you can't do that, you must enter a number, then a word"
    else:
        wordArr = ''
        for i in range(int(num) + 1):
            wordArr += (word + ' ')    
        return wordArr

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.