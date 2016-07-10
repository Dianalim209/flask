from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = "hello!"

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')
@app.route('/ninjas')
def plustwo():
    session['counter'] += 2
    return render_template('index.html')
@app.route('/reset')
def reset():
    session.clear()
    return redirect ('/')
app.run(debug = True)
