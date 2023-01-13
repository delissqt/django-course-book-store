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

---

# blank vs null

| blank = True | null = True |
|--------------|-------------|
| When providing a value for this model field (via a form), this field may be blank (empty) | When a value is received for that field, the special NULL value should be stored in the database |

if null=False is set, you hace to ensuere that mose default value is set in case of blank values

Exception: CharFields (and related types) -> The default value here is an empty string and null=True therefore typically should be avoided 
