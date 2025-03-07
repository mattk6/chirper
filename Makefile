install:
	pip install -r requirements.txt

run:
	uv run daphne conf.asgi:application

update:
	uv run python3 manage.py makemigrations chirper

migrate:
	uv run python3 manage.py migrate

sql:
	sqlite3 db.sqlite3

debug:
	uv run python3 manage.py shell

redis:
	redis-server

freeze:
	pip freeze > requirements.txt