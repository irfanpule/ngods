## Ngods
Ngods is a simple web application for editing ods file that you can use without register or login.


To clone and run this application, you'll need:
 - Git
 - virtualenv or virtualenvwrapper
 - Python 3.6

I assume you already setup the django environment on your machine.

## Setup Project

 - Clone repository
 - Activate virtualenv `source bin/activate`, if use virtualenvwrapper `workon <envname>`
 - Go into repository `cd ngods`
 - Install requirements `pip install -r requirements.txt`
 - Migrate the database `python manage.py migrate`
 - Collect static files `python manage.py collectsatic`
 - Run project `python manage.py runserver`

## TODO
 - Display history of saved files
 - Insert rows above or below
 - Delete the desired rows
 - Save as csv