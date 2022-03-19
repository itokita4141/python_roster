FROM python:3.9
ADD . /var/www/html
WORKDIR /var/www/html
RUN pip install -r ./requirements.txt
CMD gunicorn app_roster.wsgi --log-file -