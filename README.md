# howto

**Getting Started**

A quora experiment. Quora clone written in Django.
	

start the env

	source bitoraenv/bin/activate
	

install the requirements
	
	
	pip install -r requirements.txt
	

Now run the database migrations

	
	python manage.py migrate
	

Now run the server

	
	python manage.py runserver
	

Head to `http://127.0.0.1:8000/`


**Admin Site**

Create superuser for admin site

	
	python manage.py createsuperuser
	
	
Head to `http://127.0.0.1:8000/admin`
