from django.db import models
from django.contrib.auth import get_user_model


class Assignment(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, default="")
    created_by = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING, related_name="+"
    )

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
