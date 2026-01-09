# Kisoro Vision Website (Django)

This repo contains a basic Django site for Kisoro Vision Secondary School.

## Setup (development)

1. Create a virtualenv and install Django (tested on Django 6.x):

   python -m venv .venv
   .venv\Scripts\activate
   pip install django

2. Make migrations and migrate:

   python manage.py makemigrations
   python manage.py migrate

3. Create a superuser and run the dev server:

   python manage.py createsuperuser
   python manage.py runserver

4. Open http://127.0.0.1:8000/ to see the home page. Use the admin at /admin/ to add Events, News, Testimonials, Achievements and Quick Links.

Notes: The home page will create a default `SiteInfo` object on first view if none exists; use the admin to edit it and add content.
