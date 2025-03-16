install:
	pip install -r requirements.txt

run:
	clear
	uv run python3 manage.py runserver

update:
	uv run python3 manage.py makemigrations chirper

migrate:
	uv run python3 manage.py migrate

shell:
	uv run python3 manage.py shell

sql:
	sqlite3 db.sqlite3

debug:
	uv run python3 manage.py shell

redis:
	redis-server

freeze:
	pip freeze > requirements.txt

superuser:
	uv run python3 manage.py createsuperuser