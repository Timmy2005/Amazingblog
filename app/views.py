from flask import render_template, flash, redirect, session, url_for, request
from app import app, db, lm, models
from .models import User
from app import logged_in_true


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html',
                           title='Login')


# form = cgi.FieldStorage()
# if form.getvalue('username'):
#    username = form.getvalue('username')
# if form.getvalue('password'):
#    password = form.getvalue('password')
# u = models.User(username=username, password=password)
# db.session.add(u)
# db.session.commit()
# username = request.form['new-username']
# password = request.form['new-password']

@app.route('/after-login', methods=['GET', 'POST'])
def after_login():
    username = request.form['username']
    password = request.form['password']
    users = models.User.query.all()
    for i in users:
        if username == i.username:
            if password == i.password:
                response = redirect(url_for("index"))
                response.set_cookie('session-id', str(i.id))
                return response
    flash('Invalid login. Please try again.')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    return redirect(url_for('index'))
