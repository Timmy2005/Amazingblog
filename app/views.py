from flask import render_template, flash, redirect, session, url_for, request, g
from app import app, db, lm, models
from .models import User, Post
from datetime import datetime


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@app.route('/index')
def index():
    user_id = request.cookies.get('session_id')
    posts = models.Post.query.all()
    return render_template('index.html',
                           title='Home',
                           post=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html',
                           title='Login')


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
                response.set_cookie('user', i.username)
                return response
    flash('Invalid login. Please try again.')
    return redirect(url_for('login'))


@app.route('/new-user', methods=['GET', 'POST'])
def new_user():
    username = request.form['new-username']
    password = request.form['new-password']
    users = models.User.query.all()
    for i in users:
        if i.username == username:
            flash('This username is already taken.')
            return redirect(url_for('login'))
        if i.password == password:
            flash('This password is already taken.')
            return redirect(url_for('login'))
    if request.form['email']:
        email = request.form['email']
        u = models.User(username=username, password=password, email=email)
    else:
        u = models.User(username=username, password=password)
    db.session.add(u)
    db.session.commit()
    response = redirect(url_for("index"))
    response.set_cookie('session-id', str(u.id))
    response.set_cookie('user', u.username)
    return response


@app.route('/logout')
def logout():
    return redirect(url_for('index'))


@app.route('/tcg')
def tcg():
    posts = "i"
    return render_template('tcg.html',
                           title='TCG',
                           post=posts)


@app.route('/post', methods=['GET', 'POST'])
def post():
    return render_template('post.html',
                           title='New Post')


@app.route('/posting', methods=['GET', 'POST'])
def posting():
    user_id = request.cookies.get('session_id')
    title = request.form['title']
    content = request.form['content']
    p = Post(title=title, body=content, timestamp=datetime.utcnow(), author=user_id)
    db.session.add(p)
    db.session.commit()
    return redirect(url_for('index'))
