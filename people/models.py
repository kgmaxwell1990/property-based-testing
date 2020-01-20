from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class Course(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
