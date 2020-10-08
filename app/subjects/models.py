from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Subject(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
