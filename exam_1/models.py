from django.db import models
from datetime import datetime

# Create your models here.

class Author(models.Model):
    name_author = models.TextField()
    book_name = models.ManyToOneRel()
    is_active = models.BooleanField()
    created_at = models.DateField(default=datetime.now())


class Books(models.Model):
    book_name = models.TextField()
    title = models.TextField()
    caption = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.now())


class Orders(models.Model):
    name_author = models.ManyToManyField
    name_customer = models.TextField()
    book_name = models.ManyToManyField()
    time_taken = models.DateField()
    time_bring = models.DateField()
    status = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.now())