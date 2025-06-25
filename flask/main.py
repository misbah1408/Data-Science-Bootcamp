from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcom():
    return '<h1>Hello, Misbah this side, How are you?</h1>'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)