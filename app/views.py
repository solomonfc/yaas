from app import app
from flask import request,render_template,flash,redirect

@app.route('/', defaults={'name':"Guest"})
@app.route('/<string:name>' , methods=['GET'])
def say_hello(name):
	return "Hello " + name

# @app.route('/about')
# def about():
# 	return 'The about page'

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
# 	return render_template('hello.html', name=name)

# with app.test_request_context('/hello', method='POST'):
# 	assert request.path == '/hello'
# 	assert request.method == 'POST'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
# 	error = None
# 	if request.method == 'POST':
# 		if valid_login(request.form['username'],
# 					   request.form['password']):
# 			return log_the_user_in(request.form['username'])
# 		else:
# 			error = 'Invalid username/password'
# 	return render_template('login.html', error=error)