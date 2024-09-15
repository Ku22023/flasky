# Importing flask module in the project is mandatory
#Render template is used to load in HTML files
from flask import Flask, render_template, request
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

@app.route('/login',methods=('GET','POST'))
def login():
    pin = -1
    username = "placeholder"
    ans = "Hi"
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        print(username)
        username = str.lower(username)
        return render_template('login.html',ans=ans)
    if username == 'kyle':
        pin = request.form['pin']
        if int(pin) == 1234:
            ans = "Welcome, Kyle!"
            return render_template('login.html',ans=ans)
        else:
            ans = "Error: Username or Password is incorrect!"
            return render_template('login.html',ans=ans)
    else:
        ans = "Error: Username or Password is incorrect!"
        return render_template('login.html',ans=ans)



@app.route('/guess',methods=('GET','POST'))
def guess():
    try:
        num = -1
        if request.method == 'POST':
            num = request.form['number']
            print(num)
        if int(num) <= -1:
            return render_template('number.html')
        else:
            print(num)
            if int(num) == 10:
                ans = "You gyatt it!"
                return render_template('number.html',ans=ans)
            else:
                ans = "wrong wrong wrong"
                return render_template('number.html',ans=ans)
    except:
        ans = "use integers only pretty please"
        return render_template('number.html',ans=ans)
    

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
