from django.db import models

class Book(models.model):
    STATUS = [(1, 'Read'), (2, 'Not Read')]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    year = models.IntegerField()
    description = models.TextField(blank = True)
    status = models.CharField(choices = STATUS, max_length = 1)
    reviews = models.OneToManyField('BookReview', blank=True)

class BookReview(models.model):
    REVIEW_TYPE = [(1, 'Member'), (2, 'Online')]
    source = models.CharField(max_length=100)
    rating = models.IntegerField()
    comments = models.TextField(blank = True)
    review_type = models.CharField(choices = REVIEW_TYPE, max_length = 1)
