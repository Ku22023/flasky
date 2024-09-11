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

@app.route('/login')
def login():
    attempts = 3
    name = str(input("What's your name? "))
    while attempts >= 1:
        pin = int(input("Enter your PIN: "))
        lenpin = str(pin)
        if len(lenpin) == 4:
            if pin == 1234:
                return render_template('correct.html',name=name)
            else:
                attempts -= 1
                print(attempts)
                print("Wrong")
        else:
            print("Pin must be 4 digits long!")
    else:       
        return render_template('wrong.html',name=name)

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
