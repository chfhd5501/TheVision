from django.db import models
from django.contrib.auth.models import User
class Support(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    undergrad = models.IntegerField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    application_field = models.TextField()

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    undergrad = models.IntegerField()
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    application_field = models.TextField()

    def __str__(self):
         return self.name


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content