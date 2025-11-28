from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/home.html')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/comps.html')
def comps():
    return render_template('comps.html')

@app.route('/registration.html')
def registration():
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug= True)