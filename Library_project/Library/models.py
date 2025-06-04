from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.CASCADE,
        related_name='published_books'
    )

    def __str__(self):
        return f"{self.title} (ISBN: {self.isbn})"