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


---
Adding Data in Data Base from python Terminal

## open python shell
python manage.py shell

## add data in table Book

from book_outlet.models import Book

harry_potter = Book(title="Harry Potter" , rating = 5)


## display data
Book.objects.all()
Book.objects.all()[0]

### this data is saved in memory

## save data in the database

harry_potter.save()

## update data

harry_potter.title = "Harry Potter and Philosopher's Stone"


## delete data
harry_potter.delete()

---
 Other way Create element

 Book.objects.create(title="Harry Potter", rating=5, author="J.K. Rowling", is_bestselling=False)


 # filtering data
 Example:
 
 ` 
 Book.objects.filter(rating__lt=3, title__contains="story")

 Book.objects.filter(rating__lt=3, title__icontains="story")`
 `


 ## or conditions

 import "Q" class. 
 This allows us to write queries, that also contains an "or", and not just "and" combinations.

 `from django.db.models import Q`

After import we can make OR conditions filtering

`Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=True))`


also is posiible make queris with both OR and AND conditions

`Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=False), Q(author="J.K. Rowling"))`

Is possible remove "Q" call in the last contiditions this still works, This only orks if the AND conditions is in the end

`Book.objects.filter(Q(rating__lt=3) | Q(is_bestselling=False), author="J.K. Rowling")`

but we can also add the AND conditions using "Q" class

`Book.objects.filter(Q(author="J.K. rowling"), Q(rating__lt=3) | Q(is_bestselling=False))`