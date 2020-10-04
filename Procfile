heroku config: set DISABLE_COLLECTSTATIC=1
release: python manage.py makemigrations
release: python manage.py migrate
web: python manage.py runserver 0.0.0.0:8000