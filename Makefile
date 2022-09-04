
run:
	python manage.py runserver
	python manage.py bot

migrate:
	python manage.py makemigrations
	python manage.py migrate

dependencies:
	pip install -r requirements.txt
