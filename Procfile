release: python manage.py migrate
web: gunicorn config.wsgi:application --preload --workers 1

