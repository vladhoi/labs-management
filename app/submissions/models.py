from django.db import models
from assignments.models import Assignment
from django.contrib.auth import get_user_model
from core.storage import OverwriteFileSystemStorage


class Submission(models.Model):
    feedback = models.TextField()
    attached_file = models.FileField(
        upload_to="labs/%Y/%m/%d/", storage=OverwriteFileSystemStorage
    )
    assignment = models.ForeignKey(Assignment, on_delete=models.PROTECT)
    created_by = models.ForeignKey(
        get_user_model(), on_delete=models.DO_NOTHING, related_name="+"
    )

    def __str__(self):
        return self.assignment.title
