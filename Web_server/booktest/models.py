from django.db import models
from unittest.util import _MAX_LENGTH
# Create your models here.
class BookInfo(models.Model):
    title=models.CharField(max_length=20)
    pub_date=models.DateField()
    def __str__(self):
        return '%d'%self.pk
class DetailInfo(models.Model):
    name=models.CharField(_MAX_LENGTH=20)
    content=models.CharField(max_length=100)
    people=models.CharField(max_length=20)
    gender=models.BooleanField(default=True)
    foreign=models.ForeignKey(BookInfo)
    def __str__(self):
        return '%d'%self.pk
