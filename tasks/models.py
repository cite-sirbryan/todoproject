from django.db import models

# Create your models here.
# ORM of django

class Task(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    #created = models.DateTimeField(editable=True)

    def __str__(self):
        return f"{self.id} - {self.title} "