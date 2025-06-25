from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcom():
    return 'Hello, Misbah this side, How are you?'

@app.route('/index')
def index():
    return 'Welcome to index page'

if __name__ == '__main__':
    app.run(debug=True)