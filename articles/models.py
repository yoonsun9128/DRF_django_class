from turtle import title
from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    edite_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)