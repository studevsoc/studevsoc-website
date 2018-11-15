from django.db import models

# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=140)
    body = model.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
