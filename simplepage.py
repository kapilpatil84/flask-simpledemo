from flask import Flask
from flask import request

app = Flask(__name__)

from flask import render_template


@app.get("/")
def index():
    return render_template('index.html')


@app.route("/login", methods=['POST'])
def login():
    app.logger.error("Inside login...")
    username = request.form['username']
    return render_template('index.html', username=username)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

# @app.get("/")
# def index():
#     return render_template('upload_file.html')

@app.route("/upload", methods=['POST'])
def upload_files():
    if request.method == 'POST':
        file = request.files['the_file']
        file.save("uploaded_file.txt")
    return "OK"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404