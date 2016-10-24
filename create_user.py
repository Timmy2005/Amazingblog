from app import db, models

import cgi

form = cgi.FieldStorage()


def new_user():
    if form.getvalue('username'):
        username = form.getvalue('username')

    if form.getvalue('password'):
        password = form.getvalue('password')

    u = models.User(username=username, password=password)
    db.session.add(u)
    db.session.commit()


new_user()
