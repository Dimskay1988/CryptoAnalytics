
run:
	python manage.py runserver
	python manage.py bot

migrate:
	python manage.py makemigrations
	python manage.py migrate

dependencies:
	pip install -r requirements.txt

celery:
	celery -A CryptoAnalytics worker -l INFO
	celery -A CryptoAnalytics beat -l INFO
