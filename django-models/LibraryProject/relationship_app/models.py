from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField('Book')  # Many-to-Many relationship with Book

    def __str__(self):
        return self.name

# Create your models here.
