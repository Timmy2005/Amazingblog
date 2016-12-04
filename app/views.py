from flask import render_template, redirect, url_for, request
from app import app, db, models
from .models import User, Post, Youtube
from datetime import datetime
from flask import make_response
from config import POSTS_PER_PAGE, MAX_SEARCH_RESULTS


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/index/<int:page>', methods=['GET', 'POST'])
def index(page=1):
    if request.method == 'POST':
        query = request.form['search']
        return redirect(url_for('search', query=query))
    if request.cookies.get('user'):
        signed_in = True
        current_user = request.cookies.get('user')
        posts = Post.query.order_by(models.Post.id.desc()).paginate(page, POSTS_PER_PAGE, False)
        users = User.query.all()
        return render_template('index.html',
                               title='Home',
                               post=posts,
                               users=users,
                               signed_in=signed_in,
                               current_user=current_user)
    else:
        signed_in = False
        posts = Post.query.order_by(models.Post.id.desc()).paginate(page, POSTS_PER_PAGE, False)
        users = User.query.all()
        return render_template('index.html',
                               title='Home',
                               post=posts,
                               users=users,
                               signed_in=signed_in)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.cookies.get('user'):
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = models.User.query.all()
        for i in users:
            if username == i.username:
                if password == i.password:
                    response = redirect(url_for("index"))
                    response.set_cookie('user', i.username)
                    return response

        error = 'Invalid login. Please try again.'
    return render_template('login.html',
                           title='Login',
                           error=error)


@app.route('/add', methods=['GET', 'POST'])
def add():
    error = None
    if request.method == 'POST':
        username = request.form['new-username']
        password = request.form['new-password']
        users = models.User.query.all()
        for i in users:
            if i.username == username:
                if i.password == password:
                    error = 'Invalid username or password.'
                    return render_template('new_user.html',
                                           title='Create account - Pokeblog',
                                           error=error)

        u = models.User(username=username, password=password)
        db.session.add(u)
        db.session.commit()
        response = redirect(url_for("index"))
        response.set_cookie('user', username)
        return response

    return render_template('new_user.html',
                           title='Create account - Pokeblog',
                           error=error)


@app.route('/tcg')
@app.route('/tcg/<int:page>')
def tcg(page=1):
    if request.cookies.get('user'):
        signed_in = True
        current_user = request.cookies.get('user')
        posts = Post.query.filter(Post.type.contains('tcg')).order_by(models.Post.id.desc()).paginate(
            page, POSTS_PER_PAGE, False)
        users = User.query.all()
        if request.method == 'POST':
            query = request.form['search']
            return redirect(url_for('search', query=query))
        return render_template('tcg.html',
                               title='TCG',
                               post=posts,
                               users=users,
                               signed_in=signed_in,
                               current_user=current_user)
    else:
        signed_in = False
        posts = Post.query.filter(Post.type.contains('tcg')).order_by(models.Post.id.desc()).paginate(
            page, POSTS_PER_PAGE, False)
        users = User.query.all()
        if request.method == 'POST':
            query = request.form['search']
            return redirect(url_for('search', query=query))
        return render_template('tcg.html',
                               title='TCG',
                               post=posts,
                               users=users,
                               signed_in=signed_in)


@app.route('/pokego')
@app.route('/pokego/<int:page>')
def pokego(page=1):
    if request.cookies.get('user'):
        signed_in = True
        current_user = request.cookies.get('user')
        posts = Post.query.filter(Post.type.contains('pokego')).order_by(models.Post.id.desc()).paginate(
            page, POSTS_PER_PAGE, False)
        users = User.query.all()
        if request.method == 'POST':
            query = request.form['search']
            return redirect(url_for('search', query=query))
        return render_template('pokego.html',
                               title='Pokemon Go',
                               post=posts,
                               users=users,
                               signed_in=signed_in,
                               current_user=current_user)
    else:
        signed_in = False
        posts = Post.query.filter(Post.type.contains('pokego')).order_by(models.Post.id.desc()).paginate(
            page, POSTS_PER_PAGE, False)
        users = User.query.all()
        if request.method == 'POST':
            query = request.form['search']
            return redirect(url_for('search', query=query))
        return render_template('pokego.html',
                               title='Pokemon Go',
                               post=posts,
                               users=users,
                               signed_in=signed_in)


@app.route('/movies')
@app.route('/movies/<int:page>')
def movies(page=1):
    if request.cookies.get('user'):
        signed_in = True
        current_user = request.cookies.get('user')
        posts = Post.query.filter(Post.type.contains('movies')).order_by(models.Post.id.desc()).paginate(
            page, POSTS_PER_PAGE, False)
        users = User.query.all()
        if request.method == 'POST':
            query = request.form['search']
            return redirect(url_for('search', query=query))
        return render_template('movies.html',
                               title='Movies',
                               post=posts,
                               users=users,
                               signed_in=signed_in,
                               current_user=current_user)
    else:
        signed_in = False
        posts = Post.query.filter(Post.type.contains('movies')).order_by(models.Post.id.desc()).paginate(
            page, POSTS_PER_PAGE, False)
        users = User.query.all()
        if request.method == 'POST':
            query = request.form['search']
            return redirect(url_for('search', query=query))
        return render_template('movies.html',
                               title='Movies',
                               post=posts,
                               users=users,
                               signed_in=signed_in)


@app.route('/extra')
def extra():
    if request.cookies.get('user'):
        signed_in = True
        current_user = request.cookies.get('user')
        users = models.User.query.all()
        if request.method == 'POST':
            query = request.form['search']
            return redirect(url_for('search', query=query))
        return render_template('extra.html',
                               title='Extra',
                               users=users,
                               signed_in=signed_in,
                               current_user=current_user)
    else:
        signed_in = False
        users = models.User.query.all()
        if request.method == 'POST':
            query = request.form['search']
            return redirect(url_for('search', query=query))
        return render_template('extra.html',
                               title='Extra',
                               users=users,
                               signed_in=signed_in)


@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.cookies.get('user'):
        signed_in = True
        current_user = request.cookies.get('user')
        users = models.User.query.all()
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            pokeblog_type = request.form['type']
            p = Post(title=title,
                     body=content,
                     timestamp=datetime.now().strftime('%b %-d, %Y at %-I:%M %p'),
                     user=current_user,
                     type=pokeblog_type)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('index'))

        return render_template('post.html',
                               title='New Post',
                               users=users,
                               signed_in=signed_in,
                               current_user=current_user)


@app.route('/logout')
def logout():
    response = make_response(render_template('logout.html'))
    response.set_cookie('user', '', expires=0)
    return response


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    url = request.url
    post_id_split = url.split("=")
    p = models.Post.query.get(int(post_id_split[1]))
    current_type = p.type

    signed_in = True
    current_user = request.cookies.get('user')
    users = models.User.query.all()
    if request.method == 'POST':
        commit_post_id = request.form['id']
        p = models.Post.query.get(commit_post_id)
        db.session.delete(p)
        db.session.commit()
        user_id = request.cookies.get('user')
        title = request.form['title']
        content = request.form['content']
        ptype = request.form['type']
        p = Post(title=title,
                 body=content,
                 timestamp=datetime.now().strftime('%b %-d, %Y at %-I:%M %p'),
                 user=user_id,
                 type=ptype)
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html',
                           title='Edit',
                           p=p,
                           users=users,
                           signed_in=signed_in,
                           current_user=current_user,
                           type=current_type)


@app.route('/delete')
def delete():
    url = request.url
    post_id_split = url.split("=")
    p = models.Post.query.get(int(post_id_split[1]))
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/search/<query>', methods=['GET', 'POST'])
def search(query):
    if request.cookies.get('user'):
        current_user = request.cookies.get('user')
        posts = Post.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
        users = models.User.query.all()
        return render_template('search_results.html',
                               title='Search Results',
                               post=posts,
                               users=users,
                               signed_in=True,
                               current_user=current_user)

    else:
        posts = Post.query.whoosh_search(query, MAX_SEARCH_RESULTS).all()
        posts.order_by(models.Post.id.desc()).all()
        users = models.User.query.all()
        return render_template('search_results.html',
                               title='Search Results',
                               post=posts,
                               users=users,
                               signed_in=False)


@app.route('/user', methods=['GET'])
def user():
    if request.cookies.get('user'):
        current_user = request.cookies.get('user')
        users = models.User.query.all()
        return render_template('user.html',
                               title='Search Results',
                               users=users,
                               signed_in=True,
                               current_user=current_user)

    else:
        posts = Post.query.filter(Post.type.contains('actfigs'))
        posts.order_by(models.Post.id.desc()).all()
        users = models.User.query.all()
        error = 'You are not signed in. Login or sign up'
        return render_template('user.html',
                               title='Error',
                               post=posts,
                               users=users,
                               signed_in=False,
                               error=error)
