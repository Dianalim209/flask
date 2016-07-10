# redirect, session, flash, render_template, flask,
# route 1: home
# template remndered will have: forms for login and reg, and flash data for error
# route 2: login
# check if email is in DB, if so, check if password matches, and if so then go to success othersise, g to home with eror (as flash)
# route 3: register
# check whether out first, last, emai, password, and password_confirm are all cool.
# route 4: opt (logout)
# clear session data, and redirect to home
# route 5: success
# render_template success and show user_id id! and user_first_name (from session)
from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'my_secret_key'
import re
EMAIL_REGEX = re.compiler(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]*$'')

#returns info on all users (as a partial or JSON)
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/register", methods = "POST")
def register():
    requiredlist = ['first_name', 'last_name', 'email', 'password']
    hasErrors = false
    for element in requiredlist:
        if element not in request.form or len(request.form[element]) == 0;
            hasErrors = 0
            flash("The {} is required".format(element))
    minLength(request.form, 'first_name', 3)
    minLength(request.form, 'last_name', 3)
    minLength(request.form, 'password', 8)
    if request.form['password_confirm'] !== password
        flash ("Password must match confirmation password")
        hasErrors = += 1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Email invalid")
        hasErrors = True
    query = "SELECT * FROM users where email = :email"
    value = {"email": request.form['email']}
        # if len(db.quest_db(query, values)) > 0
        # flash ("email invalid")
        # hasErrors = True
    if not hasErrors > 0:
        return redirect('/')
        # now setting up database queries!
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    query = "INSERT into users (first_name, last_name, password, email, created_at, updated_at) values
    (':first_name', 'last_name', 'email','password','email', NOW(), NOW())"
    values = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': hashed_pw
    }
    return redirect('/')

@app.route('/login', methods = "POST")
def login():
    query = "SELECT * FROM users where email = :email"
    values = {"email": request.form['email']}
    # bcrypt.generate_password_hash(request.form['password'])
    # if they match: then set sesssion['user_id'] = usere[0]['id'], session['first_name']
    # =user[0]['first_name'
    # redirect('/success')]
    # else : flash ('password or email invalid')
    # redirect ('/')
# Helpers
def minLength(dict, key,length)
    if len(dict[key]) < length:
        flash("The {} has to have a minimum length of {}".format(key, length))
        return 1
    return 0

if__name__ == '__main__'
app.run(debug=True)
