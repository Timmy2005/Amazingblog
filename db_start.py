from config import SQLALCHEMY_MIGRATE_REPO
from app import db
db.create_all()
db.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
