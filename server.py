from flask import Flask, render_template, redirect, session, request
import random

app = Flask(__name__)
app.secret_key = "helloha"

@app.route("/")
def index():
    if not "num" in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html')

@app.route('/guess', methods =["POST"])
def guess():
    session['guess'] = request.form["guess"]
    guess = int(session['guess'])
    if guess > session['num']:
        session["answer"] = "Too High!"
        session["colour"] = "warning"
        return redirect('/')
    elif guess < session['num']:
        session["answer"] = "Too LOW!"
        session["colour"] = "primary"
        return redirect('/')
    else:
        session["answer"] = "Correct!"
        session["colour"] = "sucess"
        return redirect('/')

@app.route('/reset')
def reset():
    session['num'] = random.randint(1,100)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)