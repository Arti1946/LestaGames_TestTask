from django.db import models


class Word(models.Model):
    file = models.FileField(upload_to="media/files/", unique=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    word = models.CharField(max_length=100)
    tf = models.FloatField()
    idf = models.FloatField()
