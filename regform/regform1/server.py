from flask import Flask, redirect, request, render_template, flash, session
import re
from connect import MySQLConnector
from flask.ext.bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+-_]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')

app = Flask(__name__)
app.secret_key = 'RObBoss'
banana = MySQLConnector(app, 'mybd')
bcrypt = Bcrypt(app)
print (banana.query_db("select * from users"))

@app.route('/')
def index():
	return render_template('index.html')
@app.route('/register', methods=['POST'])
def register():
	# for readability
	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['password'] = request.form['password']
	session['password_confirmation'] = request.form['password_confirmation']

	# validating
	# its there
	if len(session['email'])< 0 or len(session['first_name']) < 0 or len(session['last_name']) <0 or len(session['password']) <0:
		flash('gotta have the things yo!')
	# password checks
	if len(session['password']) < 8:
		flash('password has to be over 8 bruh')
	if session['password'] != session['password_confirmation']:
		flash('passwords gotta password! and MATCH foo\'!')
	# regex time :/
	if not EMAIL_REGEX.match(session['email']):
		flash('email better peep!')
	if not NAME_REGEX.match(session['first_name']):
		flash('that isnt a first name i seen before')
	if not NAME_REGEX.match(session['last_name']):
		flash('last name be off the chain! try a version that has like, only letters, yeah?')
	else:
		flash('niiiiiiiiiice')
		query = "INSERT into users (first_name, last_name, email, password, created_at, updated_at) values (:first_name, :last_name, :email, :password, NOW(), NOW())"
		#use the dictionary that we are going to describe below to populate the: fields.
		password = bcrypt.generate_password_hash(request.form['password'])
		#encrypts your password
		values = {
			"first_name":	request.form['first_name'],
			"last_name":	request.form['last_name'],
			"email":		request.form['email'],
			"password": 	password
		}
		banana.query_db(query,values)
	return redirect('/')

@app.route('/login', methods  = ['POST'])
def login():
	#from reqeust.form we want to get user by email
	# after we get the user, compare passwords (using bcrypt hashy thing)
	#if hashy thing true, save user first_name and if in session
	#else redirect('/')
	query = "SELECT * from usrs where email = :email"
	alues = {
		"email": request['email']
	}
	users = banana.query_db(query,values)
	#user = array with a dictionary inside!
	if bcrypt.check_password_hash(user[0]['password'], request.form['password']):
		session['user_id'] = user[0]['id']
		session['first_name'] = user[0]['first_name']
		return render_template('success.html')
	return redirect('/')
app.run(debug=True)
