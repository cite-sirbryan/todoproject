from django.db import models

# Create your models here.
# ORM of django
# Object Relational Mapping

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) # we will use the date field
    #created = models.DateTimeField(editable=True)

    def __str__(self):
        return f"{self.id} - {self.title} "
    

class Person(models.Model):
    name = models.TextField(max_length=50000)
    address = models.TextField(max_length=50000)
    birthday = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.address} - {self.birthday} "