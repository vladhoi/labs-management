from django.contrib import admin
from .models import Submission


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("id", "feedback", "attached_file", "created_by")


admin.site.register(Submission, SubmissionAdmin)
