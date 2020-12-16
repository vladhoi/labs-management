from django.db import models
from django.utils import timezone
from django.conf import settings


class AbstractTableMeta(models.Model):
    created_at = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="+",
        default=None,
        null=True,
    )
    updated_at = models.DateField(default=timezone.now)
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="+",
        default=None,
        null=True,
    )

    class Meta:
        abstract = True
