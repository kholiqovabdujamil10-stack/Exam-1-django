from django.db import models


class Author(models.Model):
    name_author = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Books(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book_name = models.TextField()
    title = models.TextField()
    caption = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Orders(models.Model):
    name_customer = models.TextField()
    book_name = models.ManyToManyField(Books)
    time_taken = models.DateField()
    time_bring = models.DateField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)