from logging import debug
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/<string:name>')
def greet(name):
    return f'Hello {name}'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ =='__main__':
    app.run(debug=True)