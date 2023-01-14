from django.db import models

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
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content