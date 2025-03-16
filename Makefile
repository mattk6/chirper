install:
	uv run poetry install

run:
	clear
	uv run poetry run python manage.py runserver

migrate:
	uv run python3 manage.py makemigrations chirper
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