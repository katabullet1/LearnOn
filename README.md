# LearnOn

# Create and Apply migrations
$ python3 manage.py makemigrations

$ python3 manage.py migrate

# Create superuser to help managing for the first time
$ python3 manage.py createsuperuser

# To start the Django server
$ python3 manage.py runserver

$ python3 manage.py runserver 0.0.0.0:8000


#do not run

nohup python3 manage.py runserver 0.0.0.0:8000 &

screen -d -m python3 manage.py runserver 0.0.0.0:8000

ps auxw | grep runserver
