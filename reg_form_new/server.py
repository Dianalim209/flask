from flask import Flask, flash, redirect, render_template,request, url_for
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods=['GET', 'POST'])

    error = None
    if request.method == 'POST'
            request.form['password'] != 'secret':
        error = 'Invalid credentials'
    else:
        flash('You were successfully logged in')
        return redirect(url_for('index'))
    return render_template('login.html', error=error)
if __name__ == "__main__":
    app.run(debug=True)
