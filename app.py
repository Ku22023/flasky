# Importing flask module in the project is mandatory
#Render template is used to load in HTML files
from flask import Flask, render_template
import random

# We use this to set up our flask sever
app = Flask(__name__)

# The route( tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with index() function.
def index():
    return render_template("index.html")

@app.route('/count')
def count():
    numbers = list(range(1, 11))  # List of numbers from 1 to 10
    return render_template('count.html', numbers=numbers)

@app.route('/names')
def names():
    names = ["Liam", "Hanah", "Lauren", "Owen", "Harrison", "David"]
    return render_template('names.html',names=names)

@app.route('/random')
def random_num():
    num = random.randint(1,100)
    return render_template('random.html',num=num)

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
