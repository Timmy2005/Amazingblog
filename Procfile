web: gunicorn app:app
init: python db_start.py
upgrade: python db_create.py
migrate: gunicorn db:migrate