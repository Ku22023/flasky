# Importing flask module in the project is mandatory
#Render template is used to load in HTML files
from flask import Flask, render_template, request, redirect, flash, url_for
import random
import sqlite3

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
    
def get_db_connection():
    conn = sqlite3.connect('login.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    with app.open_resource('schema.sql') as f:
        conn.executescript(f.read().decode('utf8'))
    conn.close()

@app.route('/login',methods=('POST','GET'))
def login():
    if request.method == 'POST':
        user_name = request.form['userName']
        password = request.form['password']

        if not user_name or not password:
            flash('All fields required')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO user (username,password) VALUES (?,?)',(user_name,password))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template("login.html")

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
