from flask import Flask, render_template, redirect, url_for, request
import  requests


app = Flask(__name__)

url = 'https://icanhazdadjoke.com/'
headers = {'Accept': 'application/json'}

@app.route('/joke',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            r = requests.get(url=url, headers=headers).json()
            dad_joke = r['joke']
        except: 
            r = "Error: unable to send data" 
    return redirect(url_for('success',joke = dad_joke))

@app.route('/joke/<joke>')
def success(joke): 
    return render_template('index.html',joke=joke)


@app.route("/")
def index():
	return render_template('index.html',joke="Ready for joke?")





if __name__ == "__main__": 
    app.run(debug=True)
