from django.db import models

# Create your models here.
class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)

    def __str__(self):
        return 'isbn_13: {}, isbn_10: {}'.format(self.isbn_13, self.isbn_10)

class Book(models.Model):
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=16, default=0, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    isPublished = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)
    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='character')

class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='author')



