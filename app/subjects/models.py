from django.db import models
from django.conf import settings
from utils.models import AbstractTableMeta


class Subject(AbstractTableMeta, models.Model):
    class Meta:
        constraints = [models.UniqueConstraint(fields=["title"], name="unique_subject")]

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name="related_user"
    )

    def __str__(self):
        return self.title
