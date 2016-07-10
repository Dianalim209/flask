from flask import Flask, redirect, render_template, session, flash, request, url_for
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
SIMPLE_TXT_REGEX = re.compile(r'^[a-zA-Z]')
PASSWORD_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%])')
DOB_REGEX = re.compile(r'^[0-9]{1,2}$ + \/ +[0-9]{1,2}$ + \/ +[0-9]{1,4}$ ')
app = Flask(__name__)
app.secret_key = "formkeyhere"

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/registered', methods= ['POST'])
def register():
	# error = None
	# if request.method == 'POST'
	#retrieve information from form post
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']


	#setup validation statements
	if len(request.form['email']) < 1:
		flash("email cannot be blank!")
		return redirect('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address")
		return redirect('/')
	if len(request.form['first_name']) < 2:
		flash("first name must be more than two letters")
		return redirect('/')
	elif not SIMPLE_TXT_REGEX.match(request.form['first_name']):
		flash("Please use only letters")
		return redirect('/')
	if len(request.form['last_name']) < 2:
		flash("last name must be more than two letters!")
		return redirect('/')
	elif not SIMPLE_TXT_REGEX.match(request.form['last_name']):
		flash("Please use only letters for your last name")
		return redirect('/')
	# if not DOB_REGEX.match(request.form['birth_date']):
	# 	flash("your birthdate is tooooo long")
	# 	return redirect('/')
	if len(request.form['password']) < 8:
		flash("password must be at least 8 characters long")
		return redirect('/')
	elif not PASSWORD_REGEX.match(request.form['password']):
		flash("must use at least one lowercase, one uppercase, one special character, and one number")
		return redirect('/')
	elif not len(request.form['password']) == len(request.form['confirm_password']):
		flash('your passwords do not match!')
		return redirect('/')


	return render_template('welcome.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
app.run(debug=True)
