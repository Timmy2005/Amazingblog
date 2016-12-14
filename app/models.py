from app import db


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(64), index=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % self.username


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String())
    timestamp = db.Column(db.String())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.String())
    user = db.Column(db.String(64))
    type = db.Column(db.String())

    def __repr__(self):
        return '<Post %r>' % self.title


class Youtube(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    link = db.Column(db.String())
    body = db.Column(db.String())
    timestamp = db.Column(db.String())

    def __repr__(self):
        return '<Link %r>' % self.link
