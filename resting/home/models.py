from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
