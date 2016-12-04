from app import db, models
from datetime import datetime
import app

app.db.drop_all()
db.configure_mappers()
app.db.create_all()
u = models.User(username='timothy',
                password='cleveland')
db.session.add(u)
db.session.commit()

u = models.User(username='timmy',
                password='cleveland')
db.session.add(u)
db.session.commit()

now = datetime.now()
posts = models.Post(title='A new app called Pokeblog!',
                    body='This new app allows you to post new stuff about Pokemon!',
                    timestamp=now.strftime('%b %-d, %Y at %I:%m %p'),
                    user='timothy',
                    type='')

db.session.add(posts)
db.session.commit()

posts = models.Post(title='new user',
                    body="I'm a new user! What can I do?",
                    timestamp=now.strftime('%b %-d, %Y at %-I:%-M %p'),
                    user='timmy',
                    type='')
db.session.add(posts)
db.session.commit()
