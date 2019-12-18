from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=256)
    img_url = models.CharField(max_length=512)
    auth = models.CharField(max_length=128)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class Article(models.Model):
    title = models.CharField(max_length=512)
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    book_title = models.CharField(max_length=128)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
