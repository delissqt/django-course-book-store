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


---
Query performance

store query in variable
returns a query set which itself is an object on which we can again call filter to narrow it down even more 
and you can do it at how often you want.

`bestsellers = Book.objects.filter(is_bestselling=True)`  

`amazing_bestsellers = bestsellers.filter(rating__gt=4)`

but nonetheless, the database wasn't touched yet which is good for perormance of course.
Django will only reach out the database and do something with it once you do something with your query sets

`print(bestsellers)` // Django run the query

`print(amazing_bestsellers)` // Django is even able to do this 

---

Bulk Operations

Besides operations on individual model instances (i.e. deleting one model instance, updating one model instance etc), you can also perform bulk operations:

    You can delete multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.1/topics/db/queries/#deleting-objects

    You can update multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update

    You can create multiple model instances (i.e. database records) at once: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create



---

Get title in order to generate slug

from book_outlet.models import Book

```
Book.objects.all()

Book.objects.get(title="Harry Potter").save()
Book.objects.get(title="Harry Potter").slug
$ 'harry-potter'
```

---
Delete all data in the storage in Data Base

`Book.objects.all().delete()`

---

---

Examples with order_by()

* display the data in alphabetic order
  
`Book.objects.all().order_by("title")`

* display tha data in inverse order adding minus "-" character

`Book.objects.all().order_by("-title")` 


This also works with numbers data

`Book.objects.all().order_by("rating")`

`Book.objects.all().order_by("-rating")`

---

python manage.py createsuperuser

insert username, email address, password, password (again):

---

Different Kinds of Relationships

| One-to-Many | One-to-One | Many-tom-Many |
|-------------|------------|---------------|
| One bokk as one author, one author wrote multiple books | One author has one address, one address belongs to one author | A book can be published in many countries, a country can publish many books |


# Adding a one-to-many Relation & Migration

Example

```
class Author(models.model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False) 
    author = models.ForeignKey(Author)
    # For a author we store a pointer to an author entry in the Author table.
    # Here we wanna connect our book to an author (Author model name)

```


# Filtering data

`
books_by_rowling = Book.objects.filter(author__last_name="Rowling")
books_by_rowling
$ <QuerySet [<Book: Harry Potter 1 (5)>]>
`

`
books_by_rowling = Book.objects.filter(author__last_name__contains="wling")
books_by_rowling
$ <QuerySet [<Book: Harry Potter 1 (5)>]>
`


`
jkr = Author.objects.get(first_name="J.K.")
jkr
$<Author: Author object (1)>

jkr.book_set
$<django.db.models.fileds.related_descriptors.create_reverse_many_to_one_manager.<locals>.RelatedManager object at 0x000001E05DC62E80>


# Book set is like objects, just for relations...
jkr.book_set.all()

$<QuerySet [<Book: Harry Potter 1 (5)>]>
`


Book set is like objects, just for relations 
Django automatically creates this property (book_set) on the author object
It takes the class name of the related model book, turns it into all lower case, 
is possible to use a different name. You Just have to go to the field where you set up the relation

`jkr.book_set.all()`


```
class Book(models.Model):
    title = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")

    # related_name 

```