__author__ = 'surge'
from flask import Flask, render_template, redirect, abort, make_response
#from flask_script import Manager
from flask_bootstrap import Bootstrap

app = Flask(__name__)
#manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu/')
def menu():
    return render_template('menu.html')

@app.route('/reservations/')
def reservations():
    return render_template('reservations.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/admin/')
def bad_request():
    return '<h1>Bad request!</h1>', 400

@app.route('/makeresponse')
def makeresponse():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def redir():
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    #manager.run()
    app.run(debug=True)