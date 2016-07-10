from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', phrase = "hello",times="5")

@app.route('/ninjas', methods = ['GET'])
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)
