from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=False, null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
