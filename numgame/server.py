from flask import Flask, render_template, request, session, redirect
import random
app = Flask(__name__)
app.secret_key = 'hello123'

@app.route('/')
def index():
	# import random
	if 'number' not in session:
		session['number'] = random.randint(0,101)
	if 'guess' not in session:
		session['guess'] = ""
	return render_template('index.html')

@app.route('/guess', methods = ['POST'])
def guess():
	# del session['guess']
	if session['number'] == int(request.form['guessnum']):
		session['guess'] = "winner"

	elif session['number'] > int(request.form['guessnum']):
		session['guess'] = "low"

	else:
		session['guess'] = "high"
	return redirect('/')

	return render_template('index.html')

@app.route('/reset')
def reset():
	del session['number']
	del session['guess']

	return redirect('/')


app.run(debug=True)
