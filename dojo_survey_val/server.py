from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = "oh_heck_to_the_no"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def showResults():
    if len(request.form['name']) < 1:
        flash("Please fill in your full name :)")
        return redirect('/')
    if len(request.form['comments']) < 1:
        flash("We'd like to hear your opinion! Tell us what you think!")
        return redirect('/')
    if len(request.form['comments']) < 120:
        flash("Your comment cannot be longer than 120 characters")
        return redirect('/')
    else:
        flash("")
    return render_template('results.html',
    name = request.form['name'],
    location = request.form['location'],
    language = request.form['language'],
    comments = request.form['comments'])

@app.route('/set_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/index')
    response = current_app.make_response(redirect_to_index)
    response.set_cookie('cookie_name', value='values')
    return response

app.run(debug=True)
