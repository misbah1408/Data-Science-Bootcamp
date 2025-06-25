from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcom():
    return '<h1>Hello, Misbah this side, How are you?</h1>'

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f'<span>Name:{name} & email:{email}</span>'
    else:
        return render_template('form.html') 
    
@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f'<span>Name:{name} & email:{email}</span>'
    else:
        return render_template('form.html') 

if __name__ == '__main__':
    app.run(debug=True)