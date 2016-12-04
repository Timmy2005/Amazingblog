import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir
from flask.ext.heroku import Heroku
from flask_migrate import Migrate
from flask_script import Manager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
heroku = Heroku(app)
migrate = Migrate(app, db)
manager = Manager(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

from app import views, models
