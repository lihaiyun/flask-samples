from flask import Flask, flash, redirect, url_for, render_template, request, session
import os

from user import User
from event import Event

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.authenticate(username, password):
            session['username'] = username
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('login'))


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['username'] = None
    return redirect(url_for('home'))


@app.route('/profile')
def profile():
    if session['logged_in']:
        username = session['username']
        user = User.get_user(username)
        return render_template('profile.html', user=user)
    else:
        return redirect(url_for('login'))


@app.route('/events')
def events():
    event_dict = Event.get_dict()
    return render_template('events.html', events=event_dict.values())


@app.route('/map')
def map():
    return render_template('map.html')


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
