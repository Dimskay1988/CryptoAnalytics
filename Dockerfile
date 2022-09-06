FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1


WORKDIR /var/www
COPY requirements.txt /code/var/www/requirements.txt
RUN mkdir /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /var/www/
EXPOSE 8000
CMD python manage.py collectstatic --noinput
CMD python manage.py runserver 0.0.0.0:8000
