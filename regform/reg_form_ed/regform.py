from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "SHHHHHH"

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process_data' , methods=['POST'])
def form():
	error_count = 0
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Email is invalid")
		error_count += 1
	if not request.form['first_name'].isalpha():
		flash("First name must be in alphabetical letters!")
		error_count += 1
	if not request.form['last_name'].isalpha:
		flash("Last name must be in alphabetical letters!")
		error_count += 1
	if len(request.form['password']) < 8:
		flash("Password must be at least 8 characters")
		error_count += 1


	if error_count > 0:
		return redirect('/')
	else:
		flash("Confirm password must match password!")
		return redirect('/')


app.run(debug=True)
