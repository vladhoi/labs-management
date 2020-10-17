from django.contrib.auth import get_user_model
from django.db import models
from subjects.models import Subject


# Create your models here.


class Lecture(models.Model):
    title = models.CharField(max_length=100, blank=False)
    text = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
