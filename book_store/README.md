# Create project

django-admin startproject mysite


# create app in project

python manage.py startapp book_outlet


---

# make migrations

python manage.py makemigrations


# apply migrations

python manage.py migrate

## NOTE: Is important add the aplicacion (app contains models) in INSTALLED_APPS this can be found in seetings.py project file